from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=128)
    join_date = models.DateField(auto_now_add=True, null=True)
    subscription_ends = models.DateField(null=True, blank=True)
    social_id = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(null=True, default=False)
    telephone = models.CharField(max_length=20, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Post(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)