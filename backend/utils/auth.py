from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def hash_password(password):
    """生成密码哈希"""
    return generate_password_hash(password)

def verify_password(password_hash, password):
    """验证密码"""
    return check_password_hash(password_hash, password)

def create_jwt_token(user_id):
    """创建JWT token"""
    return create_access_token(identity=user_id)