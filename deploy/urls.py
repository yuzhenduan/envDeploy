# -*- coding: utf-8 -*-
#######################
# deploy.urls
#######################
"""
  1. 部署服务
  2. add DNS
  3. nginx设置
  4. config check
  5. 诊断
"""
from django.urls import path
from deploy import views

urlpatterns = [
    path('health/', views.health,name="health"),
    path('start/',views.deploy,name="deploy"),
    path('setNginx/<env>/<target>/<project>/',views.set_project_nginx,name="set_project_nginx"),
    path('addDNS/<env>/<project>/',views.add_project_dns,name="add_project_dns"),
    path('configCheck/<project>/',views.project_config_check,name="project_config_check"),
    path('diagnose/<project>/',views.diagnose_project,name="diagnose_project"),
]
