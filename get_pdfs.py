import selenium.webdriver as webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

### CONFIG START ###

WITH_LOGIN = False # Use script with login? if True, fill out info below
USER = 'my_login'
PW = 'my_password'
FLUGPLATZ = 'LSZH'
LOWER_FL = '000'
UPPER_FL = '120'

### CONFIG END ###

#set up a virtual display
print 'Setting up virtual display and driver...'
display = Display(visible=0, size=(800, 600))
display.start()

# set up firefox
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', "~/temp/")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/pdf'))
profile.set_preference('pdfjs.disabled', True)
driver = webdriver.Firefox(profile)

print 'Opening website...'
driver.get("http://www.skybriefing.com/portal")
time.sleep(10)
#driver.maximize_window()

## download DABS PDF
print 'Downloading first PDF...'
element = driver.find_elements_by_xpath('//*[@id="v-dabsportlet_WAR_ibsportletdabs_LAYOUT_10454"]/div/div[2]/div/div[4]/div/div/div/a')[0]
element.click()
time.sleep(10)

if not WITH_LOGIN:
    driver.quit()
    print 'Done.'
    quit()

print 'Logging in...'
driver.get("https://www.skybriefing.com/portal/de/web/guest/signinnativ")
time.sleep(20)
# username
element = driver.find_elements_by_xpath('//*[@id="_58_login"]')[0]
element.send_keys(USER)
time.sleep(2)
#pw
element = driver.find_elements_by_xpath('//*[@id="_58_password"]')[0]
element.send_keys(PW)
time.sleep(2)
element.send_keys(Keys.ENTER)
time.sleep(5)
driver.get('https://www.skybriefing.com/portal/de/new-area-briefing')
time.sleep(10)

# Information Area
element = Select(driver.find_elements_by_css_selector('div.v-select:nth-child(1) > select:nth-child(1)')[0])
#element.select_by_visible_text("Switzerland")
element.select_by_visible_text(COUNTRY)
time.sleep(2)

# Flugplatz
element = driver.find_elements_by_css_selector('input.v-widget:nth-child(1)')[0]
element.send_keys(FLUGPLATZ)
time.sleep(2)

# lower FL
element = driver.find_elements_by_css_selector('#gwt-uid-5')[0]
element.send_keys(LOWER_FL)
time.sleep(2)

# upper FL

element = driver.find_elements_by_css_selector('#gwt-uid-15')[0]
element.send_keys(UPPER_FL)
time.sleep(2)

print 'Entered flight information and pressed Enter, this could take a while...'
element.send_keys(Keys.ENTER)
time.sleep(60)

print 'Downloading generated PDF...'

element = driver.find_elements_by_css_selector('div.skb:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(2)')[0]
element.click()
time.sleep(20)

# logging out
print 'Logging out...'
driver.get('https://www.skybriefing.com/portal/de/c/portal/logout')
time.sleep(10)

# clean quit
driver.quit()
print 'All done!'
