import pandas as pd

# 读取Excel文件
file_path = '2024-6-29.xlsx'  # 替换为你的Excel文件路径
df = pd.read_excel(file_path)

# 指定要处理的列名
column_name = '字段5'  # 替换为你的列名
column_name1 = '字段3'
column_name2 = '字段4'

# 去除tab符号和.符号
df[column_name] = df[column_name].str.replace(' ', '', regex=True)
df[column_name] = df[column_name].str.replace('	', '', regex=True)

df[column_name1] = df[column_name1].str.replace(' ', '', regex=True)
df[column_name1] = df[column_name1].str.replace('	', '', regex=True)

df[column_name2] = df[column_name2].str.replace(' ', '', regex=True)
df[column_name2] = df[column_name2].str.replace('	', '', regex=True)

# # 保存修改后的数据到新的Excel文件
output_file_path = '2024-6-29-new.xlsx'  # 替换为你想要保存的文件路径
df.to_excel(output_file_path, index=False)
#
# print("处理完成并保存到新的Excel文件。")



# 希望使用Python将下面的xlsx数据表导入MySQL数据库，表第一行是字段定义如下：
# poi_category_id fir_code sec_code thi_code
#
#
# 希望使用Python将abc文件夹下的所有csv数据表导入MySQL数据库，确保只有12列，如果数据有13列，删除最后一列
# idnametypeaddresslocationtypecodepcodepnamecitycodecitynameadcodeadname
#
# 将id填充到poi_category_id字段，name填充到title字段，typecode填充到poi_category_id字段，忽略type
#
# 下面是示例数据：
# B016600EPF,牛家川村,地名地址信息;普通地名;村庄级地名,兴县,"110.585847,38.299193",190108,140000,山西省,0358,吕梁市,141123,兴县,
# B0FFH5VTDB,汇源饭店,餐饮服务;中餐厅;中餐厅,林涛大道前湾路2号,"111.078737,39.021047",050100,140000,山西省,0350,忻州市,140931,保德县,


a = ''