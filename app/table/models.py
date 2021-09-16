from django.db import models


class User(models.Model):
  id = models.AutoField(help_text="User Primary Key", primary_key=True)
  username = models.CharField(max_length=50, blank=False, null=False,
                              unique=True)
  email = models.EmailField(blank=False, null=False)
  enabled = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Plan(models.Model):
  EVALUATION = (
    ('A', 'Perfect'),
    ('B', 'Good'),
    ('C', 'Not Bad'),
    ('D', 'Failed'),
  )
  user_id = models.ForeignKey(User, related_name="user",
                              on_delete=models.CASCADE, db_column="user_id")
  title = models.CharField(max_length=150, blank=False, null=False)
  description = models.TextField(max_length=500, blank=True, null=True)
  evaluation = models.CharField(help_text="Plan achievement evaluation", max_length=1, choices=EVALUATION)
  start = models.DateTimeField(help_text="The start of the execution period "
                                         "of the plan", blank=False, null=False)
  end = models.DateTimeField(help_text="The end of the execution period of "
                                       "the plan", blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class TimeTable(models.Model):
  id = models.BigAutoField(help_text="TimeTable Primary Key", primary_key=True)
  plan_id = models.ForeignKey(Plan, related_name="plan",
                              on_delete=models.CASCADE, db_column="plan_id")
  title = models.CharField(max_length=100, blank=False, null=False)
  memo = models.TextField(max_length=500, blank=True, null=True)
  from_at = models.TimeField(help_text="The start time", blank=False, null=False)
  to_at = models.TimeField(help_text="The end time", blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
