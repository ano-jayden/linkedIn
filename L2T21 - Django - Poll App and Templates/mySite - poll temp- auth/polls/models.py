# polls/models.py

from django.db import models
from django.utils import timezone

class Poll(models.Model):
    """Model representing a poll question."""
    question = models.CharField(max_length=200)  # The question text
    pub_date = pub_date = models.DateTimeField(default=timezone.make_aware(timezone.datetime(2023, 1, 1)))

    def __str__(self):
        """Return the string representation of the poll."""
        return self.question

class Choice(models.Model):
    """Model representing a choice for a specific poll."""
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)  # The poll to which this choice belongs
    choice_text = models.CharField(max_length=200)  # The text of the choice
    votes = models.IntegerField(default=0)  # The number of votes for this choice

    def __str__(self):
        """Return the string representation of the choice."""
        return self.choice_text
