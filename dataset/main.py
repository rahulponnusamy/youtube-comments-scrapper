import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

data=[]

with Chrome(executable_path=r'C:\Users\KUDSIT\Downloads\chromedriver_win32 (1)\chromedriver.exe') as driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s")

    for item in range(200):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append(comment.text)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.DataFrame(data, columns=['comment'])
    df.head()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
