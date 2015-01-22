bball
=====

basic project to help users evaluate NBA players from a fantasy basketball perspective


SETUP
======

mkvirtualenv 'bball'
pip install numpy
pip install -r pip-requirements.txt
./manage.py makemigrations
./manage.py syncdb
./manage.py scrape_players
./manage.py backfill_stats
./manage.py create_teams

