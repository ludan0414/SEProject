from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Blog, User

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/api/blogs', methods=['GET'])
def get_blogs():
    """获取博客列表"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        # 构建查询
        query = Blog.query.filter_by(is_published=True)
        
        # 搜索功能
        search = request.args.get('search')
        if search:
            query = query.filter(Blog.title.contains(search) | Blog.content.contains(search))
        
        # 标签过滤
        tag = request.args.get('tag')
        if tag:
            query = query.filter(Blog.tags.contains(tag))
        
        # 排序和分页
        blogs = query.order_by(Blog.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'blogs': [{
                'id': blog.id,
                'title': blog.title,
                'summary': blog.summary or blog.content[:100] + '...',
                'author': blog.author.username,
                'tags': blog.tags.split(',') if blog.tags else [],
                'created_at': blog.created_at.isoformat(),
                'updated_at': blog.updated_at.isoformat()
            } for blog in blogs.items],
            'total': blogs.total,
            'pages': blogs.pages,
            'current_page': page
        }), 200
    except Exception as e:
        return jsonify({'error': '获取博客列表失败'}), 500

@blog_bp.route('/api/blogs/<blog_id>', methods=['GET'])
def get_blog(blog_id):
    """获取单篇博客"""
    try:
        blog = Blog.query.get(blog_id)
        
        if not blog or not blog.is_published:
            return jsonify({'error': '博客不存在或未发布'}), 404
        
        return jsonify({
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'summary': blog.summary,
            'tags': blog.tags.split(',') if blog.tags else [],
            'author': {
                'id': blog.author.id,
                'username': blog.author.username
            },
            'created_at': blog.created_at.isoformat(),
            'updated_at': blog.updated_at.isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': '获取博客失败'}), 500

@blog_bp.route('/api/blogs', methods=['POST'])
@jwt_required()
def create_blog():
    """创建博客"""
    try:
        data = request.get_json()
        current_user_id = get_jwt_identity()
        
        if not data or not data.get('title') or not data.get('content'):
            return jsonify({'error': '标题和内容不能为空'}), 400
        
        new_blog = Blog(
            title=data['title'],
            content=data['content'],
            summary=data.get('summary', ''),
            tags=','.join(data.get('tags', [])),
            author_id=current_user_id,
            is_published=data.get('is_published', True)
        )
        
        db.session.add(new_blog)
        db.session.commit()
        
        return jsonify({
            'message': '博客创建成功',
            'blog': {
                'id': new_blog.id,
                'title': new_blog.title,
                'summary': new_blog.summary
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': '创建博客失败'}), 500

@blog_bp.route('/api/blogs/<blog_id>', methods=['PUT'])
@jwt_required()
def update_blog(blog_id):
    """更新博客"""
    try:
        blog = Blog.query.get(blog_id)
        if not blog:
            return jsonify({'error': '博客不存在'}), 404
            
        current_user_id = get_jwt_identity()
        
        # 检查权限
        if blog.author_id != current_user_id:
            return jsonify({'error': '无权修改此博客'}), 403
        
        data = request.get_json()
        
        if 'title' in data:
            blog.title = data['title']
        if 'content' in data:
            blog.content = data['content']
        if 'summary' in data:
            blog.summary = data['summary']
        if 'tags' in data:
            blog.tags = ','.join(data['tags'])
        if 'is_published' in data:
            blog.is_published = data['is_published']
        
        db.session.commit()
        
        return jsonify({'message': '博客更新成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': '更新博客失败'}), 500

@blog_bp.route('/api/blogs/<blog_id>', methods=['DELETE'])
@jwt_required()
def delete_blog(blog_id):
    """删除博客"""
    try:
        blog = Blog.query.get(blog_id)
        if not blog:
            return jsonify({'error': '博客不存在'}), 404
            
        current_user_id = get_jwt_identity()
        
        # 检查权限
        if blog.author_id != current_user_id:
            return jsonify({'error': '无权删除此博客'}), 403
        
        db.session.delete(blog)
        db.session.commit()
        
        return jsonify({'message': '博客删除成功'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': '删除博客失败'}), 500