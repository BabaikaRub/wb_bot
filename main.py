import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import schedule


class Clicker:
    def __init__(self, url):
        self.url = url

    def click(self, browser):
        browser.find_element(By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/app-edit-auction-campaign/div/form/app-campaign-card/div/form/div[1]/div[1]/div[2]/div[1]/app-number-ticker/div/div[3]/i').click()

        #error = browser.find_element(By.CLASS_NAME, 'toast toast--error ng-star-inserted')
        
    
    def save_result(self, browser):
        browser.find_element(By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/app-edit-auction-campaign/div/form/div[9]/div/button[2]').click()
        print('[INFO] Saved succes')
        time.sleep(2)
    
    def check_result(self, browser):

        flag_list = ['1-2', '1', '2']

        result = browser.find_element(By.XPATH, '/html/body/app-root/div/div[1]/div[2]/div/app-edit-auction-campaign/div/form/app-campaign-card/div/form/div[1]/div[1]/div[2]/div[2]/span').text.replace(' ', '')
        
        if result in flag_list:
            return True
        
        else:
            return False

    def start(self):
        options_chrome = webdriver.ChromeOptions()
        options_chrome.add_argument("--start-maximized")
        options_chrome.add_argument('user-data-dir=C:\\Users\\rodio\\PycharmProjects\\wild_bot\\data\\User Data')
        
        print('[INFO] Programm started')

        try:
            browser = webdriver.Chrome(options=options_chrome)
            
            browser.get(self.url)
            time.sleep(7)

            browser.execute_script("window.scrollBy(0,450)")

            while not self.check_result(browser):
                self.click(browser)
                time.sleep(0.5)
            
            self.save_result(browser)
                          
            print('[INFO] We get needed place')
            time.sleep(3)

        except Exception as _ex:
            print(f'[ERROR] {_ex}')

        finally:
            browser.quit()
            print('[INFO] Finished')


def main():
    url = 'https://cmp.wildberries.ru/campaigns/list/active/edit/search/3248023'

    wb_clicker = Clicker(url)

    wb_clicker.start()
    #schedule.every(3).minutes.do(wb_clicker.start(), url)

    # while True:
    #     schedule.run_pending()


if __name__ == '__main__':
    main()
