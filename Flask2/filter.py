from flask import Flask, Blueprint,request, current_app

# 创建蓝图对象
filter_bp = Blueprint('filter_bp', __name__)

# 定义请求过滤器，在请求到达视图函数之前执行
@filter_bp.before_request
def before_request():
    current_app.logger.info('Request Path: %s', request.path)
    current_app.logger.info('Request Method: %s', request.method)
    current_app.logger.info('Request Headers: %s', request.headers)
    current_app.logger.info('Request Data: %s', request.data)

# 定义请求过滤器，在视图函数处理完请求后执行
@filter_bp.after_request
def after_request(response):
    current_app.logger.info('Response Status Code: %s', response.status_code)
    current_app.logger.info('Response Headers: %s', response.headers)
    current_app.logger.info('Response Data: %s', response.get_data())
    return response