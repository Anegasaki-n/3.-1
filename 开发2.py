from selennium import webdriver
import time
import base64

driver = webdriver.Chrome()
driver.get('https://www.163.com/')

x = driver.get_screenshot_as_base64()
image = base64.b64decode(x)


while True:
	file = open('{}.jpg'.format(time.time()),'wb')
	file.write(image)
	time.sleep(300)
