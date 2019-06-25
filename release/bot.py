from selenium import webdriver

# CONFIGURATIONS HERE

DRIVER_PATH = '/Users/danielkwong/Desktop/chromedriver'
URL = "https://fearofgod.com//products/flannel-shirt-jacket-1"

driver = webdriver.Chrome(executable_path=r''+DRIVER_PATH)
driver.get(URL)
