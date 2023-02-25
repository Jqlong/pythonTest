import pandas as pd
file1 = 'result_rott_iat/rott_iat_lose_1.xls'
file2 = 'result_rott_iat/rott_iat_lose_2.xls'
file3 = 'result_rott_iat/rott_iat_lose_3.xls'
file4 = 'result_rott_iat/rott_iat_lose_4.xls'
file5 = 'result_rott_iat/rott_iat_lose_5.xls'

df1 = pd.read_excel(file1)
df2 = pd.read_excel(file2)
df3 = pd.read_excel(file3)
df4 = pd.read_excel(file4)
df5 = pd.read_excel(file5)
data_frame = pd.concat([df1, df2, df3, df4, df5], axis=0, ignore_index=True)
data_frame.to_excel('result_rott_iat/all_lose.xls', index=False)


