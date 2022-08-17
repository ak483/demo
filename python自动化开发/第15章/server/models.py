from settings import *

# 定义自动化程序信息表
class ProgramInfo(db.Model):
    # db.Column是定义字段、db.INT是字段的数据类型
    __tablename__ = 'ProgramInfo'
    id = db.Column(db.INT, primary_key=True)
    clientIP = db.Column(db.String(50))
    introduce = db.Column(db.String(50))
    name = db.Column(db.String(50), unique=True)
    statusLock = db.Column(db.String(50))

# 定义任务记录表
class TaskRecord(db.Model):
    # db.Column是定义字段、db.INT是字段的数据类型
    __tablename__ = 'TaskRecord'
    id = db.Column(db.INT, primary_key=True)
    clientIP = db.Column(db.String(50))
    name = db.Column(db.String(50))
    status = db.Column(db.String(50))
    createTime = db.Column(db.DateTime, server_default=db.func.now())

# 创建数据表
db.create_all()

if __name__=='__main__':
    # 插入数据
    p = ProgramInfo()
    p.clientIP = 'localhost'
    p.introduce = 'MySQLAlchemy'
    p.name = 'SQLAlchemy'
    p.statusLock = ''
    db.session.add(p)
    db.session.commit()
    # 更新数据
    name = 'SQLAlchemy'
    qs = ProgramInfo.query.filter_by(name=name)
    qs.update({ProgramInfo.introduce: 'YourSQLAlchemy'})
    # 查询数据
    # 查询全表
    print(ProgramInfo.query.all())
    # 条件查询
    print(ProgramInfo.query.filter_by(name='SQLAlchemy').all())
    # 仅查询字段name
    print(db.session.query(ProgramInfo.name).all())
    # 删除某条数据
    name = 'SQLAlchemy'
    qs = ProgramInfo.query.filter_by(name=name).first()
    db.session.delete(qs)
    db.session.commit()