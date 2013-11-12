from fabric.api import local
from fabric.api import lcd

def deploy():
	with lcd('/path/to/my/prod/area/'):
		local('git pull /media/Tinkerspace/CSCE470/finalproject/BarCrawl/')
		local('python manage.py migrate barcrawl')
		local('python manage.py test barcrawl')
		local('/my/command/to/restart/webserver')

def prepare_deployment(branch_name):
	local('python manage.py test barcrawl')
	local('git add -p && git commit')
	local('git checkout master && git merge ' + branch_name)
