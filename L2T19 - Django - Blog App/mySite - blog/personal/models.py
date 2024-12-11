from django.db import models

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Your team is breaking")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
