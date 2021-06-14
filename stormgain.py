from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import json
from  random import randint

with open ('settings.json') as config_file:
    config = json.load(config_file)
stormgainemail = config['stormgain_email']
stormgainpw = config['stormgain_pw']
fromA = config['stormgainsleepMIN']
toB = config['stormgainsleepMAX']
path = os.getcwd()+'\\'
chrome_options = Options()
chrome_options.add_argument('--window-size=1600x800')
chrome_options.add_argument(path)



class browserstarter:

    def start(self):
        chrome_driver = path +"\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        self.vars = {}
        self.driver.get("https://trading-tigers.com")
        time.sleep(randint(3,6))
        os.system('cls')
        print("Browser started!")
        start.stormgain()

    def startup(self):
        start.start()

    def stormgainsleeper(self):
        sleeptime = randint(fromA, toB)
        self.driver.close()
        print('Miner is Activ!\nNext Claim in',sleeptime, 'sec')
        time.sleep(sleeptime)
        start.start()


    def shortsleep(self):
        print('Short Sleep Triggert!\nClose Browser!')
        self.driver.close()
        ran = randint(1000,3000)
        print("Sleep:",int(ran),"sec")
        time.sleep(ran)
        start.start()

    def claimusdt(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
        except Exception as e:
            print(e)

    def checkusdt(self):
        try:
            html = self.driver.find_element_by_xpath('//*[@id="region-main"]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/span[1]').get_attribute('innerHTML')
            usdt = html.replace('≈','')
            print('You have Mined '+str(usdt)+'$')
            if float(usdt) >= float(10):
                print('More Than 10USDT, Claim it now!')
                start.claimusdt()
        except Exception as e:
            print(e)

    def stormgain(self):
        try:
            self.driver.get("https://app.stormgain.com/#modal_login")     
            time.sleep(randint(3,6))
            self.driver.find_element(By.ID, "email").send_keys(stormgainemail)
            self.driver.find_element(By.ID, "password").send_keys(stormgainpw)
            time.sleep(randint(3,6))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
            time.sleep(randint(10,25))
            self.driver.get('https://app.stormgain.com/crypto-miner/')
            time.sleep(randint(3,10))
            #self.driver.switch_to.frame(0)
            start.checkusdt()
            self.driver.refresh()
            time.sleep(randint(3,10))
            #self.driver.switch_to.frame(0)
        except:
            start.shortsleep()
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".font-medium > .text-17").click()
            time.sleep(randint(3,6))
            print('Miner is Activ!')
            start.stormgainsleeper()
        except:
            print('Mining already active?\nGetting Short Sleep!')
            start.shortsleep()
            if KeyboardInterrupt:
                exit()

start = browserstarter()
start.start()
