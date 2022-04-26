import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


wordle_URL="https://www.powerlanguage.co.uk/wordle/"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument=('--no-sandbox')
chrome_options.add_argument=('--window=size=1920,1080')
chrome_options.add_argument=('--headless')
chrome_options.add_argument=('--disable-gpu')
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wd.get(wordle_URL)
jsonstring=json.loads(wd.execute_script("return window.localStorage.getItem('nyt-wordle-state')"))
solution=jsonstring["solution"]
print(solution)

