from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@given('I Launch Chrome Browser')
def launcBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('I Open Fabelio Homepage')
def openHomePage(context):
    context.driver.get("https://qa.fabelio.com/")

@when('I Move to Login Modal')
def loginModal(context):
    context.driver.find_element_by_xpath("//*[@id='topmenu-bar']/div/div[3]/div[2]/button").click()
    context.driver.implicitly_wait(2)

@when('I Click Register Link')
def registerPage(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Daftar')]").click()
    context.driver.implicitly_wait(5)

@then('I Expect That the Register Title is "{title}"')
def verifyTitle(context,title):
    register_title = context.driver.find_element_by_xpath("//div[@class='css-r7tjwg']").text
    assert (register_title == title)
    context.driver.implicitly_wait(2)
    context.driver.close()
#====================================

@when('I Set Null Value to the All Input Field')
def inputField(context):
    context.driver.find_element_by_id("first_name").send_keys()
    context.driver.find_element_by_id("last_name").send_keys()
    context.driver.find_element_by_id("email").send_keys()
    context.driver.find_element_by_id("password").send_keys()
    context.driver.find_element_by_id("password_confirmation").send_keys()
    context.driver.implicitly_wait(2)

@when('I Click on the Buat Akun Button')
def clickMasukButton(context):
    context.driver.find_element_by_xpath("//span[contains(text(),'Buat Akun')]").click()

@then('I Expect That Warning Message Should Be Displayed')
def warningMessage(context):
    warning_first_name=context.driver.find_element_by_id("first_name-helper-text").is_displayed()
    warning_last_name=context.driver.find_element_by_id("last_name-helper-text").is_displayed()
    warning_email=context.driver.find_element_by_id("email-helper-text").is_displayed()
    warning_password=context.driver.find_element_by_id("password-helper-text").is_displayed()
    warning_password_confirm=context.driver.find_element_by_id("password_confirmation-helper-text").is_displayed()

    assert warning_first_name is True
    assert warning_last_name is True
    assert warning_email is True
    assert warning_password is True
    assert warning_password_confirm is True
    context.driver.close()
#==================================================================================
@when('I Set Invalid Value for Email Field')
def invalidEmail(context):
    context.driver.find_element_by_id("first_name").send_keys("Adi")
    context.driver.find_element_by_id("last_name").send_keys("Darmawan")
    context.driver.find_element_by_id("email").send_keys("asd")
    context.driver.find_element_by_id("password").send_keys("1234567890")
    context.driver.find_element_by_id("password_confirmation").send_keys("1234567890")
    context.driver.implicitly_wait(2)

@when('I Click Aggrement Checkbox')
def aggrement(context):
    context.driver.find_element_by_id("checkbox_agreement").click()

@then('I Expect That Warning Message on Email Field Should Be Displayed')
def warningMessage(context):
    warning_email=context.driver.find_element_by_id("email-helper-text").is_displayed()

    assert warning_email is True
    context.driver.close()
#==================================================================================
@when('I Set Invalid Value for Password Field')
def invalidEmail(context):
    context.driver.find_element_by_id("first_name").send_keys("Adi")
    context.driver.find_element_by_id("last_name").send_keys("Darmawan")
    context.driver.find_element_by_id("email").send_keys("asd@gmail.com")
    context.driver.find_element_by_id("password").send_keys("123")
    context.driver.find_element_by_id("password_confirmation").send_keys("123")
    context.driver.implicitly_wait(2)

@then('I Expect That Warning Message on Password Field Should Be Displayed')
def warningMessage(context):
    warning_password=context.driver.find_element_by_id("password-helper-text").is_displayed()
    warning_password_confirm=context.driver.find_element_by_id("password_confirmation-helper-text").is_displayed()
    assert warning_password is True
    assert warning_password_confirm is True
    context.driver.close()
#================================================================================
@when('I Set Valid Value For Each Field')
def invalidEmail(context):
    context.driver.find_element_by_id("first_name").send_keys("Adi")
    context.driver.find_element_by_id("last_name").send_keys("Darmawan")
    context.driver.find_element_by_id("email").send_keys("asd@gmail.com")
    context.driver.find_element_by_id("password").send_keys("123123123")
    context.driver.find_element_by_id("password_confirmation").send_keys("123123123")
    context.driver.implicitly_wait(2)

@then('I Expect That Warning Message on Checkbox Should Be Displayed')
def warningMessage(context):
    warning_checkbox=context.driver.find_element_by_class_name("MuiFormHelperText-root").is_displayed()
    assert warning_checkbox is True
    context.driver.close()