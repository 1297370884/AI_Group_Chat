import os
from pathlib import Path
from robyn.templating import JinjaTemplate
from robyn import Robyn, ALLOW_CORS

"""
配置环境
"""
# 获取当前文件路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# def serve_static_files(app):
#     """配置静态资源在哪个目录"""
#     app.serve_directory(
#         route="/static",  # 访问路由前缀
#         directory_path=os.path.join(BASE_DIR, "static"),  # 静态文件目录的绝对路径
#         index_file=None  # 不需要指定索引文件
#     )

# # 创建模板实例
# template = JinjaTemplate(directory=os.path.join(BASE_DIR, "templates"))

# def render_template(template_name, **kwargs):
#     """全局配置render_template"""
#     return template.render_template(template_name, **kwargs)

def configure_cors(app: Robyn):
    """配置CORS"""
    ALLOW_CORS(app, origins=[
        "*"
    ])

# 数据库配置
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'aidata',
    'charset': 'utf8mb4'
}

