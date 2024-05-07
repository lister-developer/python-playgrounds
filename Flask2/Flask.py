from flask import Flask, request
import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO) # flask 的默认级别为 WARNING，浙江指定为INFO

# 配置日志记录器
log_handler = logging.FileHandler('app.log')  # 创建一个文件处理器，指定日志文件路径
log_handler.setLevel(logging.DEBUG)  # 设置日志级别为 INFO
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 设置日志格式
log_handler.setFormatter(formatter)  # 应用日志格式到文件处理器
app.logger.addHandler(log_handler)


from api1 import api1_bp
from api2 import api2_bp
from demo_api import demo_api_bp
from filter import filter_bp

# 注册请求过滤器的蓝图
app.register_blueprint(filter_bp)

@app.before_request
def before_request():
    app.logger.info('Request Path: %s', request.path)
    app.logger.info('Request Method: %s', request.method)
    app.logger.info('Request Headers: %s', request.headers)
    app.logger.info('Request Data: %s', request.data)

# 定义请求过滤器，在视图函数处理完请求后执行
@app.after_request
def after_request(response):
    app.logger.info('Response Status Code: %s', response.status_code)
    app.logger.info('Response Headers: %s', response.headers)
    app.logger.info('Response Data: %s', response.get_data())
    return response


# 注册蓝图
app.register_blueprint(api1_bp, url_prefix='/api1')
app.register_blueprint(api2_bp, url_prefix='/api2')
app.register_blueprint(demo_api_bp)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

