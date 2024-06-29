import pandas as pd
import json
import mysql.connector
import ast
import uuid
from OpenAI import second_category

def insert_app_tags():
    # 连接数据库
    db = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )

    cursor = db.cursor()

    # 读取Excel文件
    df = pd.read_excel("./2024-04-08-logocom-app-tags.xlsx", engine='openpyxl')
    # 遍历每一行数据
    for index, row in df.iterrows():
        app_id = row[0]
        tags = ast.literal_eval(row[2])  # 将字符串转换为Python列表
        # 解析tags，使用 , 拼接里面的字符串
        # tags = json.dumps(tags, ensure_ascii=False)
        tags = ", ".join(tags)
        print(tags)
        # 创建SQL语句
        sql = "UPDATE xb_application SET tags = %s WHERE application_id = %s"

        # 执行SQL语句
        cursor.execute(sql, (tags, app_id))
    # 提交到数据库执行
    db.commit()

    # 关闭数据库连接
    db.close()

def insert_tags():
    # 连接数据库
    db = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )

    cursor = db.cursor()

    # 读取Excel文件
    df = pd.read_excel("./2024-04-08-logocom-app-tags.xlsx", engine='openpyxl')
    # 遍历每一行数据
    for index, row in df.iterrows():
        tags = ast.literal_eval(row.iloc[2])  # 将字符串转换为Python列表
        # 遍历tags列表中的每个文本元素
        for tag_text in tags:
            # 检查文本是否已经存在于数据库中
            sql_check = "SELECT * FROM xb_tag WHERE name = %s"
            cursor.execute(sql_check, (tag_text,))
            existing_tag = cursor.fetchone()

            # 如果文本不存在，则插入到数据库中
            if not existing_tag:
                # 生成唯一的UUID并去除连字符
                tag_id = str(uuid.uuid4()).replace('-', '')

                # 插入到数据库中
                sql_insert = "INSERT INTO xb_tag (name, tag_id) VALUES (%s, %s)"
                cursor.execute(sql_insert, (tag_text, tag_id))
    # 提交到数据库执行
    db.commit()

    # 关闭数据库连接
    db.close()

def insert_category():
    # 连接数据库
    db = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )

    cursor = db.cursor()

    # 读取Excel文件
    df = pd.read_excel("./2024-04-08-logocom-app-tags.xlsx", engine='openpyxl')
    # 遍历每一行数据
    for index, row in df.iterrows():
        tags = ast.literal_eval(row.iloc[2])  # 将字符串转换为Python列表
        # 遍历tags列表中的每个文本元素
        for tag_text in tags:
            # 检查文本是否已经存在于数据库中
            sql_check = "SELECT * FROM xb_tag WHERE name = %s"
            cursor.execute(sql_check, (tag_text,))
            existing_tag = cursor.fetchone()

            # 如果文本不存在，则插入到数据库中
            if not existing_tag:
                # 生成唯一的UUID并去除连字符
                tag_id = str(uuid.uuid4()).replace('-', '')

                # 插入到数据库中
                sql_insert = "INSERT INTO xb_tag (name, tag_id) VALUES (%s, %s)"
                cursor.execute(sql_insert, (tag_text, tag_id))

    # 遍历每一行数据
    for index, row in df.iterrows():
        app_id = row[0]
        categories = row[3].split(',')  # 获取分类列表
        # 查询已存在的分类，如果不存在则插入到xb_category表
        for category in categories:
            # 查询分类是否已存在
            sql_check = "SELECT category_code, name FROM xb_category WHERE name = %s and type = 3"
            cursor.execute(sql_check, (category,))
            existing_category = cursor.fetchone()

            if not existing_category:
                # 生成分类ID
                category_id = str(uuid.uuid4()).replace('-', '')

                # 插入分类到xb_category表
                sql_insert_category = "INSERT INTO xb_category (category_code, name, level, type) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_insert_category, (category_id, category, 1, 3))
                db.commit()

            else:
                category_id = existing_category[0]

            # 插入应用与分类的关联关系到xb_application_category表
            sql_insert_app_category = "update xb_application set category_ids = %s where application_id = %s"
            cursor.execute(sql_insert_app_category, ( "[\""+ category_id + "\"]", app_id))
            db.commit()


    # 提交到数据库执行
    db.commit()

    # 关闭数据库连接
    db.close()

import os

def insert_img():
    # 连接数据库
    db = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )

    cursor = db.cursor()

    # 图片文件夹路径
    image_folder = "/Users/deltaqin/PycharmProjects/pythonProject/img"

    # 遍历图片文件夹
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # 只处理图片文件
            application_id = os.path.splitext(filename)[0]  # 使用文件名作为application_id
            thumbnails_value = filename  # 更新thumbnails字段值为文件名以及其后缀

            # 更新xb_application表
            sql_update = "UPDATE xb_application SET thumbnails = %s WHERE application_id = %s"
            cursor.execute(sql_update, (thumbnails_value, application_id))
            db.commit()

    # 关闭数据库连接
    db.close()

