from django.contrib import admin
from .models import PlayerList, Team, Match, Stats, Dummy


admin.site.register(PlayerList)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Stats)
admin.site.register(Dummy)
