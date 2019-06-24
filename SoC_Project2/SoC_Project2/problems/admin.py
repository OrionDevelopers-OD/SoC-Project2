from django.contrib import admin

from .models import contestName, Challenges


admin.site.register(Challenges)
admin.site.register(contestName)
