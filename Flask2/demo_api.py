from flask import Flask, Blueprint, jsonify
from flask import request, current_app
from dataclasses import dataclass

@dataclass
class MyData:
    name: str
    age: int

demo_api_bp = Blueprint('demo_api_bp', __name__)


# 从 form-data 中取值
@demo_api_bp.route("/login", methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username)
    return "login success"
    
# 响应JSON结构的结果
@demo_api_bp.post("/json-response")
def json_response():
    current_app.logger.debug('A value for debugging')
    current_app.logger.warning('A warning occurred (%d apples)', 42)
    current_app.logger.error('An error occurred')
    data = MyData(
        name="Lister",
        age=18
    )
    return jsonify(data)

# 接收 json 格式的参数
@demo_api_bp.post("/json-request")
def json_request():
    # 获取 JSON 格式的请求体参数，并转换成 MyData 对象
    json_data = request.json
    my_data = MyData(**json_data)

    # 现在你可以像操作普通对象一样操作 my_data
    current_app.logger.info(my_data.name)
    current_app.logger.info(my_data.age)
    current_app.logger.info("json-request")

    return 'JSON data processed'