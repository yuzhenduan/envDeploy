# -*- coding: utf-8 -*-
#######################
# deploy.views
#######################
import time
from django.http import HttpResponse
from deploy import models


# deploy/health
def health(request):
    return HttpResponse("<h1>Yes, We Can!</h1>")


# deploy/start
def deploy(request):
    """
    需要参数的时候获取并验证必须的参数
    1. 接受和验证传递进来的必要参数
    2. 权限校验
    3. config check
    4. 设置nginx(总机，目标)
    5. 拉取分支
    6. 打包构建服务
    7. 发送文件到指定机器
    8. 启动并探测服务
    9. 发送通知或记录日志
    status={"accept_vars":{"env":"输入env不存在",
                           "project":"输入project不存在",},
            "env_vars":{"env":"未获取到配置",
                        "hosts":"未获取到部署机器",
                        "db":"未获取到数据库信息"},
            "project_vars":{"gitpath":"未配置gitpath",
                            "domainname":"未配置域名",
                            "domainname_exp":"未配置域名表达式",
                            "mgt_port":"未配置管理端口，一般用于关闭服务",
                            "listen_port":"未配置listen_port，必须配置",
                            "deploy_type":"未配置部署类型",
                            "status":"已下线",
                            "config_name":"配置中心名字",
                            "config_token":"配置中心token"},
            "roles":{"owner":"项目归属",
                     "email":"email",
                     "qa":"测试qa",
                     "deploy_usre":"执行人",
                     "current_privilege":"没有执行权限",
                     "datetime":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())},
            "config":{"dns":"检查通过",
                      "db_url":"检查通过",
                      "status":"规则全部通过"},
            "nginx":{"openRestry":"配置未发生变化",
                     "jumper":"配置未发生变化",
                     "target":"配置未发生变化",
                     "drone":"配置未发生变化"},
            "git":{"pull":"拉取成功",
                   "branch":"已切到指定分支"},
            "build":{"status":"successful",
                     "deploy_type":"spring-meteor"},
            "send":{"package":"successful",
                    "config":"successful",
                    "startup":"successful"},
            "start":{"host":"启动主机",
                     "port":"启动端口",
                     "status":"alive",
                     "health":"服务探测接口正常"}
            }
    """
    # 1 接受和校验
    vars_status,accept_vars=get_and_check(request)
    env_vars_status,env_vars=get_env_vars(env)
    project_vars_status,project_vars=get_project_vars(env,project)
    # 2 权限校验(预留)

    # 3 config check
    config_check_status=project_config_check()

    # 4 set nginx(获取环境和相关的权限设置)
    nginx_status=set_nginxs()

    # 5 拉取和切换分支
    git_status=clone_and_set_git()
    
    # 6 打包构建服务
    build_status=build_project()

    # 7 send locally to the target machine
    send_status=send_to_target()

    # 8 启动并探活服务
    start_status=start_and_spy()

# deploy/setNginx/<env>/<target>/<project>
def set_project_nginx(request,env,target):
   """
   """
   pass


# deploy/addDNS/<env>/<project>
def add_project_dns(request,env,project):
   """
   """
   pass


# deploy/configCheck/<project>
def project_config_check(request,project):
	pass



# deploy/diagnose/<project>
def diagnose_project(request,project):
	pass

