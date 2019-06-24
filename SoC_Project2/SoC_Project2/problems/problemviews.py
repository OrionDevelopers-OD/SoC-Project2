from django.shortcuts import render
from .models import contestName, Challenges
from django.views.generic import ListView, DetailView


class ChallengeListView(ListView):
    model=Challenges
    ordering = ('problem_name',)
    context_object_name = 'challenge_list'
    template_name = 'compete.html'

    def get_queryset(self):
        queryset = Challenges.objects.all()
        return queryset


def challengeView(request, week):
    obj = Challenges.objects.get(week=week)
    return render(request, 'challenges.html', {'object': obj})
