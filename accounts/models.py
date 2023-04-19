from django.db import models
from django.contrib.auth.models import Group

try:
    group = Group.objects.get(name='yetkili')
except Group.DoesNotExist:
    group = Group.objects.create(name='yetkili')