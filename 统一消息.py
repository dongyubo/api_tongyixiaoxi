import requests
import random
data_list = []
for i in range(1):
	url = 'http://172.22.33.111:6061/auth/getToken'
	name = str(random.randint(1, 100))


	params = {
		'bizNo': 'prefix_'+name,
		'request': {
			'channelCode': '104LNJ4S',
			'channelSecret': 'MEPCQKPYF0XOI785'
		},
		'version': 1.0
	}
	response = requests.post(url, json=params)
	# if response.status_code != 200:
	# 	break


	data = response.json()
	# if 'errorMsg' in data:
	# 		break
	data_list.append(data)
	data_list.append(params)

	print('当前执行的请求数据：', params)
	# print('当前执行的返回数据：',i,data)
	print('\033[1;31;40m当前执行的返回数据：{},{}\033[0m'.format(i, data))
# # Create a Pandas dataframe from some data.
# df = pd.DataFrame(data_list)
# # Create a Pandas Excel writer using XlsxWriter as the engine.
# desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
# writer = pd.ExcelWriter(os.path.join(desktop_path, 'pandas_simple.xlsx'), engine='xlsxwriter')
# # Convert the dataframe to an XlsxWriter Excel object.
# df.to_excel(writer, sheet_name='Sheet1')
# # Close the Pandas Excel writer and output the Excel file.
# writer.save()



