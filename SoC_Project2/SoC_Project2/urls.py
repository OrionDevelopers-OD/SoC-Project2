"""SoC_Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

from SoC_Project2.core import views
from SoC_Project2.problems import problemviews

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('contests/', include(([
        path('', views.compete, name='compete'),
        path('weekly/', problemviews.challenge, name='weekly_challenge_list'),
        path('weekly/week<int:week>/', problemviews.weekly_challenge, name='weekly_challenge'),
    ], 'core'), namespace='challenges')),   
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('mentors/', views.mentors, name='mentors'),
    path('profilepersonname/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
