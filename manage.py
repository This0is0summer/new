from flask import Flask
# 导入扩展Flask_cript
from flask_migrate import Manager
from flask_migrate import Migrate
#  ManagerCommand
# 导入flask_sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy
# 导入配置对象
from .config1 import Config
# 导入配置对象

app = Flask(__name__)
# 使用配置对象
app.config.from_object(Config)
# 数据库实例
db = SQLAlchemy(app)
# 实例化管理对象
manage = Manager(app)
# 使用迁移框架
Migrate(app)
# 通过管理器对象，添加迁移命令
# 不可以使用
# manage.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return "this is index"

if __name__ == '__main__':
    app.run(debug=True, port=8080)