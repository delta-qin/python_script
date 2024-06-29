import os
import pandas as pd  # 确保只在这里导入pandas

GLFOX___POI = '/Users/deltaqin/PycharmProjects/pythonProject/glfox/2023_12POI'
# GLFOX___POI = '/Users/deltaqin/PycharmProjects/pythonProject/glfox/test'



# 遍历abc文件夹下的所有.xlsx文件
for filename in os.listdir(GLFOX___POI):
    print(filename)

    if filename.endswith('.xlsx'):
        filepath = os.path.join(GLFOX___POI, filename)

        # 读取xlsx文件中的所有工作表
        excel_data = pd.read_excel(filepath, sheet_name=None, header=None, dtype=str, engine='openpyxl')

        # 对于每个工作表，将其保存为一个.csv文件
        for sheet_name, data in excel_data.items():
            # 如果第一列 不是B开头的字符串，删除改行
            # if data.iloc[0, 0].startswith('B'):
            #     data = data.iloc[1:, :]
            #     print(data)

            # 只读取需要的列存在csv文件中


            csv_filename = f"{os.path.splitext(filename)[0]}_{sheet_name}.csv"
            csv_filepath = os.path.join(GLFOX___POI, csv_filename)
            # 只写入数据，不写入列名
            data.to_csv(csv_filepath, index=False, header=False)
            # data.to_csv(csv_filepath, index=False)