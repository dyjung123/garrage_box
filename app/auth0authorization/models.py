from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    pass


class Plan(models.Model):
    EVALUATION = (
        ('A', 'Perfect'),
        ('B', 'Good'),
        ('C', 'Not Bad'),
        ('D', 'Failed'),
    )
    user = models.ForeignKey(settings.API_AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    evaluation = models.CharField(help_text="Plan achievement evaluation",
                                  max_length=1, choices=EVALUATION, null=True,
                                  blank=True)
    start = models.DateTimeField(help_text="The start of the execution period "
                                           "of the plan", blank=False,
                                 null=False)
    end = models.DateTimeField(help_text="The end of the execution period of "
                                         "the plan", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimeTable(models.Model):
    user = models.ForeignKey(settings.API_AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name="plan", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    memo = models.TextField(max_length=500, blank=True, null=True)
    from_at = models.TimeField(help_text="The start time", blank=False,
                               null=False)
    to_at = models.TimeField(help_text="The end time", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
