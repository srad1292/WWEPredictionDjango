"""
Definition of models.
"""

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Wrestler(models.Model):
    def __str__(self):
        return u'{0}'.format(self.name)
    name = models.CharField(max_length = 40, unique=True)


class Event(models.Model):
	name = models.CharField(max_length = 40)
	date = models.DateField()

class Match(models.Model):
	event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
	number_of_participants = models.IntegerField()
	match_type = models.CharField(max_length = 80)
	title = models.CharField(max_length = 80, blank=True)
	display = models.TextField()
	prediction = models.CharField(max_length = 255)
	winner = models.CharField(max_length = 255)

class Match_Wrestler_Results(models.Model):
	match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
	wrestler_id = models.ForeignKey(Wrestler, on_delete=models.CASCADE)
	won = models.BooleanField()
	lost = models.BooleanField()
	draw = models.BooleanField()
	prediction = models.BooleanField()

	class Meta:
		unique_together = (("match_id", "wrestler_id"),)