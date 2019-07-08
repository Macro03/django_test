from django.shortcuts import render
import datetime
from django.db import connection
from .models import Log
# Create your views here.
def addLog(log_module,log_context,log_ip,long_user):
    cmd = "insert into log_log(log_module,log_addtime,log_context,log_ip,log_user) values ('%s','%s','%s','%s','%s')"
    cmd = cmd % (log_module,datetime.datetime.now(),log_context,log_ip,long_user)
    cursor = connection.curson()#连接数据库
    cursor.excute(cmd)
    cursor.close()
    return True