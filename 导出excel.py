import pandas as pd

# 创建数据框，每一行是一个列表
df = pd.DataFrame([[13103838059, 2882171681, "wxa59d704e7d4107ec", "wxa59d704e7d4107ec"]])

# 设置列标题
df.columns = ["电话号码", "App设备ID", "微信小程序OpenId", "微信公众号OpenId"]

# 重复数据
df = pd.concat([df] * 100000, ignore_index=True)

# 导出为excel
df.to_excel("fixed_values_100000_rows.xlsx", index=False)
