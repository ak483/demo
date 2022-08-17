from admin import *
from flask import request, jsonify

# API接口，用于接收client的运行结果
# http://127.0.0.1:8080/?taskId=3&name=mytest&status=Done
@app.route('/')
def callBack():
    # 获取GET的请求参数
    taskId = request.args.get('taskId', '')
    name = request.args.get('name', '')
    status = request.args.get('status', '')
    if taskId and name:
        # 在任务记录表修改任务执行状态
        task = TaskRecord.query.filter_by(id=int(taskId)).first()
        task.status = status
        # 释放任务的状态锁
        info = ProgramInfo.query.filter_by(name=name).first()
        info.statusLock = ''
        db.session.commit()
        # 返回响应内容
        response = {"result": "success"}
        return jsonify(response)
    else:
        # 返回响应内容
        response = {"result": "fail"}
        return jsonify(response)

# 网站启动运行
if __name__ == '__main__':
    app.run(port=8080, debug=True)