bball
===================

basic project to help users evaluate NBA players from a fantasy basketball perspective

===================

mkvirtualenv 'bball'
pip install numpy
pip install -r pip-requirements.txt
./manage.py makemigrations
./manage.py syncdb
./manage.py setup_initial_data


daily crons (to be run at 1am):
./manage.py get_bosxcores
./manage.py populate_stats
./manage.py get_recent_notes


weekly crons (to be run mondays at 1am):
./manage.py record matchup_scores





