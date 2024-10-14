from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager




class SumanSimpleTestScripts:


   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   # start the selenium automation
   def start_automation(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : unable to automate !")
           return False


   # shutdown the selenium automation
   def shutdown(self):
       self.driver.close()
       return True


   # fetch the URL of the web application
   def fetch_url(self):
       if self.start_automation():
           return self.driver.current_url
       else:
           print("ERROR : URL cannot be fetched !")
           return False


   # fetch the TITLE of the web application
   def fetch_title(self):
       if self.start_automation():
           return self.driver.title
       else:
           print("ERROR : TITLE cannot be fetched !")
           return False




if __name__ == "__main__":
   url = "https://www.saucedemo.com/"
   suman = SumanSimpleTestScripts(url)
   suman.start_automation()
   print(suman.fetch_title())
   print(suman.fetch_url())
   suman.shutdown()

