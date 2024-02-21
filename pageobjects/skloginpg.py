import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from testdata.sklogindata import SKLoginData
class SKLoginPg:
    title_text = "//*[@class='ui inverted centered header']"
    register_xpath = "//*[@class='ui inverted basic button']"
    login_xpath="//*[@class='ui inverted green basic button']"

    def verify_subtitle(self,driver):
        sub_title_element = driver.find_element(By.XPATH,SKLoginPg.title_text)
        if sub_title_element.is_displayed():
            txt = sub_title_element.text
            print("txt = ",txt)
            assert txt == SKLoginData.sk_footer_title
        else:
            print("Element not displayed")
            assert False

    def verify_register(self,driver):
        sub_title_element = driver.find_element(By.XPATH,SKLoginPg.register_xpath)
        if sub_title_element.is_displayed():
            txt = sub_title_element.text
            print("txt = ", txt)
            assert txt == SKLoginData.sk_register
        else:
            print("Element not displayed")
            assert False

    def verify_register_button(self,driver):
        driver.find_element(By.XPATH,SKLoginPg.register_xpath).click()
        driver.explicity_wait(10)
        driver.close()

    def verify_login(self,driver):
        sub_title_element = driver.find_element(By.XPATH,SKLoginPg.login_xpath)
        if sub_title_element.is_displayed():
            txt = sub_title_element.text
            print("txt = ", txt)
            assert txt == SKLoginData.sk_login
        else:
            print("Element not displayed")
            assert False

    def verify_login_button(self,driver,creds):
        driver.find_element(By.XPATH,SKLoginPg.login_xpath).click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//*[@name='phps_usern']").send_keys(creds[0])
        driver.find_element(By.XPATH, "//*[@name='phps_passwd']").send_keys(creds[1])
        driver.find_element(By.XPATH, "//*[@name='phps_login']").click()
        driver.find_element(By.LINK_TEXT,"Home").click()
        first = driver.find_element(By.XPATH,"//*[@id='all-items']/div[2]").click()
        admin=driver.find_element(By.XPATH,"(//*[@class='ui inverted button price-button'])[2]").click()
        action = ActionChains(driver)
        action.move_to_element(first).perform()
        driver.find_element(By.ID,"modalBuy").click()
        time.sleep(10)
        # driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]").click()
        # driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/a[6]").click()
        driver.close()

    def verify_Register_button2(self,driver,creds):
        driver.find_element(By.XPATH,SKLoginPg.register_xpath).click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//*[@name='usern']").send_keys(creds[0])
        driver.find_element(By.XPATH,"//*[@name='email']").send_keys(creds[1])
        driver.find_element(By.XPATH, "//*[@name='passwd']").send_keys(creds[2])
        driver.find_element(By.XPATH, "//*[@name='cpasswd']").send_keys(creds[3])
        driver.find_element(By.XPATH,"//*[@name='phps_register']").click()
        driver.find_element(By.XPATH, "//*[@name='phps_usern']").send_keys(creds[0])
        driver.find_element(By.XPATH, "//*[@name='phps_passwd']").send_keys(creds[2])
        driver.find_element(By.XPATH, "//*[//*[@name='phps_login']]").click()
        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]").click()
        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/a[6]").click()
        driver.close()
