import functools
from dataclasses import dataclass

from flask import (
    Blueprint, request, jsonify
)

bp = Blueprint('user', __name__, url_prefix='/user')

@dataclass
class UserModel:
    user_id: int
    name: str
    email: str
    

@bp.get("/get-users")
def get_users():
    list = []          ## 空列表
    list.append(UserModel(user_id=1, name="a", email="a"))   ## 使用 append() 添加元素
    list.append(UserModel(user_id=2, name="b", email="b"))
    return jsonify(list)