import subprocess
import re
import locale


def getWifiPassword(wifiName):
	with subprocess.Popen('netsh WLAN show profiles {} key=clear'.format(wifiName),
		shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE) as subp:
		try:
			out = subp.stdout.read().decode("gbk")
			# print(out)
		except Exception as e:
			cmd = 'netsh WLAN show profiles {} key=clear'.format(wifiName)
			cmd.encode(locale.getdefaultlocale()[1])
			try:
				with subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
					stderr=subprocess.PIPE) as subp1:
					out = subp1.stdout.read().decode("gb18030")
					# print(out)
			except Exception as e:
				return '解码出错'
	data = re.findall(r'关键内容.*: (.*)\r',out)
	return data[0] if data else None

def getWifiName():
	with subprocess.Popen('netsh WLAN show profiles',
		shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE) as subp:
		try:
			out = subp.stdout.read().decode("gbk")
		except Exception as e:
			# print(e)
			return []
	data = re.findall(r'所有用户配置文件 : (.*)\r',out)
	return data if data else []

if __name__ == '__main__':
	print('='*100)
	print('='*21+'WIFI名称'+'='*21+'|'+'='*21+'WIFI密码'+'='*21)
	for wifiName in getWifiName():
		password = getWifiPassword(wifiName)
		print(wifiName+' '*(50-len(wifiName)),password)
	print('='*101)
