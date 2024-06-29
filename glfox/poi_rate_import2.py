import pandas as pd
import mysql.connector
import uuid

# 读取csv文件
data = pd.read_csv('/Users/deltaqin/PycharmProjects/pythonProject/glfox/2023_6_poi_rate.csv')

# 创建数据库连接
db_user = 'root'
db_password = 'EYwNE9>#gNosdeltaqin'
# db_host = 'localhost'  # 或者是你的数据库服务器地址
db_name = 'xbfox_forum'
db_host='101.35.43.238'

# 创建数据库连接
mydb = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)

# 创建游标
mycursor = mydb.cursor()

# 遍历csv文件中的每一行
for index, row in data.iterrows():
    title = row['景点名称']
    longitude = row['景点经度']
    latitude = row['景点纬度']
    location = f"{longitude},{latitude}"
    city = row['景点城市']
    city_rank = row['点评数量排名_当前城市']
    national_rank = row['点评数量排名_全国']

    # 构建插入语句
    insert_sql = f"""
    INSERT INTO gl_hot_poi (title, location, cityname, city_rank, national_rank, hot_poi_id) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    val = (title, location, city, city_rank, national_rank, str(uuid.uuid4()).replace('-', ''))

    # 执行插入
    mycursor.execute(insert_sql, val)

    # 提交修改
    mydb.commit()

print(f"{mycursor.rowcount} records inserted.")

# 关闭数据库连接
mydb.close()
