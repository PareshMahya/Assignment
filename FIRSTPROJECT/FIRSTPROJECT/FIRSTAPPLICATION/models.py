from django.db import models

# Create your models here.
class Student(models.Model):
    CONTACT_CHOICES = [
        ('Email', 'Email'),
        ('Mail', 'Mail'),
        ('Phone', 'Phone'),
    ]
    Name = models.CharField(max_length=25)
    #ID = models.IntegerField(max_digits=2)
    Contact = models.CharField(
        max_length=10,
        choices=CONTACT_CHOICES,
        default='Email',
    )
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name