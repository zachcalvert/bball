import copper
import pandas as pd
import requests
from bs4 import BeautifulSoup

from players.models import Player
from teams.models import Team

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Scrapes the rotoworld player page to import current NBA players into the app.
    TODO: does not pull in the team they play for currently
    """
    def handle(self, *args, **options):
    	team1 = Team.objects.create(name='Stairway to Kevin', wins=73, losses=35)

    	team1_players = ('Kevin Durant', 'Rajon Rondo', 'Eric Gordon', 'Dirk Nowitzki',
    		'Andrew Bogut', 'Mo Williams', 'Kyle Korver', 'Roy Hibbert', 'Draymond Green',
    		'Hassan Whiteside', 'Mike Conley', 'Kevin Martin',)

    	for team1_player in team1_players:
    		try:
    			player = Player.objects.get(name=team1_player)
    		except Player.DoesNotExist:
    			print('could not find player: {}'.format(team1_player))
    			pass
    		player.team = team1
    		player.save()

    	team2 = Team.objects.create(name='Team Name', wins=65, losses=43)

    	team2_players = ('George Hill', 'Mario Chalmers', 'Klay Thompson', 'Anthony Davis',
    		'Alex Len', 'Nicolas Batum', 'Jimmy Butler', 'Markieff Morris', 'Bradley Beal',
    		'Omer Asik', 'DeAndre Jordan', 'Brandon Knight', 'Wilson Chandler',)
    	
    	for team2_player in team2_players:
    		try:
    			player = Player.objects.get(name=team2_player)
    		except Player.DoesNotExist:
    			print('could not find player: {}'.format(team2_player))
    			pass
    		player.team = team2
    		player.save()

    	team3 = Team.objects.create(name='Evil Twin Cliff Paul', wins=52, losses=56)

    	team3_players = ('Kyle Lowry', 'Lance Stephenson', 'Demar Derozan', 'Carlos Boozer',
    		'Tristan Thompson', 'Isaiah Thomas', 'Greg Monroe', 'Chris Paul', 'Jeff Teague',
    		'Tyson Chandler', 'Tony Wroten', 'Kelly Olynyk', 'Nick Young',)
    	
    	for team3_player in team3_players:
    		try:
    			player = Player.objects.get(name=team3_player)
    		except Player.DoesNotExist:
    			print('could not find player: {}'.format(team3_player))
    			pass
    		player.team = team3
    		player.save()

        team4 = Team.objects.create(name='Team walsh', wins=72, losses=35, ties=1)

        team4_players = ('Louis Williams', 'James Harden', 'Joe Johnson', 'Josh Smith',
            'Marc Gasol', 'Michael Carter-Williams', 'Nikola Vucevic', 'Jrue Holiday', 'Jeff Green',
            'Jordan Hill', 'Zaza Pachulia', 'Khris Middleton', 'Timofey Mozgov',)
        
        for team4_player in team4_players:
            try:
                player = Player.objects.get(name=team4_player)
            except Player.DoesNotExist:
                print('could not find player: {}'.format(team4_player))
                pass
            player.team = team4
            player.save()

        team5 = Team.objects.create(name='Team Calero', wins=69, losses=39)

        team5_players = ('Brandon Jennings', 'J.R. Smith', 'Tyreke Evans', 'Paul Millsap',
            'DeMarcus Cousins', 'Damian Lillard', 'Mason Plumlee', 'Rudy Gay', 'Trevor Ariza',
            'Rudy Gobert', 'Tobias Harris', 'Jusuf Nurkic', 'Dion Waiters',)
        
        for team5_player in team5_players:
            try:
                player = Player.objects.get(name=team5_player)
            except Player.DoesNotExist:
                print('could not find player: {}'.format(team5_player))
                pass
            player.team = team5
            player.save()


        team6 = Team.objects.create(name='Team Waritz', wins=58, losses=50)

        team6_players = ('Russell Westbrook', 'Evan Turner', 'Paul Pierce', 'Tim Duncan',
            'Brook Lopez', 'Corey Brewer', 'Nene Hilario', 'Chris Bosh', 'Ryan Anderson',
            'Jose Calderon', 'Ty Lawson', 'Al Horford', 'Dwyane Wade',)
        
        for team6_player in team6_players:
            try:
                player = Player.objects.get(name=team6_player)
            except Player.DoesNotExist:
                print('could not find player: {}'.format(team6_player))
                pass
            player.team = team6
            player.save()


        team7 = Team.objects.create(name='Team Eyler', wins=53, losses=53, ties=2)

        team7_players = ('Goran Dragic', 'Kyrie Irving', 'Thaddeus Young', 'Gorgui Dieng',
            'Al Jefferson', 'Trey Burke', 'David West', 'John Wall', 'Demarre Carroll',
            'Nerlens Noel', 'Ricky Rubio', 'Gerald Henderson', 'Nikola Pekovic',)
        
        for team7_player in team7_players:
            try:
                player = Player.objects.get(name=team7_player)
            except Player.DoesNotExist:
                print('could not find player: {}'.format(team7_player))
                pass
            player.team = team7
            player.save()

        team8 = Team.objects.create(name='Team wilgus', wins=49, losses=57, ties=2)

        team8_players = ('Avery Bradley', 'Andre Iguodala', 'Chandler Parsons', 'Tyler Zeller',
            'Derrick Favors', 'Stephen Curry', 'Channing Frye', 'Andre Drummond', 'Gerald Green',
            'Reggie Jackson', 'Joakim Noah', 'Deron Williams', 'Arron Afflalo',)
        
        for team8_player in team8_players:
            try:
                player = Player.objects.get(name=team8_player)
            except Player.DoesNotExist:
                print('could not find player: {}'.format(team8_player))
                pass
            player.team = team8
            player.save()

        # team9 = Team.objects.create(name='Evil Twin Cliff Paul', wins=52, losses=56)

        # team9_players = ('Kyle Lowry', 'Lance Stephenson', 'Demar Derozan', 'Carlos Boozer',
        #     'Tristan Thompson', 'Isiah Thomas', 'Greg Monroe', 'Chris Paul', 'Jeff Teague',
        #     'Tyson Chandler', 'Tony Wroten', 'Kelly Olylnk', 'Nick Young',)
        
        # for team9_player in team9_players:
        #     try:
        #         player = Player.objects.get(name=team9_player)
        #     except Player.DoesNotExist:
        #         print('could not find player: {}'.format(team9_player))
        #         pass
        #     player.team = team9
        #     player.save()

        # team10 = Team.objects.create(name='Evil Twin Cliff Paul', wins=52, losses=56)

        # team10_players = ('Kyle Lowry', 'Lance Stephenson', 'Demar Derozan', 'Carlos Boozer',
        #     'Tristan Thompson', 'Isiah Thomas', 'Greg Monroe', 'Chris Paul', 'Jeff Teague',
        #     'Tyson Chandler', 'Tony Wroten', 'Kelly Olylnk', 'Nick Young',)
        
        # for team10_player in team10_players:
        #     try:
        #         player = Player.objects.get(name=team10_player)
        #     except Player.DoesNotExist:
        #         print('could not find player: {}'.format(team10_player))
        #         pass
        #     player.team = team10
        #     player.save()


        # team11 = Team.objects.create(name='Evil Twin Cliff Paul', wins=52, losses=56)

        # team11_players = ('Kyle Lowry', 'Lance Stephenson', 'Demar Derozan', 'Carlos Boozer',
        #     'Tristan Thompson', 'Isiah Thomas', 'Greg Monroe', 'Chris Paul', 'Jeff Teague',
        #     'Tyson Chandler', 'Tony Wroten', 'Kelly Olylnk', 'Nick Young',)
        
        # for team11_player in team11_players:
        #     try:
        #         player = Player.objects.get(name=team11_player)
        #     except Player.DoesNotExist:
        #         print('could not find player: {}'.format(team11_player))
        #         pass
        #     player.team = team11
        #     player.save()

        # team12 = Team.objects.create(name='Evil Twin Cliff Paul', wins=52, losses=56)

        # team12_players = ('Kyle Lowry', 'Lance Stephenson', 'Demar Derozan', 'Carlos Boozer',
        #     'Tristan Thompson', 'Isiah Thomas', 'Greg Monroe', 'Chris Paul', 'Jeff Teague',
        #     'Tyson Chandler', 'Tony Wroten', 'Kelly Olylnk', 'Nick Young',)
        
        # for team12_player in team12_players:
        #     try:
        #         player = Player.objects.get(name=team12_player)
        #     except Player.DoesNotExist:
        #         print('could not find player: {}'.format(team12_player))
        #         pass
        #     player.team = team12
        #     player.save()

