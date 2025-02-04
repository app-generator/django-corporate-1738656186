# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Position(models.Model):

    #__Position_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Position_FIELDS__END

    class Meta:
        verbose_name        = _("Position")
        verbose_name_plural = _("Position")


class Worker(models.Model):

    #__Worker_FIELDS__
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    #__Worker_FIELDS__END

    class Meta:
        verbose_name        = _("Worker")
        verbose_name_plural = _("Worker")


class Tasktype(models.Model):

    #__Tasktype_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Tasktype_FIELDS__END

    class Meta:
        verbose_name        = _("Tasktype")
        verbose_name_plural = _("Tasktype")


class Task(models.Model):

    #__Task_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    deadline = models.DateTimeField(blank=True, null=True, default=timezone.now)
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=255, null=True, blank=True)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ForeignKey(Worker, on_delete=models.CASCADE)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")



#__MODELS__END
