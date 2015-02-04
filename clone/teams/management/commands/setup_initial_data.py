from django.core import management
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Scrape data from rotoworld and basketball-reference and load into db
    """
    def handle(self, *args, **options):
    	management.call_command('scrape_players')
    	management.call_command('get_schedule')
    	management.call_command('get_tipoffs')
    	management.call_command('get_boxscores')
    	management.call_command('populate_stats')
    	management.call_command('create_teams')
        management.call_command('generate_matchups')
