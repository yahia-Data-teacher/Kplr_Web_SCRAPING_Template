from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json
import pandas as pd
# lecture des données à partir du fichier csv
df_vin = pd.read_csv('vin_11.csv')
vin = []


def web_scrap():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--disable-extensions")

  for i in df_vin['vin_11'][10:30]:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.autodna.com/")


#Complete Code
if __name__ == "__main__":
  web_scrap()
