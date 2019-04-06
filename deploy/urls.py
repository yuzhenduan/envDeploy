# -*- coding: utf-8 -*-
#######################
# deploy.urls
#######################

from django.urls import path
from deploy import views

urlpatterns = [
    path('health/', views.health,name="health"),
    path('start/',views.deploy,name="deploy"),
    path('setNginx/<target>/',views.set_nginx,name="set_nginx"),
    path('remove/<env>/<project>/',views.remove_env_project,name="remove_env_project"),
    path('remove/<env>/<drone>/<project>/',views.remove_drone_project,name="remove_drone_project"),
    path('config/check/<project>/',views.config_check,name="deploy"),
    path('byBusiness/<env>/<business>',views.deploy_business,name="deploy_business"),
    path('ALL/<env>/',views.deploy_all,name="deploy_all"),
    path('diagnose/<project>/',views.diagnose_project,name="diagnose_project"),
]
