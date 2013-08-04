#From http://www.jeffknupp.com/blog/2012/10/24/starting-a-django-14-project-the-right-way/
from fabric.api import local

def prepare_deployment(branch_name):
    local('python manage.py test Control_System')
    local('git add -p && git commit')
