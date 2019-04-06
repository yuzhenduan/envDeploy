# -*- coding: utf-8 -*-
#######################
# deploy.views
#######################

from django.http import HttpResponse

# deploy/health
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")


# deploy/start
def deploy(request):
	pass


# deploy/setNginx/<target>
def set_nginx(request,target):
	pass


# deploy/remove/<env>/<project>
def remove_env_project(request,env,project):
	pass


# deploy/remove/<env>/<drone>/<project>
def remove_drone_project(request,env,drone,project):
	pass


# deploy/config/check/<project>
def config_check(request,project):
	pass


# deploy/byBusiness/<env>/<project>
def deploy_business(request,env,project):
	pass


# deploy/ALL/<env>
def deploy_all(request,env):
	pass


# deploy/diagnose/<project>
def diagnose_project(request,project):
	pass

