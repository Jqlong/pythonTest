import pandas as pd
input_file = '../数据包丢失原因区分仿真.xls'
data_frame = pd.read_excel(input_file)
data_frame['ROTT'] = data_frame[data_frame.columns[1]] - data_frame[data_frame.columns[0]]
important_col = [1, 2]
# 将rott写入文件中
# 如果不等于零
# 现在判断不为零的行
data_frame_isin = data_frame[data_frame['包处理类型：0入队，1误码，2拥塞'].isin(important_col)]
print(data_frame_isin)
data_frame.loc[0, 'ROTT_min'] = data_frame[data_frame.columns[3]].min()
data_frame.loc[0, 'ROTT_max'] = data_frame[data_frame.columns[3]].max()
# ROTT_min = data_frame[data_frame.columns[3]].min()
data_frame.to_excel('result.xls', index=False)



