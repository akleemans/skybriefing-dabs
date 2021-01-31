import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

USER = 'my_login'
PW = 'my_password'
COUNTRY = 'Switzerland'
FLUGPLATZ = 'LSZB'
LOWER_FL = '000'
UPPER_FL = '080'

print('Starting. Setting up Firefox...')
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', "~/temp/")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/pdf'))
profile.set_preference('pdfjs.disabled', True)
driver = webdriver.Firefox(profile)

print('Opening website...')
driver.get("https://www.skybriefing.com")
time.sleep(10)

print('Downloading first PDF...')
element = driver.find_elements_by_css_selector('div[location="pdfLinkToday"] a')[0]
element.click()
time.sleep(10)

print('Logging in...')
driver.get("https://www.skybriefing.com/de/signinnativ")
time.sleep(40)
print('Entering username...')
element = driver.find_elements_by_xpath('//*[@id="_com_liferay_login_web_portlet_LoginPortlet_login"]')[0]
element.send_keys(USER)
time.sleep(5)
print('Entering password...')
element = driver.find_elements_by_xpath('//*[@id="_com_liferay_login_web_portlet_LoginPortlet_password"]')[0]
element.send_keys(PW)
time.sleep(5)
element.send_keys(Keys.ENTER)
time.sleep(5)
print('Open Area Briefing...')
driver.get('https://www.skybriefing.com/de/new-area-briefing')
time.sleep(30)

# Information Area
element = Select(driver.find_elements_by_css_selector('div.v-select:nth-child(1) > select:nth-child(1)')[0])
element.select_by_visible_text(COUNTRY)
time.sleep(2)

# Flugplatz
element = driver.find_elements_by_css_selector('input.v-widget:nth-child(1)')[0]
element.send_keys(FLUGPLATZ)
time.sleep(2)

# lower FL
element = driver.find_elements_by_css_selector('#gwt-uid-6')[0]
element.send_keys(LOWER_FL)
time.sleep(2)

# upper FL
element = driver.find_elements_by_css_selector('#gwt-uid-14')[0]
element.send_keys(UPPER_FL)
time.sleep(2)

print('Entered flight information and pressed Enter, this could take a while...')
element.send_keys(Keys.ENTER)
time.sleep(70)

print('Downloading generated PDF...')
element = driver.find_elements_by_css_selector('div.skb:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)')[0]
element.click()
time.sleep(20)

# logging out
print('Logging out...')
driver.get('https://www.skybriefing.com/c/portal/logout')
time.sleep(10)

# clean quit
driver.close()
print('All done!')
