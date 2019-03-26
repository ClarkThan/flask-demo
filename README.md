# flask-demo

> 准备

+ 更新代码: `git pull origin` 或者重新clone
+ 准备运行环境: `cd flask-demo && pipenv install`
+ 激活运行环境: `pipenv shell`
+ 准备数据库(也可单独创建): `python` 进入
    + from app import app, db
    + ctx = app.app_context(); ctx.push()
    + db.create_all()
    + ctx.pop()
+ 上一步成功的话, 当前目录会增加**test.db**文件
+ 运行程序: `python app.py`

> 用例(分别浏览器中访问如下链接)

+ http://127.0.0.1:5000/tb
+ 另外插入n条数据: `sqlite3 test.db`
    + insert into user values (3, 'Adam', 'adam@qq.com'), (4, 'John', 'john@qq.com');
+ http://127.0.0.1:5000/tb