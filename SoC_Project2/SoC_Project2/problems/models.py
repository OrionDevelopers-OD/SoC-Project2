from django.db import models
from django.db.models.signals import pre_save

class contestName(models.Model):
    CONTEST_NAME=(
        ('Weekly Challenges Series', 'Weekly Challenges Series'),
        ('Other Contests','Other Contests'),
        # more contests add here
    )
    contest = models.CharField(max_length=30, choices=CONTEST_NAME)

    def __str__(self):
        return self.contest

class Challenges(models.Model):
    DIFFICULTY_LEVEL = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    contest = models.ForeignKey(contestName, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    problem_name = models.CharField(max_length=50, unique=True)
    problem = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    constraints = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_LEVEL, default='Easy')
    input_example = models.TextField()
    output_example = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.problem_name

