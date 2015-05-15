from __future__ import division
from datetime import datetime
from players.models import Player
from schedule.models import Game, StatLine
from django.db.models import Q

ROOT_IMAGE_URL = """http://i.cdn.turner.com/nba/nba/.element/img/2.0/sect/statscube/players/large/"""

def get_image_url(player_name):
    name = player_name.replace(' ','_').lower()
    return "{0}{1}.png".format(ROOT_IMAGE_URL,name)

def todays_opponent(player_id):
    player = Player.objects.get(id=player_id)
    now = datetime.now()
    games = Game.objects.filter(Q(home_team=player.nba_team)| Q(away_team=player.nba_team))
    for game in games:
        if game.date == now.date():
            if game.away_team == player.nba_team:
                return '@{}'.format(game.home_team)
            elif game.home_team == player.nba_team:
                return game.away_team

def todays_game_status(player_id):
    player = Player.objects.get(id=player_id)
    now = datetime.now()
    games = Game.objects.filter(Q(home_team=player.nba_team)| Q(away_team=player.nba_team))
    for game in games:
        if game.date == now.date():
            return game.tipoff


def calculate_totals(player, start_day, end_day):
    # """
    # Returns a dictionary with average stats and total stats for the given time period.
    # """
    start_day = start_day
    end_day = end_day

    games_played = 0
    total_stats = {"games_played": 0, "minutes": 0, "fgm": 0, "fga": 0, "ftm": 0, "fta": 0,
        "threes": 0, "rebounds": 0, "assists": 0, "steals": 0, "blocks": 0, "turnovers": 0, "points": 0}

    games = Game.objects.filter(Q(home_team=player.nba_team)| Q(away_team=player.nba_team))
    games = games.filter(Q(date__gte=start_day) & Q(date__lte=end_day))

    for game in games:
        try:
            sl = StatLine.objects.get(game_id=game.id, player_id=player.id)
        except StatLine.DoesNotExist:
            continue
        if sl:
            total_stats['games_played'] += 1
            minutes = sl.mp[:2].replace(':','')
            total_stats['minutes'] += int(minutes)
            total_stats['fgm'] += int(sl.fgm)
            total_stats['fga'] += int(sl.fga)
            total_stats['ftm'] += int(sl.ftm)
            total_stats['fta'] += int(sl.fta)
            total_stats['threes'] += int(sl.threesm)
            total_stats['rebounds'] += int(sl.trbs)
            total_stats['assists'] += int(sl.asts)
            total_stats['steals'] += int(sl.stls)
            total_stats['blocks'] += int(sl.blks)
            total_stats['turnovers'] += int(sl.tos)
            total_stats['points'] += int(sl.pts)

    if total_stats.get('fga') == 0:
        total_stats['fgpct'] = 0.00
    else:
        total_stats['fgpct'] = round((total_stats.get('fgm')/total_stats.get('fga')), 3)

    if total_stats.get('fta') == 0:
        total_stats['ftpct'] = 0.00
    else:
        total_stats['ftpct'] = round((total_stats.get('ftm')/total_stats.get('fta')), 3)

    return total_stats

def calculate_avgs(total_stats):
    games_played = total_stats.pop('games_played')
    fgpct = total_stats.pop('fgpct')
    ftpct = total_stats.pop('ftpct')
    avg_stats = {}
    for k, v in total_stats.items():
       if games_played == 0:
           avg = 0
       else:
           avg = v/games_played
       avg_stats[k] = round(avg, 1)
    avg_stats['games_played'] = games_played
    avg_stats['fgpct'] = fgpct
    avg_stats['ftpct'] = ftpct

    return avg_stats
	