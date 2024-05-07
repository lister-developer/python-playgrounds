from flask import Blueprint, jsonify

# 创建蓝图对象
api2_bp = Blueprint('api2', __name__)

# 定义路由
@api2_bp.route('/hello')
def hello_api2():
    return jsonify({'message': 'Hello from API 2!'})

@api2_bp.route('/goodbye')
def goodbye_api2():
    return jsonify({'message': 'Goodbye from API 2!'})
