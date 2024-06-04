from seleniumbase import BaseCase
from ARMember.page_objects.login_page import loginPageConstants as lc
from time import sleep
class loginTest(BaseCase):
    
    def testloginwithrightcred(self):
        self.open(lc.url)    
        username = self.find_element("name",lc.username_locator)
        username.send_keys(lc.correct_username)
        psw = self.find_element("name",lc.psw_locator)
        psw.send_keys(lc.correct_username)
        self.click("name",lc.submitbtn)
        sleep(2)
        redirected_url = self.get_current_url()
        cookies = self.get_cookies()
        self.assertEqual(redirected_url,lc.redirect_url)
        print(cookies)
    pass