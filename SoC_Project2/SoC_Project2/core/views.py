from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def compete(request):
    return render(request, 'compete.html')

def leaderboard(request):
    return render(request, 'leaderboard.html')

def mentors(request):
    return render(request, 'mentors.html')

def profile(request):
    return render(request, 'profile.html')
