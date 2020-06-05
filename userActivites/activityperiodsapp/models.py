from django.db import models
import pytz

class User(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones,pytz.all_timezones))
    real_name = models.CharField(max_length=225)
    tz = models.CharField(max_length=225,choices=TIMEZONES)

class ActivityPeriod(models.Model):
    activity = models.ForeignKey('activityperiodsapp.User', on_delete=models.CASCADE, null=True,
                                         blank=True, related_name="activity_periods")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()