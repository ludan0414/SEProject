from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import config
from models import db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # 初始化扩展
    db.init_app(app)
    jwt = JWTManager(app)
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # 注册蓝图
    from routes.auth import auth_bp
    from routes.blog import blog_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)
    
    # JWT 配置
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({'error': 'token已过期'}), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({'error': '无效的token'}), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({'error': '缺少访问令牌'}), 401
    
    # 错误处理
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': '资源未找到'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': '服务器内部错误'}), 500
    
    # 健康检查端点
    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'healthy', 'message': 'PKU Lab Blog API is running'})
    
    return app