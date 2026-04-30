from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.db.models import Sum
from .models import Transaction
from .serializers import UserSerializer, RegisterSerializer, TransactionSerializer

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"accessToken": token.key, "user": UserSerializer(user).data}, status=201)
        return Response({"message": "Error", "errors": serializer.errors}, status=400)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"accessToken": token.key, "user": UserSerializer(user).data})
        return Response({"message": "Invalid credentials"}, status=401)

class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        income = queryset.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = queryset.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
        return Response({
            "items": serializer.data,
            "summary": {
                "incomeTotal": float(income),
                "expenseTotal": float(expense),
                "balance": float(income - expense)
            }
        })
