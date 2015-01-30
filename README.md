bball
===================

basic project to help users evaluate NBA players from a fantasy basketball perspective

===================

mkvirtualenv 'bball'
pip install numpy
pip install -r pip-requirements.txt
./manage.py makemigrations
./manage.py syncdb
./manage.py scrape_players
./manage.py get_schedule
./manage.py get_tipoffs
./manage.py get_boxscores
./manage.py populate_stats
./manage.py create_teams



