from django.db import models

class Message(models.Model):
  t = models.DateTimeField(auto_now=True)
  name = models.CharField(max_length=100)
  body = models.TextField()

  def __unicode__(self):
    return "%s %s: %r" % (self.t, self.name, self.body)
