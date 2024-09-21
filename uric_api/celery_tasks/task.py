from .main import app

# 经过@app.task装饰过，就会被celery识别为任务，否则就是普通的函数
@app.task
def task1():
    print("任务1函数正在执行....")

@app.task
def task2(a, b, c):
    print(f"任务2函数正在执行，参数：{[a, b, c]}....")

@app.task
def task3():
    print(f"任务3函数正在执行....")
    return True

@app.task
def task4(a, b, c):
    print(f"任务4函数正在执行....")
    return a, b, c


# 命令必须在manage.py的父目录下执行
# 启动定时任务首先需要有一个work执行异步任务，然后再启动一个定时器触发任务。
# celery -A celery_tasks.main worker -l info
# # windows下关闭celery，快捷键：ctrl+C即可
#
# # 启动定时器触发 beat  (注意：下面是一条完整指令)
# celery -A celery_tasks.main beat -l info --scheduler  django_celery_beat.schedulers:DatabaseScheduler


# import json
# from host.models import Host
# from django.conf import settings
# from uric_api.utils.key import AppSetting
# @app.task(name='schedule_task')
# def schedule_task(cmd, hosts_ids):
#     """计划任务"""
#     hosts_objs = Host.objects.filter(id__in=hosts_ids)
#     result_data = []
#     private_key, public_key = AppSetting.get(settings.DEFAULT_KEY_NAME)
#     for host_obj in hosts_objs:
#         cli = host_obj.get_ssh(private_key)
#         code, result = cli.exec_command(cmd)
#         result_data.append({
#             'host_id': host_obj.id,
#             'host': host_obj.ip_addr,
#             'status': code,
#             'result': result
#         })
#         print('>>>>', code, result)
#
#     return json.dumps(result_data)
