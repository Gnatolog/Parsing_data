from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import SaveHdd
import WorkWebSite

# поключаем driver
# region parametr Brauser
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless=new")  # for Chrome >= 109
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome()  # режим браузера:  options true безгаловый
url = "https://investidor.cmvm.pt/PInvestidor/Content?Input" \
      "=2261423276FE736012E5188493A75BA7DF245F268FA18A136059316E2C3550AE "
driver.get(url)
# endregion

test = WorkWebSite.test(url, driver, "black_list")
save = SaveHdd.save_json(test)



