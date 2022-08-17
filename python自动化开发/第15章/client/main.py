from flask import request, jsonify
from taskInfo import *

# API接口，接收任务请求
@app.route('/')
def task_receive():
    taskId = request.args.get('taskId', '')
    name = request.args.get('name', '')
    kwargs = {}
    kwargs['train_date'] = '2018-10-29'
    kwargs['from_station'] = '广州'
    kwargs['to_station'] = '武汉'
    AutoTask.delay(taskId, name, **kwargs)
    return jsonify({"result": "success",
                    "taskId": taskId,})

# 先启动celery，在PyCharm的Terminal输入以下指令：
# celery -A taskInfo.celery worker -l info -P solo
# 再启动运行网站
if __name__ == '__main__':
    app.run(port=8000, debug=True)