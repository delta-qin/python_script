import os
import pandas as pd
from sqlalchemy import create_engine

allowed_category_ids = ["050000","050100","050101","050102","050103","050104","050105","050106","050107","050108","050109","050110","050111","050112","050113","050114","050115","050116","050117","050118","050119","050120","050121","050122","050123","050200","050201","050202","050203","050204","050205","050206","050207","050208","050209","050210","050211","050212","050213","050214","050215","050216","050217","050300","050301","050302","050303","050304","050305","050306","050307","050308","050309","050310","050311","050400","050500","050501","050502","050503","050504","050600","050700","050800","050900","060000","060100","060101","060102","060103","060200","060201","060202","060300","060301","060302","060303","060304","060305","060306","060307","060308","060400","060401","060402","060403","060404","060405","060406","060407","060408","060409","060411","060413","060414","060415","060500","060501","060502","060700","060701","060702","060703","060704","060705","060706","060800","060900","060901","060902","060903","060904","060905","060906","060907","061000","061001","061100","061101","061102","061103","061104","061200","061201","061202","061203","061204","061205","061206","061207","061208","061209","061210","061211","061212","061213","061214","061300","061301","061302","061400","061401","080000","080100","080101","080102","080103","080104","080105","080106","080107","080108","080109","080110","080111","080112","080113","080114","080115","080116","080117","080118","080119","080200","080201","080202","080300","080301","080302","080303","080304","080305","080306","080307","080308","080400","080401","080402","080500","080501","080502","080503","080504","080505","080600","080601","080602","080603","100000","100100","100101","100102","100103","100104","100105","100200","100201","110000","110100","110101","110102","110103","110104","110105","110106","110200","110201","110202","110203","110204","110205","110206","110207","110208","110209","110210","140000","140100","140101","140102","140200","140201","140300","140400","140500","140600","140700","140800","140900","141000","141201"]


column_names = ['id', 'name', 'type', 'address', 'location', 'typecode', 'pcode', 'pname', 'citycode', 'cityname', 'adcode', 'adname']

# GLFOX___POI = '/Users/deltaqin/PycharmProjects/pythonProject/glfox/2023_12POI'
GLFOX___POI = '/Users/deltaqin/PycharmProjects/pythonProject/glfox/test'

# 数据库连接配置
db_config = {
    'dialect': 'mysql',
    'driver': 'mysqlconnector',
    'username': 'root',
    'password': 'EYwNE9>#gNosdeltaqin',
    'host': 'localhost',
    'port': '3306',
    'database': 'xbfox_forum',
}

database_uri = 'mysql+pymysql://root:EYwNE9>#gNosdeltaqin@localhost:3306/xbfox_forum'

# engine = create_engine(database_uri)

# 创建数据库引擎
engine = create_engine(
    f"{db_config['dialect']}+{db_config['driver']}://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

# 遍历abc文件夹下的所有.xlsx文件
for filename in os.listdir(GLFOX___POI):
    print(filename)

    if filename.endswith('.csv'):
        filepath = os.path.join(GLFOX___POI, filename)

        # 读取xlsx文件中的所有工作表
        # excel_data = pd.read_excel(filepath, sheet_name=None, header=None,dtype={'typecode': str}, engine='openpyxl')
        # excel_data = pd.read_csv(filepath)

        # 读取CSV文件
        df = pd.read_csv(filepath)

        # 选择需要的列，并重命名
        df = df[['id', 'name', 'typecode']]
        df.columns = ['poi_id', 'title', 'poi_category_id']

        # 将数据写入MySQL
        df.to_sql('table_name', con=engine, index=False, if_exists='append')


        # for i, (sheet_name, data) in enumerate(excel_data.items()):
        #     # 检查列数，如果为13，则删除最后一列
        #     if len(data.columns) == 13:
        #         data = data.iloc[:, :-1]  # 删除最后一列
        #
        #
        #     # 对于第一个工作表，使用默认的标题行；对于其他工作表，手动指定列名
        #     data.columns = column_names
        #
        #     # 确保只保留允许分类ID的行
        #     filtered_data = data[data['typecode'].isin(allowed_category_ids)]
        #     # 如果过滤后的数据为空，则跳过此工作表
        #     if filtered_data.empty:
        #         continue
        #
        #     data = filtered_data[
        #         ['id', 'name', 'typecode', 'address', 'location', 'pcode', 'pname', 'citycode', 'cityname', 'adcode',
        #          'adname']]
        #
        #     # 重命名列名以匹配数据库字段
        #     data.rename(columns={'id': 'poi_id', 'name': 'title', 'typecode': 'poi_category_id'}, inplace=True)
        #
        #     # 将DataFrame写入数据库
        #     data.to_sql(name='gl_poi', con=engine, if_exists='append', index=False)

# 关闭数据库连接
engine.dispose()