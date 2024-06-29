import pandas as pd
import mysql.connector
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 读取csv文件
data = pd.read_csv('/Users/deltaqin/PycharmProjects/pythonProject/glfox/2023_6_poi_rate.csv')

db_user = 'root'
db_password = 'EYwNE9>#gNosdeltaqin'
db_host = 'localhost'  # 或者是你的数据库服务器地址
db_name = 'xbfox_forum'
# db_host='101.35.43.238'

# 创建数据库连接
mydb = mysql.connector.connect(
  host=db_host,
  user=db_user,
  password=db_password,
  database=db_name
)

# 创建一个新的DataFrame来保存不存在的记录
not_found_data = pd.DataFrame(columns=data.columns)

# 创建游标
mycursor = mydb.cursor(buffered=True)

# 遍历csv文件中的每一行
for index, row in data.iterrows():
    title = row['景点名称']
    city = row['景点城市']
    city_rank = row['点评数量排名_当前城市']
    national_rank = row['点评数量排名_全国']

    # 构建查询语句
    select_sql = f'SELECT * FROM gl_poi WHERE title = "{title}" and cityname like "{city}%"'
    try:
        # 执行查询
        mycursor.execute(select_sql)

        # 获取查询结果
        result = mycursor.fetchone()
        if result:
            # 如果查询结果存在，获取ID
            id = result[0]  # assuming the id is the first column

            # 构建更新语句
            update_sql = f'UPDATE gl_poi SET city_rank = {city_rank}, national_rank = {national_rank} WHERE id = {id}'

            # 执行更新
            mycursor.execute(update_sql)

            # 提交修改
            mydb.commit()

            logging.info(f'Successfully updated {title} in {city}.')
        else:
            not_found_data = pd.concat([not_found_data, pd.DataFrame([row])], ignore_index=True)

            logging.warning(f'No result found for {title} in {city}. Saving to not_found_data.')
    except mysql.connector.Error as err:
        logging.error(f"Something went wrong: {err}")
        continue

# 关闭数据库连接
mydb.close()

not_found_data.to_csv('not_found_data.csv', index=False)
