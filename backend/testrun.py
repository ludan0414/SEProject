# import requests
# import sys

# BASE = "http://localhost:5001"

# def register(username, password, email):
#     return requests.post(f"{BASE}/api/register", json={
#         "username": username, "password": password, "email": email
#     })

# def login(username, password):
#     return requests.post(f"{BASE}/api/login", json={
#         "username": username, "password": password
#     })

# def me(token):
#     return requests.get(f"{BASE}/api/me", headers={
#         "Authorization": f"Bearer {token}"
#     })

# def main():
#     username = "user1"
#     password = "pass"
#     email = "u@example.com"

#     r = register(username, password, email)
#     print("register:", r.status_code, r.text)

#     if r.status_code == 201:
#         token = r.json().get("token")
#     else:
#         # 若已存在或注册失败，尝试登录
#         r2 = login(username, password)
#         print("login:", r2.status_code, r2.text)
#         if r2.status_code != 200:
#             sys.exit(1)
#         token = r2.json().get("token")

#     print("token:", token)
#     r3 = me(token)
#     print("me:", r3.status_code, r3.text)

# if __name__ == "__main__":
#     main()
import requests
from app import create_app
from models import db, Blog

app = create_app()

def get_first_blog_id():
    with app.app_context():
        blog = Blog.query.filter_by(is_published=True).first()
        return blog.id if blog else None

if __name__ == "__main__":
    blog_id = get_first_blog_id()
    if not blog_id:
        print("未在数据库中找到已发布的博客。请先运行 run.py 初始化数据库或创建博客。")
    else:
        url = f"http://localhost:5001/blog/{blog_id}"
        try:
            r = requests.post(url)
            print(r.status_code)
            print(r.json())
        except Exception as err:
            print("请求失败：", err)