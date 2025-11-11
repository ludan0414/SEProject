import os
from app import create_app
from models import db, User, Blog  # 确保 Blog 在这里导入
from utils.auth import hash_password

# 创建应用实例
app = create_app()

def init_database():
    """初始化数据库和示例数据"""
    with app.app_context():
        # 创建所有表
        db.create_all()
        print("数据库表创建成功！")
        
        # 添加初始管理员用户
        admin_user = None
        if not User.query.filter_by(username='admin').first():
            admin_user = User(
                username='admin',
                email='admin@pku.edu.cn',
                password_hash=hash_password('admin123')
            )
            db.session.add(admin_user)
            db.session.commit()
            print("初始管理员用户已创建: 用户名: admin, 密码: admin123")
        else:
            admin_user = User.query.filter_by(username='admin').first()
            print("管理员用户已存在")
        
        # 添加示例博客
        if not Blog.query.first() and admin_user:
            sample_blog = Blog(
                title='欢迎使用 PKU Lab Blog',
                content='这是一个示例博客文章，欢迎使用我们的实验室博客系统！该系统提供了完整的博客管理功能，包括文章的创建、编辑、发布和删除。',
                summary='欢迎使用PKU实验室博客系统',
                tags='欢迎,示例,介绍',
                author_id=admin_user.id,
                is_published=True
            )
            db.session.add(sample_blog)
            
            # 添加第二个示例博客
            sample_blog2 = Blog(
                title='实验室资源介绍',
                content='在这里你可以分享实验室的研究成果、技术文档、项目经验等。系统支持标签分类、搜索功能，方便知识的管理和查找。',
                summary='实验室资源管理系统介绍',
                tags='资源,管理,文档',
                author_id=admin_user.id,
                is_published=True
            )
            db.session.add(sample_blog2)
            db.session.commit()
            print("示例博客已创建！")
        else:
            print("博客已存在，跳过创建")

if __name__ == '__main__':
    # 初始化数据库
    init_database()
    
    # 启动应用
    print(f"服务器启动在: http://localhost:5000")
    print(f"API健康检查: http://localhost:5000/api/health")
    print(f"前端地址: http://localhost:3000")
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5001)