from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time
from selenium.webdriver.common.action_chains import ActionChains
import sys
search_name="nirmal patel" #default name in case one forgot to enter name
try:
	serach_name=''.join(sys.argv[1:])
except:
	print("name required to search")

def page_unlike():
	browser.find_element_by_xpath('//*[@data-click="home_icon"]').click()	#Home button xpath and click.
	time.sleep(1)
	browser.find_element_by_xpath('//*[@title="Pages"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//*[@role="tablist"]/li[3]/a').click()
	time.sleep(2)
	pages=browser.find_elements_by_xpath('//*[@id="all_liked_pages"]/div/div')
	for page in pages:
		page.find_element_by_xpath('./div/div/div[2]/div/button').click()


temp=time.time()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser= webdriver.Chrome(options=chrome_options,executable_path=r"C:\Program Files\Python37\chromedriver")
browser.maximize_window()

browser.get("https://en-gb.facebook.com/login/")
# username
browser.find_element_by_xpath('//*[@id="email"]').send_keys('7016317545')
time.sleep(1)
# password
browser.find_element_by_xpath('//*[@id="pass"]').send_keys('nicpatel@963')
time.sleep(1)
# login click()
browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
time.sleep(1)
# type name to search
browser.find_element_by_xpath('//input[@name="q"]').send_keys(search_name)
# click search
browser.find_element_by_xpath('//button[@data-testid="facebar_search_button"]').click()
time.sleep(5)

main_div=browser.find_element_by_xpath('//div[@class="_6rbb"]')
print(main_div)
divs=main_div.find_elements_by_xpath('./div')
print(divs)
nirmal_profile=divs[0].find_element_by_xpath('./div/div/div/div/div/div/div/a').get_attribute('href')
time.sleep(1)
browser.get(nirmal_profile)
time.sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
timeline=browser.find_elements_by_xpath('//div[@class="rq0escxv l9j0dhe7 du4w35lb d2edcug0 gile2uim buofh1pr g5gj957u hpfvmrgz aov4n071 oi9244e8 bi6gxh9e h676nmdw"]/div')
timeline.pop(0)
browser.execute_script("window.scrollTo(0,0);")
print(len(timeline),type(timeline))

for post in timeline:
	try:
		if post.find_element_by_xpath('./div/div/div/div[2]/div/div[4]/div[1]/div/div/span[1]/div/div/div').get_attribute('aria-label')=='Like':
			action = ActionChains(browser)
			hover=post.find_element_by_xpath('./div/div/div/div[2]/div/div[4]/div[1]/div/div/span[1]/div/div/div')
			# //div[@aria-label="Reactions"]')
			action.move_to_element(hover).perform()
			time.sleep(0.7)
			hover.click()
			time.sleep(1)
		else:
			print('already liked')
	except:
		print("exception in like")
	
	

page_unlike()
print("time taken:",time.time()-temp)




