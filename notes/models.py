from __future__ import unicode_literals

from django.db import models

class Note(models.Model):
    note_title = models.CharField(max_length=100,default="blank")
    note_content = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.note_title