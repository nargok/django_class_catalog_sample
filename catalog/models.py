from django.db import models

class Teacher(models.Model):
  kana = models.CharField(max_length=255, null=True)
  name = models.CharField(max_length=255)

class Broadcast(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  teachers = models.ManyToManyField(Teacher)
  examination_start = models.DateTimeField(null=True)
  examination_end = models.DateTimeField(null=True)

class BroadcastLesson(models.Model):
  broadcast = models.ForeignKey(Broadcast, on_delete=models.PROTECT)
  description = models.TextField()