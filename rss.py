
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.fotmob.com/news")
print(driver.title)
driver.quit()

print("RSS file created at: ", os.path.abspath("rss.xml"))