def insert_category_tag():
    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )

    def get_tag_id(tag):
        with conn.cursor() as cursor:
            sql = "SELECT tag_id FROM xb_tag WHERE name = %s"
            cursor.execute(sql, (tag,))
            result = cursor.fetchone()
            return result[0] if result else None

    def check_category_tag_exists(category_id, tag_id):
        with conn.cursor() as cursor:
            sql = "SELECT * FROM xb_category_tag WHERE category_code = %s AND tag_id = %s"
            cursor.execute(sql, (category_id, tag_id))
            return cursor.fetchone() is not None

    def insert_category_tag(category_id, tag_id, tag_name):
        with conn.cursor() as cursor:
            print("insert into xb_category_tag (category_code, tag_id, tag_name) values (%s, %s, %s)", (category_id, tag_id, tag_name))
            sql = "INSERT INTO xb_category_tag (category_code, tag_id, tag_name) VALUES (%s, %s, %s)"
            cursor.execute(sql, (category_id, tag_id, tag_name))
            conn.commit()

    def process_apps(apps):
        for app in apps:
            category_id = app['creator_ids'][0]  # 假设分类ID就是creator_ids列表的第一项
            tags = app['tags'].split(', ')
            for tag in tags:
                tag_id = get_tag_id(tag)
                if tag_id is not None and not check_category_tag_exists(category_id, tag_id):
                    insert_category_tag(category_id, tag_id, tag)

    def get_all_apps():
        with conn.cursor() as cursor:
            sql = "SELECT application_id, category_ids, tags FROM xb_application"
            cursor.execute(sql)
            results = cursor.fetchall()
            apps = []
            for result in results:
               if result[2] and result[1]:
                   category_ids = json.loads(result[1])
                   tags = result[2]
                   apps.append({'creator_ids': category_ids, 'tags': tags})
            return apps

    # 假设你已经有了一个从数据库中获取所有应用的函数
    apps = get_all_apps()
    process_apps(apps)

def update_category_tag_count():
    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )
    with conn.cursor() as cursor:
        sql = "SELECT category_code, tag_id, tag_name FROM xb_category_tag"
        cursor.execute(sql)
        results = cursor.fetchall()

        for line in results:
            category_code = line[0]
            tag_id = line[1]
            tag_name = line[2]
            print(category_code, tag_id)
            print("SELECT count(*) FROM xb_application where category_ids like %s  and tags like %s", ("%" + category_code + "%", "%" + tag_name + "%"))
            sql = "SELECT count(*) FROM xb_application where category_ids like %s  and tags like %s"
            cursor.execute(sql, ("%" + category_code + "%", "%" + tag_name + "%"))
            count = cursor.fetchone()[0]
            sql_update = "UPDATE xb_category_tag SET app_count = %s WHERE category_code = %s AND tag_id = %s"
            cursor.execute(sql_update, (count, category_code, tag_id))

    conn.commit()
    # 关闭数据库连接
    conn.close()
# insert_tags()

def insert_app_tag():
    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )
    with conn.cursor() as cursor:
        sql = "SELECT application_id, tags FROM xb_application"
        cursor.execute(sql)
        results = cursor.fetchall()

        for line in results:
            app_id = line[0]
            tags = line[1]
            if tags:
                tags = tags.split(', ')
                tag_ids = "[\""
                for tag in tags:
                    tag_sql = "SELECT tag_id FROM xb_tag WHERE name = %s"
                    cursor.execute(tag_sql, (tag,))
                    tag_id = cursor.fetchone()
                    if tag_id:
                        tag_id = tag_id[0]
                        tag_ids += tag_id + "\", \""
                tag_ids = tag_ids[:-3]
                tag_ids += "]"
                print(tag_ids)
                update_app_sql = "UPDATE xb_application SET tag_ids = %s WHERE application_id = %s"
                cursor.execute(update_app_sql, (tag_ids, app_id))

    conn.commit()
    conn.close()

