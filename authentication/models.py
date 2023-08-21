from django.db import models

# Create your models here.
class SessionToken(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)