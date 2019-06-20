from django.shortcuts import render
from .models import WeeklyChallenges


def challenge(request):
    all_challenges = WeeklyChallenges.objects.all()
    return render(request, 'challenge_list.html', {'challenges': all_challenges})


def weekly_challenge(request, week):
    obj = WeeklyChallenges.objects.get(week=week)
    return render(request, 'weekly_challenge.html', {'object': obj})
