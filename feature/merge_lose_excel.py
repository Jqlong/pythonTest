import pandas as pd

input_file_1 = 'rott_lose/final_lose_ture5.xls'
input_file_2 = 'iat_lose/packet_loss_5.xlsx'

df1 = pd.read_excel(input_file_1)
df2 = pd.read_excel(input_file_2)
merge_df = pd.concat([df1, df2], axis=1)
merge_df = merge_df.drop(['产生时间', '到达时间', '包处理类型：0入队，1误码，2拥塞', 'NUM_lose'], axis=1)
merge_df = merge_df.reindex(columns=[c for c in merge_df.columns if c != '丢包类别'] + ['丢包类别'])
merge_df.to_excel('result_rott_iat/rott_iat_lose_5.xls', index=None)



