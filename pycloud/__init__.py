print("检查依赖中...")
def welcome():
	print("欢迎使用pycloud")
try:
	import os
	print("尝试导入request....")
	import requests
	print("依赖检查完成")
	welcome()
except:
	print("未找到request!")
	print("尝试下载，请稍后...")
	try:
		os.system("pip install requests")
		import requests
		print("下载成功！")
	except:
		print("下载失败，有可能是你的pip出错了...")
		print("或者说，请尝试下载pip")
	welcome()
from .main import Pycloud