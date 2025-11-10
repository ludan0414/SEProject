from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity  # 添加这行
from models import db, User
from utils.auth import hash_password, verify_password, create_jwt_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/login', methods=['POST'])
def login():
    """用户登录"""
    try:
        data = request.get_json()
        
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({'error': '用户名和密码不能为空'}), 400
        
        # 查找用户
        user = User.query.filter_by(username=data['username']).first()
        
        if not user or not verify_password(user.password_hash, data['password']):
            return jsonify({'error': '用户名或密码错误'}), 401
        
        # 生成token
        token = create_jwt_token(user.id)
        
        return jsonify({
            'message': '登录成功',
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }), 200
    except Exception as e:
        return jsonify({'error': '服务器内部错误'}), 500

@auth_bp.route('/api/register', methods=['POST'])
def register():
    """用户注册"""
    try:
        data = request.get_json()
        
        if not data or not data.get('username') or not data.get('password') or not data.get('email'):
            return jsonify({'error': '用户名、密码和邮箱不能为空'}), 400
        
        # 检查用户是否已存在
        if User.query.filter_by(username=data['username']).first():
            return jsonify({'error': '用户名已存在'}), 409
        
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': '邮箱已被注册'}), 409
        
        # 创建新用户
        new_user = User(
            username=data['username'],
            email=data['email'],
            password_hash=hash_password(data['password'])
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # 生成token
        token = create_jwt_token(new_user.id)
        
        return jsonify({
            'message': '注册成功',
            'token': token,
            'user': {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': '注册失败'}), 500

@auth_bp.route('/api/me', methods=['GET'])
@jwt_required()  # 这里需要 jwt_required
def get_current_user():
    """获取当前用户信息"""
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({'error': '用户不存在'}), 404
        
        return jsonify({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }), 200
    except Exception as e:
        return jsonify({'error': '获取用户信息失败'}), 500