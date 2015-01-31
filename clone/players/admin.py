from django.contrib import admin
from django import forms
from players.models import Player


class PlayerAdminForm(forms.ModelForm):
    recent_notes = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Player


class PlayerAdmin(admin.ModelAdmin):
	list_display = ('name', 'nba_team', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'mpg')
	search_fields = ['name', 'position']

	form = PlayerAdminForm
	fieldsets = [
        (None, {'fields': ['name', 'nba_team', 'position']}),
        ('Recent notes', {'fields': ['recent_notes']}),
        ('Season averages', {'fields': ['ppg','rpg','apg','spg',
        	'bpg','mpg','threespg'],}),
    ]

	readonly_fields = ('ppg','rpg','apg','bpg','spg','mpg','threespg')

admin.site.register(Player, PlayerAdmin)