from flask import Blueprint, jsonify

# 创建蓝图对象
api1_bp = Blueprint('api1', __name__)

# 定义路由
@api1_bp.get('/hello')
def hello_api1():
    return jsonify({'message': 'Hello from API 1!'})

@api1_bp.route('/goodbye')
def goodbye_api1():
    return jsonify({'message': 'Goodbye from API 1!'})
