from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, MeView, TransactionViewSet

router = DefaultRouter(trailing_slash=False) 
router.register(r'transactions', TransactionViewSet, basename='transactions')

urlpatterns = [

    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/me', MeView.as_view(), name='me'),
    

    path('', include(router.urls)),
]
