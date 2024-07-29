from django.db import models

# Create your models here.
class Contact(models.Model):

    Name = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Email = models.EmailField()
    Message = models.TextField()

    def __str__(self):
        return self.Name + '  ' + self.Subject + '  ' + self.Email + '  ' + self.Message