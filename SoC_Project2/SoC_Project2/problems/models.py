from django.db import models


class WeeklyChallenges(models.Model):
    DIFFICULTY_LEVEL = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    week = models.IntegerField(default=0)
    problem_name = models.CharField(max_length=50, unique=True)
    problem = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    constraints = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVEL, default='Easy')
    input_example = models.TextField()
    output_example = models.TextField()
