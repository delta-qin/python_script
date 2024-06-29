import pandas as pd
import mysql.connector

# 读取xlsx文件
df = pd.read_excel('/Users/deltaqin/PycharmProjects/pythonProject/glfox/poi_category.xlsx')  # 请将'your_file.xlsx'替换为你的文件路径

# 连接到MySQL数据库
# cnx = mysql.connector.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     password="EYwNE9>#gNosdeltaqin",  # 数据库密码
#     database="xbfox_forum"  # 数据库名
# )

cnx = mysql.connector.connect(
    host="101.35.43.238",  # 数据库主机地址
    user="root",  # 数据库用户名
    password="EYwNE9>#gNosdeltaqin",  # 数据库密码
    database="xbfox_forum"  # 数据库名
)

# 创建游标
cursor = cnx.cursor()

# 假设你的表名为'your_table'
table_name = 'gl_poi_category'

# 插入数据的SQL语句
sql = f"INSERT INTO {table_name} (poi_category_id, fir_code, sec_code, thi_code) VALUES (%s, %s, %s, %s)"

# 遍历DataFrame的每一行，插入数据
for index, row in df.iterrows():
    cursor.execute(sql, (row['poi_category_id'], row['fir_code'], row['sec_code'], row['thi_code']))

# 确认更改
cnx.commit()

# 关闭游标和连接
cursor.close()
cnx.close()