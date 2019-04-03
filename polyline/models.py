from django.db import models
from datetime import datetime
# Create your models here.

class PolylineData(models.Model):
	filename = models.CharField(max_length=30, blank=True)
	score = models.DecimalField(max_digits=9, decimal_places=6)

	def __str__(self):
            return ('#' + str(self.id) + ' File: ' + str(self.filename) + ' - Score: ' + str(self.score))

class Polyline(models.Model):
	rpi_id=models.CharField(max_length=30, blank=True)
	timestamp = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
            return ('#' + str(self.id) + ' TS: ' + str(self.timestamp).split()[0])