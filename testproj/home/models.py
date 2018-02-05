from django.db import models

from oauth2client.contrib.django_util.storage import DjangoORMStorage
from oauth2client.contrib.django_util.models import CredentialsField

from django.contrib.auth.models import User


# Create your models here.

class CredentialsModel(models.Model):
  id = models.ForeignKey(User, primary_key=True)
  credential = CredentialsField()