import pandas as pd
import os
import glob
import csv

input_path = '../'
output_file = 'supplier_data_test_10.csv'
all_files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frame = []
for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).mean()



