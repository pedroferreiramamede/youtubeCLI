from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import time
from termcolor import colored

driver=webdriver.Firefox()
driver.minimize_window()

searchVideo = str(raw_input("Busca: "))

#driver.get('https://github.com/')
driver.get('https://youtube.com/')
#driver.quit()

inputElement = driver.find_element_by_name("search_query")
inputElement.send_keys(searchVideo)
inputElement.submit()

time.sleep(2.8)


RESULTS_LOCATOR = "//div/h3/a"

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

for item in page1_results:
    print colored ([page1_results.index(item)], 'green'), colored (item.text, 'yellow')
    
videoIndex = raw_input("Escolha um video: ")
videoIndex = int(videoIndex)


link = driver.find_element_by_link_text(page1_results[videoIndex].text)
link.click()

time.sleep(8)
try:                                   
    driver.find_element_by_class_name('videoAdUiSkipButton.videoAdUiAction.videoAdUiFixedPaddingSkipButton').click();
    print 'ad skiped'
except:
    print 'did not find the button to skip ad 1'

try:
    driver.find_element_by_class_name('ytp-ad-skip-button.ytp-button').click();
    print 'ad skiped'
except:
    print 'did not find the button to skip ad 2'


print colored ('[p]', 'green'), colored ('play/pause', 'yellow')
print colored ('[q]', 'green'), colored ('quit', 'yellow')
print colored ('[s]', 'green'), colored ('skip ad', 'yellow')

print colored ('Control:', 'red')

musicPlaying = True
appPlaying = True
while appPlaying:
    actionOnPlaying = raw_input()
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

    if actionOnPlaying == 's':
        print 'skip ad >|'
        sys.stdout.write("\033[F") #back to previous line
        sys.stdout.write("\033[K") #clear line
        try:                                   
            driver.find_element_by_class_name('videoAdUiSkipButton.videoAdUiAction.videoAdUiFixedPaddingSkipButton').click();
            print 'ad skiped'
	    sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
        except:
            print 'did not find the button to skip ad 1'
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
        try:
            driver.find_element_by_class_name('ytp-ad-skip-button.ytp-button').click()
            print 'ad skiped'
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
        except:
            print 'did not find the button to skip ad 2'
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line   
    if actionOnPlaying == 'p':
        if musicPlaying
            print '||'
            driver.find_element_by_class_name('ytp-play-button.ytp-button').click()
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
            musicPlaying = False
        else:
            print '>'
            driver.find_element_by_class_name('ytp-play-button.ytp-button').click()
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line
            musicPlaying = True
    if actionOnPlaying == 'q':
        print 'exiting...'
        driver.quit()
        appPlaying = False
