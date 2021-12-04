import requests
import time
from lxml import etree
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.firefox.options import Options as fireOptions
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.common.keys import Keys

def scrollToDown(driver,item):
	driver.execute_script("""
	(function () {
	var y = 0;
	var step = 30;·
	window.scroll(0, 0);
	function f() {
	if (y < document.body.scrollHeight) {
	y += step;
	window.scroll(0, y);
	setTimeout(f, 100);
	} else {
	window.scroll(0, 0);
	document.title += "scroll-done";
	}
	}
	setTimeout(f, 1000);
	})();
	""")
	while True:
		try:
			item.find_element_by_xpath('./div[2]/div/div/span').click()
		except Exception as e:
			pass
		else:
			break
		# if "scroll-done" in driver.title:
		# 	break
		# else:
		# 	print("还没有拉到最底端...")
		time.sleep(2)

def __driver(driver_path):
        if driver_path.split('/')[-1] == "chromedriver.exe" or driver_path.split('\\')[-1] == "chromedriver.exe":
            flag = 'Chrome'
            _options = chromeOptions()
        elif driver_path.split('/')[-1] == "geckodriver.exe" or driver_path.split('\\')[-1] == "geckodriver.exe":
            flag = 'Firefox'
            _options = fireOptions()
        # # _options.add_argument("--proxy-server=http://115.221.116.136:8888")
        # _options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        # # _options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
        # _options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        # _options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        # _options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # _options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        
        if flag == "Chrome":
            return Chrome(chrome_options=_options, executable_path=driver_path)
        elif flag == "Firefox":
            return Firefox(firefox_options=_options, executable_path=driver_path)


def get_info(start,end,data):
	url = 'http://www.shenzhenair.com/szair_B2C/flightsearch.action?hcType=DC&constId=&type=单程&orgCity={}&orgCityCode=TAO&dstCity={}&dstCityCode=CTU&orgDate={}&dstDate={}&quiz=Y&quiz=1'.format(start,end,data,data)
	url = 'https://www.qdairlines.com/book/flightSearch'

	driver = __driver('E:\\chromedriver.exe')
	# driver.set_page_load_timeout(10)

	res = driver.get(url)
	time.sleep(10)
	results = driver.find_elements_by_xpath('//*[@class="flightTr"]')
	print(results)
	for i in range(len(results)):
		try:
			a = results[i].find_element_by_xpath('./td[1]/div[1]/table/tbody/tr/td[1]/div').text
			b = results[i].find_element_by_xpath('./td[1]/div[1]/table/tbody/tr/td[2]/div').text
		except Exception as e:
			a = results[i].find_element_by_xpath('./td[1]/div[1]/text()').text
		else:
			pass
		finally:
			print(a)

def get_info2(start,end,data):
	url = 'https://www.qdairlines.com/book/flightSearch'

	driver = __driver('E:\\chromedriver.exe')
	driver.set_page_load_timeout(10)

	res = driver.get(url)
	driver.maximize_window()
	# time.sleep(10)
	driver.find_element_by_xpath('//*[@id="orig"]').send_keys(start)
	driver.find_element_by_xpath('//*[@id="dest"]').send_keys(end)
	driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/input').clear()
	driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/input').send_keys(data)
	driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div[2]/div/div[1]/div/div/div/input').send_keys(Keys.ENTER)
	driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div[2]/div[4]/div/button').click()
	time.sleep(2)
	try:
		driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[7]/div/div[2]/div[2]/div/button').click()
		# driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div/div/div[3]/div[2]/div[2]/div/div/span').click()
		# time.sleep(3)
		# driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div/div/div[3]/div[2]/div[2]/div/div').click()
	except Exception as e:
		pass
	time.sleep(2)
	# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

	time.sleep(2)
	results = driver.find_elements_by_xpath('//*[@class="airlines_cont"]')
	for item in results:
		a = item.find_element_by_xpath('./div[1]/div[1]/div[1]/span[1]').text
		b = item.find_element_by_xpath('./div[1]/div[1]/div[1]/span[2]').text
		c = item.find_element_by_xpath('./div[1]/div[1]/div[1]/span[3]').text
		title0 = a+b+c
		print('================',title0,'================')
		startTime = item.find_element_by_xpath('./div[1]/div[1]/div[2]/div[1]/strong').text
		startAdress = item.find_element_by_xpath('./div[1]/div[1]/div[2]/div[1]/div').text
		allTime = item.find_element_by_xpath('./div[1]/div[1]/div[2]/div[2]/div[2]').text
		endTime = item.find_element_by_xpath('./div[1]/div[1]/div[2]/div[3]/strong').text
		endAdress = item.find_element_by_xpath('./div[1]/div[1]/div[2]/div[3]/div').text
		print('始发：{}{}-----{}-----终点：{}{}'.format(startTime,startAdress,allTime,endTime,endAdress))
		prices = item.find_elements_by_xpath('./div[1]/div')
		price_list = []
		for item2 in prices[1:]:
			if len(item2.find_elements_by_xpath('./div/span')) == 2:
				price = item2.find_element_by_xpath('./div/span[2]').text + item2.find_element_by_xpath('./div/span[1]').text
			else:
				price = item2.find_element_by_xpath('./div/span').text
			price_list.append(price)
		print('经济舱：{}，超级经济舱：{}，头等舱：{},'.format(*price_list))
		# item.find_element_by_xpath('./div[2]/div/div/text()').click()
		scrollToDown(driver,item)
		tr_list = item.find_elements_by_xpath('./div[2]/table/tbody/tr')
		for tr in tr_list:
			a = tr.find_element_by_xpath('./td[1]/div/div[1]').text + tr.find_element_by_xpath('./td[1]/div/div[1]/span').text # 仓名称

			c = tr.find_element_by_xpath('./td[4]/div').text # 折扣

			d = tr.find_element_by_xpath('./td[5]/div/div/span[2]').text + tr.find_element_by_xpath('./td[5]/div/div/span[1]').text # 价格

			e = tr.find_element_by_xpath('./td[6]/div/span[2]').text # 余票

			print('{}--{}--{}--{}'.format(a,c,d,e))
		print('===='*15)


	# # 点击选择经济舱、超级经济舱、头等舱
	# results[0].find_element_by_xpath('./div[1]/div[3]/div/span[2]').click()
	time.sleep(2)




if __name__ == '__main__':
	get_info2('青岛','成都','2021-03-08')