from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
from bs4 import BeautifulSoup as soup
import pandas as pd

df_vin = pd.read_csv('vin_11.csv')
vin = []


def web_scrap():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--disable-extensions")

  for i in df_vin['vin_11'][20:30]:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.autodna.com/")

    ## Finding Elements
    search = driver.find_element(By.CLASS_NAME, 'vin-input')
    search.send_keys(i + '123456')
    driver.find_element(By.CLASS_NAME, 'vin-btn').click()
    time.sleep(15)

    S = soup(driver.page_source, "html.parser")
    t = str(S.title).split(' | ')[1].split(' - ')[0].split(' ')
    d = {'vin_11': i, 'Make': t[0], 'Model': ' '.join(t[1:])}
    print(d)
    vin.append(d)
    driver.quit()

  with open('data-vin.json', 'w') as outfile:
    json.dump(vin, outfile)
  df = pd.read_json('data-vin.json')
  df.to_csv('data-vin.csv')


if __name__ == "__main__":
  web_scrap()
