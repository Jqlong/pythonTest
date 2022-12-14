"""为每个工作簿和工作表计算总数和均值"""
import pandas as pd
import glob
import os

input_path = ''
output_file = 'output/pandas7_output.xls'
all_workbooks = glob.glob(os.path.join(input_path, '*.xls*'))
data_frames = []
for workbook in all_workbooks:
    all_worksheets = pd.read_excel(workbook, sheet_name=None, index_col=None)
    workbook_total_sales = []
    workbook_number_of_sales = []
    worksheet_data_frames = []
    worksheets_data_frame = None
    workbook_data_frame = None
    for worksheet_name, data in all_worksheets.items():
        total_sales = pd.DataFrame(
            [float(str(value).strip('$').replace(',', '')) for value in data.loc[:, 'Sale Amount']]).sum()
        number_of_sales = len(data.loc[:, 'Sale Amount'])
        average_sales = pd.DataFrame(total_sales / number_of_sales)

        workbook_total_sales.append(total_sales)
        workbook_number_of_sales.append(number_of_sales)

        data = {'workbook': os.path.basename(workbook),
                'worksheet': worksheet_name,
                'worksheet_total': total_sales,
                'worksheet_average': average_sales}

        result_list = pd.DataFrame({'workbook': os.path.basename(workbook),
                                    'worksheet': worksheet_name,
                                    'worksheet_total': total_sales,
                                    'worksheet_average': average_sales})
        # worksheet_data_frames.append(
        # pd.DataFrame(data, columns=['workbook', 'worksheet', 'worksheet_total', 'worksheet_average']))
        worksheet_data_frames.append(result_list)
    worksheets_data_frame = pd.concat(worksheet_data_frames, axis=0, ignore_index=True)

    workbook_total = pd.DataFrame(workbook_total_sales).sum()
    workbook_total_number_of_sales = pd.DataFrame(workbook_number_of_sales).sum()
    workbook_average = pd.DataFrame(workbook_total / workbook_total_number_of_sales)

    workbook_stats = {'workbook': os.path.basename(workbook),
                      'workbook_total': workbook_total,
                      'workbook_average': workbook_average}

    workbook_stats = pd.DataFrame(workbook_stats, columns=['workbook', 'workbook_total', 'workbook_average'])
    workbook_data_frame = pd.merge(worksheets_data_frame, workbook_stats, on='workbook', how='left')
    data_frames.append(workbook_data_frame)

all_data_concatenated = pd.concat(data_frames, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='sums_and_averages', index=False)
writer.save()
