from django.contrib import admin
from players.models import Player



class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name', 'nba_team', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'mpg')
	search_fields = ['name', 'position']

	fieldsets = [
        (None,               {'fields': ['name', 'nba_team', 'position']}),
        ('Stats', {'fields': ['ppg','rpg','apg','spg',
        	'bpg','mpg','threespg'],}),
    ]

	readonly_fields = ('ppg','rpg','apg','bpg','spg','mpg','threespg')

admin.site.register(Player, PlayerAdmin)