def insert_second_category():
    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )
    with conn.cursor() as cursor:
        # 定义一级分类和对应的二级分类
        categories = {
            "效率办公": [
                "文档处理",
                "项目管理",
                "会议工具",
                "时间管理",
                "数据管理",
                "办公协作",
                "运营与产品",
                "销售与市场",
                "编程与技术",
                "自动化工具"
            ],
            "实用工具": [
                "系统工具",
                "浏览器插件",
                "安全工具",
                "工具集合"
            ],
            "图片、音视频处理": [
                "视频处理",
                "音频处理",
                "图像处理",
                "录屏工具",
                "素材管理",
                "摄影工具",
                "相册管理"
            ],
            "娱乐消遣": [
                "看",
                "听",
                "玩",
                "社交",
            ],
            "图书阅读": [
                "电子书与在线阅读",
                "写作工具",
                "阅读辅助",
            ],
            "学习教育": [
                "在线学习",
                "知识管理",
                "学术研究",
                "语言学习",
                "编程学习"
            ],
            "金融理财": [
                "投资工具",
                "财务软件",
                "银行服务",
                "保险服务"
            ],
            "新闻资讯": [
                "新闻阅读",
                "行业资讯",
                "媒体工具"
            ],
            "时尚购物": [
                "购物平台",
                "时尚设计",
                "品牌营销"
            ],
            "医疗健康": [
                "健康管理",
                "医疗工具",
                "健身运动"
            ],
            "旅行交通": [
                "旅行规划",
                "导航工具",
                "交通服务"
            ],
            "居家生活": [
                "家居设计",
                "生活助手",
                "厨艺烹饪"
            ]
        }
        for first_category in categories:
            # 查询一级分类对应的ID
            cursor.execute("SELECT category_code FROM xb_category WHERE name=%s", (first_category,))
            first_category_id = cursor.fetchone()[0]

            # 遍历二级分类
            for second_category in categories[first_category]:
                # 插入二级分类， par_category_code 指定为一级分类
                sql = "INSERT INTO xb_category (category_code, name, level, type, par_category_code) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (str(uuid.uuid4()).replace('-', ''), second_category, 2, 3, first_category_id))

                # 提交事务
                conn.commit()

def insert_app_second_category():
    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="EYwNE9>#gNosdeltaqin",  # 数据库密码
        database="xbfox_forum"  # 数据库名
    )
    with conn.cursor() as cursor:
        # 定义一级分类和对应的二级分类
        categories = {
            "效率办公": [
                "文档处理",
                "项目管理",
                "会议工具",
                "时间管理",
                "数据管理",
                "办公协作",
                "运营与产品",
                "销售与市场",
                "编程与技术",
                "自动化工具",
                "设计与创意"
            ],
            "实用工具": [
                "系统工具",
                "浏览器插件",
                "安全工具",
                "工具集合"
            ],
            "图片、音视频处理": [
                "视频处理",
                "音频处理",
                "图像处理",
                "录屏工具",
                "素材管理",
                "摄影工具",
                "相册管理"
            ],
            "娱乐消遣": [
                "看",
                "听",
                "玩",
                "社交",
            ],
            "图书阅读": [
                "电子书与在线阅读",
                "写作工具",
                "阅读辅助",
            ],
            "学习教育": [
                "在线学习",
                "知识管理",
                "学术研究",
                "语言学习",
                "编程学习"
            ],
            "金融理财": [
                "投资工具",
                "财务软件",
                "银行服务",
                "保险服务"
            ],
            "新闻资讯": [
                "新闻阅读",
                "行业资讯",
                "媒体工具"
            ],
            "时尚购物": [
                "购物平台",
                "时尚设计",
                "品牌营销"
            ],
            "医疗健康": [
                "健康管理",
                "医疗工具",
                "健身运动"
            ],
            "旅行交通": [
                "旅行规划",
                "导航工具",
                "交通服务"
            ],
            "居家生活": [
                "家居设计",
                "生活助手",
                "厨艺烹饪"
            ]
        }

        # 查询所有的分类信息
        sql = "select category_code, name from  xb_category where type =3 and level = 1 "
        cursor.execute(sql)
        category_res = cursor.fetchall()
        categoryIdNameMap = {}
        for line in category_res:
            categoryIdNameMap[line[0]] = line[1]

        sql = "SELECT application_id, tags, faq, category_ids FROM xb_application"
        cursor.execute(sql)
        results = cursor.fetchall()

        for line in results[1:]:
            app_id = line[0]
            tags = line[1]
            description = line[2]
            category_ids = line[3]
            # 如果 category_ids 包含大于 1 个分类，说明已经更新过了
            if category_ids.count(",") > 0:
                continue
            #  ["01hcaf9sn7a54z04jq332g92n5"]
            category_id = category_ids[2:-2]
            firstCategory = categoryIdNameMap[category_id]
            # 使用一级分类查询对应的二级分类
            secondCategorys = categories[firstCategory]
            # AI 查询当前应用应该属于哪一个二级分类，
            # 1. 使用 tags 和 description 作为输入
            # 删除标签中的特殊字符
            description = description.replace(" ", "")
            description = description.replace("\n", "")
            content = description
            # 2. 使用分类模型进行预测
            try:
                second_category_res = second_category(secondCategorys, content)
                # 如果 second_category_res 有 引号删除
                second_category_res = second_category_res.replace("\"", "")
                # 查询对应的二级分类的 ID
                sql111 = "select category_code from xb_category where name = %s and type = 3"
                cursor.execute(sql111, (second_category_res,))
                second_category_id = cursor.fetchone()[0]
                # 更新应用的二级分类的 ID
                category_ids = "[\""+ category_id + "\", \"" + second_category_id + "\"]"
                print(category_ids)
                sql = "UPDATE xb_application SET category_ids = %s WHERE application_id = %s"
                cursor.execute(sql, (category_ids, app_id))
            except Exception as e:
                print(e)
                print("Error info" +  app_id + second_category_res)
            conn.commit()

    # 关闭数据库连接
    conn.close()


insert_app_second_category()

