# 对数据进行排序编号

import pandas as pd
import openpyxl
from itertools import chain


def sort_date():
    """获取数据"""

    # 读取相对位置的xcel,使用openpyxl引擎，
    df = pd.read_excel("alter_test.xlsx",header=None, sheet_name="Sheet1")

    # 空列表
    res = []
    for row in df.index:
        rowDate = df.loc[row].values[:]
        rowDate = rowDate.tolist()
        res.append(rowDate)
    # print(res)
    res = list(chain.from_iterable(res))
    # print(res)
    res.sort()
    print(len(res))
    # print(res)
    return res
    # print(res)
    # one_cell = df.iat[0, 0]  # A2单元格
    # print(one_cell)

    # row_data0 = df.loc[[0]].values
    # for cel0 in row_data0:
    #     if cel0.all() == "'位置信息'":
    #         continue
    #     print(cel0)

    # col_date = df.iloc[:, 0]  # 读取第一列
    # for col in col_date:
    #     print(col)
    # print(df)


sort_date()
