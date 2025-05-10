from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


@given('kullanıcı Trendyol ana sayfasındadır')
def step_impl(context):
    context.driver.get("https://www.trendyol.com/")
    context.driver.maximize_window()
    time.sleep(3)

@when('kullanıcı çerezleri kabul eder')
def step_impl(context):
  context.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
  time.sleep(5)

@then('kullanıcı arama kutusuna "telefon" yazar ve arama yapar')
def step_impl(context):
    search_box=context.driver.find_element(By.CLASS_NAME, "V8wbcUhU")
    search_box.click()
    search_box.send_keys("telefon" +Keys.ENTER)

@then("kullanıcı ilk ürünü seçer")
def step_impl(context):
    time.sleep(3)  # Sayfanın yüklenmesini bekle
    ilk_urun = context.driver.find_element(By.CSS_SELECTOR, "div.p-card-wrppr a")
    ilk_urun.click()
    time.sleep(3)  # Ürün detay sayfası yüklensin
    context.driver.switch_to.window(context.driver.window_handles[-1])
@then("konum seç işaretlenir")
def step_impl(context):
    buton = context.driver.find_element(By.CLASS_NAME, "onboarding-popover__default-renderer-primary-button")
    buton.click()

@then("kullanıcı ürünü sepete ekler")
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME,"add-to-basket-button-text").click()
    time.sleep(3)


@then("kullanıcı ana sayfaya döner")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//img[@alt='Trendyol Türkçe']").click()
    current_url = context.driver.current_url
    assert current_url == "https://www.trendyol.com/", f"Hata: Ana sayfaya yönlendirilmedi, mevcut URL: {current_url}"


@given('kullanıcı ana sayfada arama kutusuna "laptop" yazar ve arama yapar')
def step_impl(context):
    search_boxx = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "V8wbcUhU"))
    )
    search_boxx.click()
    search_boxx.send_keys("laptop" + Keys.ENTER)

@when('kullanıcı "hp" markasını filtreler')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='fltr-item-text' and text()='HP']").click()
    time.sleep(3)


@then("kullanıcı ikinci ürünü seçer")
def step_impl(context):
    # Ürünlerin yüklendiğinden emin ol
    wait = WebDriverWait(context.driver, 10)
    second_product = wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//a[@class='p-card-chldrn-cntnr card-border'])[2]")  # İkinci ürünü seçiyoruz
    ))

    # İkinci ürüne tıklama
    second_product.click()
    context.driver.switch_to.window(context.driver.window_handles[-1])
@then("kullanıcı ikinci ürünü sepete ekler")
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME,"add-to-basket-button-text").click()
    time.sleep(3)

@given("kullanıcı sepete gider")
def step_impl(context):
    sepetim_link = context.driver.find_element(By.XPATH, "//p[@class='link-text' and text()='Sepetim']")
    sepetim_link.click()
    anladim_button = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Anladım']"))
    )
    anladim_button.click()
@then("kullanıcı sepette en az 1 ürün olduğunu doğrular")
def self_impl(context):
    sepet_header = context.driver.find_element(By.CLASS_NAME, "pb-header")
    sepet_metni = sepet_header.text
    if "Ürün" in sepet_metni:
        print("Sepette ürün var!")
    else:
        print("Sepet boş.")
