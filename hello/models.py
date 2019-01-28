from django.db import models

# Create your models here.
class HelloWorld(models.Model):
    user_name = models.CharField(max_length=30)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name + " says " + self.content
