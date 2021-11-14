from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.google.ro/")

button = driver.find_element_by_id("L2AGLb")
button.click()

searchField = driver.find_element_by_name("q")
searchField.send_keys("facebook")

searchButton = driver.find_element_by_name("btnK")
searchButton.submit()

facebookLink = driver.find_element_by_partial_link_text("Facebook - conectează-te sau înscrie-te")
facebookLink.click()

acceptFacebookButton = driver.find_element_by_css_selector("._9xo5 ._9xo7")
acceptFacebookButton.click()

emailField = driver.find_element_by_id("email")
emailField.send_keys("something@something.com")
passwordField = driver.find_element_by_id("pass")
passwordField.send_keys("password123")

connectFacebookButton = driver.find_element_by_name("login")
connectFacebookButton.click()

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.element_to_be_clickable((By.ID, "loginbutton")))

errorMeessage = driver.find_element_by_class_name("_9ay7")
assert errorMeessage.text == "Adresa de e-mail introdusă nu este asociată unui cont. Găseşte-ţi contul şi conectează-te."
