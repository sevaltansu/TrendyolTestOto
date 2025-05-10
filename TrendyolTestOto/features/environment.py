
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def before_all(context):
    service = Service("./chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option(name="detach", value=True)
    context.driver = webdriver.Chrome(service=service, options=options)

def after_all(context):
    context.driver.quit()


