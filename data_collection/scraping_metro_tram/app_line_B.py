import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

path=Service("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver\\chromedriver.exe")
browser = webdriver.Chrome(chrome_options=options, service=path)
browser.get("http://www.ferro-lyon.net/Metro-sur-pneus/lignes-A-B/ligne-B-station-par-station/")

time.sleep(3)
#LIGNE B

# Creating the dataframe

df = pd.DataFrame(columns=['name', 'link', 'line', 'city'])


# LOOP
for i in range(1,11):
    dict = {'name':'', 'link':'', 'line': 'B', 'city':'lyon'}

    station_link = browser.find_element(By.XPATH,"""//*[@id="som"]/ul/li["""+str(i)+"""]/a""")                                               
    title = browser.find_element(By.XPATH,"""//*[@id="som"]/ul/li["""+str(i)+"""]/a""").get_attribute('title')
                                        
    time.sleep(2)

    station_link.click()

    time.sleep(3)

    link_gps = browser.find_element(By.XPATH,'//*[@id="contenu"]/div[1]/table[1]/tbody/tr[9]/td/a').get_attribute('href')
                                            
    dict.update({'name': str(title)})
    dict.update({'link': str(link_gps)})
    df = df.append(dict, ignore_index=True)

    time.sleep(3)

    if i == 10:
        df.to_csv('save_output_scrapping/save_output/output_line_B.csv')
        browser.quit()
    else:
        browser.back()