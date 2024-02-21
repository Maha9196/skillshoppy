import time

import pytest

from helpers.common_methods import Helper
from pageobjects import skloginpg
from pageobjects.skloginpg import SKLoginPg

helper = Helper()
skloginpg = SKLoginPg()

class Test_SKLoginTC:

    def test_verify_subtitle(self):
        driver = helper.create_driver()
        helper.open_url()
        skloginpg.verify_subtitle(driver)
        helper.close_browser()

    def test_verify_register(self):
        driver = helper.create_driver()
        helper.open_url()
        skloginpg.verify_register(driver)
        helper.close_browser()

    def test_verify_register_button(self):
        driver = helper.create_driver()
        helper.open_url()
        skloginpg.verify_register_button(driver)
        helper.close_browser()



    def test_verify_login(self):
        driver = helper.create_driver()
        helper.open_url()
        skloginpg.verify_login(driver)
        helper.close_browser()

    def test_verify_login_button(self):
        driver = helper.create_driver()
        helper.open_url()
        skloginpg.verify_login_button(driver)
        time.sleep(10)
    @pytest.mark.m1
    @pytest.mark.parametrize("creds", helper.getuserlist())
    def test_verify_login_button(self, creds):
        driver = helper.create_driver()
        helper.open_url()
        print("creds", creds)
        skloginpg.verify_login_button(driver,creds)
        helper.close_browser()

    @pytest.mark.m1
    @pytest.mark.parametrize("creds", helper.getregisterlist())
    def test_verify_register_button2(self, creds):
        driver = helper.create_driver()
        helper.open_url()
        print("creds", creds)
        skloginpg.verify_Register_button2(driver,creds)
        helper.close_browser()
