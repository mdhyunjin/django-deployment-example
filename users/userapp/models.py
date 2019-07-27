from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    emalil = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return "{0} {1}: {2}".format(self.firstName,
                                    self.lastName,
                                    self.emalil)
