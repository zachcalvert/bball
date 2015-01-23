bball
=====

basic project to help users evaluate NBA players from a fantasy basketball perspective


SETUP:

sudo easy_install virtualenv


SAMPLE BASH PROFILE
===========================================================================================================
export PATH=/opt/local/bin:/opt/local/sbin:/bin:/usr/bin:/usr/local/bin:/usr/sbin:/sbin:/usr/local/git/bin

#Python mysql connector needs these paths set
export PATH=/usr/local/mysql/bin/:$PATH
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib:$DYLD_LIBRARY_PATH

# See http://www.doughellmann.com/docs/virtualenvwrapper/
export WORKON_HOME=$HOME/.virtualenvs
export PIP_DOWNLOAD_CACHE=$HOME/.pip_download_cache
source /usr/local/bin/virtualenvwrapper.sh

==========================================================================================================



mkvirtualenv 'bball'
pip install numpy
pip install -r pip-requirements.txt
./manage.py makemigrations
./manage.py syncdb
./manage.py scrape_players
./manage.py backfill_stats
./manage.py create_teams



