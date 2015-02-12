from django.contrib import admin
from django import forms
from players.models import Player


class PlayerAdminForm(forms.ModelForm):
    recent_notes = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Player


class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name', 'nba_team', 'points', 'assists', 'rebounds', 'steals', 'blocks', 'minutes')
	search_fields = ['name', 'position', 'nba_team']

	form = PlayerAdminForm
	fieldsets = [
        (None, {'fields': ['name', 'nba_team', 'position']}),
        ('Recent notes', {'fields': ['recent_notes']}),
        ('Season stats', {'fields': ['points','rebounds','assists','steals',
        	'blocks','minutes'],}),
    ]

	readonly_fields = ('points','rebounds','assists','blocks','steals','minutes')

admin.site.register(Player, PlayerAdmin)