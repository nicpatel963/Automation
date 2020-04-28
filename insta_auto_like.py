from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
def follow(browser):	
	print("follow")
	browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()	
	sug=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]')
	sug_list=sug.find_elements_by_xpath('./div[2]/div/div/div/div')
	print(sug_list)
	for i in range(len(sug_list)):
		bt_sug=sug_list[i].find_element_by_xpath('./div[3]/button')
		action = ActionChains(browser)
		action.click(bt_sug).perform()
		time.sleep(2)

def like():
	browser.execute_script("window.scrollTo(0,0);")
	temp=browser.find_elements_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[2]/div/article')
	print(temp)
	try:
		for i in range(10):
			print(i)
			# temp=browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[1]/div[1]/div/article')
			temp=browser.find_elements_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[2]/div/article')
			action = ActionChains(browser)
			post=temp[i].find_element_by_xpath('./div[2]/section[1]/span/button')
			temp=browser.find_elements_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[2]/div/article')
			time.sleep(1)
			if( post.find_element_by_xpath('./*').get_attribute('aria-label')=='Like'):
			        action.click(post).perform()
			else:
			        action.click(post).perform()
	except:
		print("error in 39")


def unfollow():

	browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a').click()	
	time.sleep(1)	
	profile=browser.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
	profile.click()
	time.sleep(5)
	browser.find_element_by_xpath('//ul/li[2]/a').click()
	time.sleep(2)
	li_followers=browser.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li')
	followers=[]
	for i in li_followers:
		followers.append(i.find_element_by_xpath('./div/div[2]/div/div/div/a').get_attribute('text'))
	print(followers)			
	# browser.find_element_by_xpath('//*[@class="WaOAr"]/button').click() #cancel button
	time.sleep(2)
	browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
	time.sleep(2)
	browser.find_element_by_xpath('//ul/li[3]/a').click()
	time.sleep(2)
	li_following=browser.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li')
	time.sleep(2)
	following=[]
	
	for i in li_following:
		following.append(i.find_element_by_xpath('./div/div[2]/div/div/div/a').get_attribute('text'))
	
	print(following)
	
	for li in li_following:
		if li.find_element_by_xpath('./div/div[2]/div/div/div/a').get_attribute('text') not in followers:
			print(li.find_element_by_xpath('./div/div[2]/div/div/div/a').get_attribute('text'))
			li.find_element_by_xpath('./div/div[3]/button').click()
			time.sleep(1)
			browser.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button[1]').click()
			time.sleep(1)
			# li.find_element_by_xpath('./div/div[3]/button').click()
			time.sleep(1)


temp=time.time()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser= webdriver.Chrome(options=chrome_options,executable_path=r"C:\Program Files\Python37\chromedriver")
browser.maximize_window()
action = ActionChains(browser)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
browser.find_element_by_xpath('//*[@name="username"]').send_keys('nic_temp')
browser.find_element_by_xpath('//*[@name="password"]').send_keys('nicpatel@963')
time.sleep(1)
try:
	browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
except:
	print(browser.find_element_by_xpath('//*[@type=submit]'),"line 93")

time.sleep(4)

# browser.execute_script("window.scrollTo(0, 	7000);")
# time.sleep(2)
# temp=browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article')

# time.sleep(1)

like()
follow(browser)
unfollow()