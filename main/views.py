# -*- coding: utf-8 -*-
#######################
# main.views
#######################
import demjson
from django.http import HttpResponse

def health(request):
    return HttpResponse(<h1>Yes, We can!</h1>)

def deploy(request):
    '''
    params={"env":env,"targetHost":default,"project":project,"repository":orign,"branch"::master,"config":test,"sha":None,"operator":None,"type":test,"setNginx":True,"build":True,"check"}
    '''
    return

def deploySimple(request):
    '''
    params={"env":env,"targetHost":default,"project":project,"repository":orign,"branch":master,"config":test,"sha":None}
    '''
    return
