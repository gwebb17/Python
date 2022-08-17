from django.db import models

NAME_CHOICES = {
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms')
}



# Create your models here.
class Profile(models.Model):
    Prefix = models.CharField(max_length=10, default='', choices=NAME_CHOICES)
    First_name = models.CharField(max_length=20, default='', blank=True, null=False)
    Last_name = models.CharField(max_length=20, default='', blank=True, null=False)
    Email = models.CharField(max_length=50, default='', blank=True, null=False)
    Username = models.CharField(max_length=50, default='', blank=True, null=False)


    objects= models.Manager()

    def __str__(self):
        return self.First_name