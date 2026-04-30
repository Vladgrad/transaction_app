from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



class User(AbstractUser):
       id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
       
       email = models.EmailField(unique=True)
       
       name = models.CharField(max_length=255)
       
       USERNAME_FIELD = 'email'
       REQUIRED_FIELDS = ['username', 'name']
       
       
       def __str__(self):
              return self.email
       
       
class Transaction(models.Model):
       id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
       user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
       type = models.CharField(max_length=10)
       amount = models.DecimalField(max_digits=15, decimal_places=2)
       currency = models.CharField(max_length=3, default='RUB')
       category = models.CharField(max_length=100)
       comment = models.TextField(blank=True, null=True)
       occurredAt = models.DateTimeField()
       createdAt = models.DateTimeField(auto_now_add=True)
       updatedAt = models.DateTimeField(auto_now=True)