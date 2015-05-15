from django.contrib import admin
from teams.models import Team 
from players.models import Player


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 0
    readonly_fields = ('name', 'position', 'nba_team')

    fieldsets = [
        ('Players', {'fields': ['name', 'position', 'nba_team']}),
    ]

class TeamAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'record')

    # fields = ('players',)
    inlines = [PlayerInline,]

    def players(self, obj):
        return obj.players

admin.site.register(Team, TeamAdmin)