from django.shortcuts import render
from SoC_Project2.problems.models import Challenges


def dashboard(request): 
    all_challenges = Challenges.objects.all()
    return render(request, 'dashboard.html', {'challenges': all_challenges})

def leaderboard(request):
    return render(request, 'leaderboard.html')

def mentors(request):
    return render(request, 'mentors.html')

def profile(request):
    return render(request, 'profile.html')
