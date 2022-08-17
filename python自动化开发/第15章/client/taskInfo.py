from settings import *
from trainTicket import *
import requests
# 定义并注册异步任务
@celery.task()
def AutoTask(taskId, name, **kwargs):
    try:
        if name == 'printPDF':
            print('printPDF')
        elif name == 'trainTicket':
            train_date = kwargs['train_date']
            from_station = kwargs['from_station']
            to_station = kwargs['to_station']
            info = get_info(train_date, from_station, to_station)
            print(str(info))
        status = 'Done'
    except Exception as e:
        print(e)
        status = 'Fail'
    # 将运行结果返回到调度中心
    url = 'http://127.0.0.1:8080/?name=' + name + \
          '&taskId=' + str(taskId) + '&status=' + status
    try:
        requests.get(url)
    except:pass
    # 返回任务状态
    return status