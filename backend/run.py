import subprocess
import os
import socket
from app import create_app
from models import db, User, Blog  # 确保 Blog 在这里导入
from utils.auth import hash_password

# 创建应用实例
app = create_app()

# 检测端口，防止 debug 模式下前端重复启动
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def run_frontend():
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        return
    if is_port_in_use(3000):
        print("Frontend already running, skipping...")
        return
    frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')
    subprocess.Popen("yarn dev", cwd=frontend_dir, shell=True)

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
                content='''
这是一个示例博客文章，欢迎使用我们的实验室博客系统！该系统提供了完整的博客管理功能，包括文章的创建、编辑、发布和删除。

以下是一个 Markdown 示例文章：

# 欢迎使用 Cmd Markdown 编辑阅读器

------

我们理解您需要更便捷更高效的工具记录思想，整理笔记、知识，并将其中承载的价值传播给他人，**Cmd Markdown** 是我们给出的答案 —— 我们为记录思想和分享知识提供更专业的工具。 您可以使用 Cmd Markdown：

> * 整理知识，学习笔记
> * 发布日记，杂文，所见所想
> * 撰写发布技术文稿（代码支持）
> * 绘制发布各类图表（十九种图表支持）
> * 撰写发布学术论文（LaTeX 公式支持）
> * 利用 AI 辅助写作（可切换大模型）

![cmd-markdown-logo](https://www.zybuluo.com/static/img/logo.png)

除了您现在看到的这个 Cmd Markdown 在线版本，您还可以前往以下网址下载：

### [Windows/Mac/Linux 全平台客户端](https://www.zybuluo.com/cmd/)

> 请保留此份 Cmd Markdown 的欢迎稿兼使用说明，如需撰写新稿件，点击顶部工具栏右侧的 <i class="icon-file"></i> **新文稿** 或者使用快捷键 `Ctrl+Alt+N`。


```python
@requires_authorization
class SomeClass:
    pass

if __name__ == '__main__':
    # A comment
    print 'hello world'
```

行内公式：$1 + 2 = 3, \\sum_{i =1}^n i = \\dfrac{n(n+1)}{2}$

行间公式：$$1 + 2 = 3, \\sum_{i =1}^n i = \\dfrac{n(n+1)}{2}$$

''',
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
    run_frontend()

    # 启动应用
    print(f"服务器启动在: http://localhost:5000")
    print(f"API健康检查: http://localhost:5000/api/health")
    print(f"前端地址: http://localhost:3000")
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)