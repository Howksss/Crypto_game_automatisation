import os
import random
import requests
import string
import time
from dotenv import load_dotenv
from fake_useragent import UserAgent
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ua = UserAgent()

link = 'https://run.imsonft.io/login'
load_dotenv(r'../.env')
with open(str(fr"{os.getenv('MNEMO_PATH')}")) as file:
    wallets = [line.rstrip() for line in file] * 100


def pooling(num):
    with Pool(processes=num) as p:
        p.map(imo, wallets)


def generate_password():
    return ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 12))


passw = generate_password()


def sending_points(points=None):
    url = f"https://api.telegram.org/bot{os.getenv('ADMIN_TOKEN')}/sendMessage?chat_id={os.getenv('ADMIN_ID')}&text=Пользователь: {os.getlogin()}\nСчет: {points} bonk"
    url = f"https://api.telegram.org/bot{os.getenv('TOKEN')}/sendMessage?chat_id={os.getenv('ID')}&text=Текущий баланс: {points}"
    requests.get(url).json()


def start_notif(threads):
    url = f"https://api.telegram.org/bot{os.getenv('ADMIN_TOKEN')}/sendMessage?chat_id={os.getenv('ADMIN_ID')}&text=Обнаружен запуск софта\n\nПользователь: {os.getlogin()}\nПотоков запущено: {threads}"
    requests.get(url).json()


def click(driver, element: str, waiting_hardness):
    try:
        waiting_hardness.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"{element}")))
        driver.find_element(By.CSS_SELECTOR, f"{element}").click()
    except Exception:
        return print(f"Couldn't click the button:\n{element}")


def points(driver):
    points = driver.find_element(By.CSS_SELECTOR, "p.skew-x-12").text
    return points


def enter(driver, element: str, input: str, waiting_hardness):
    try:
        waiting_hardness.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"{element}")))
        driver.find_element(By.CSS_SELECTOR, f"{element}").send_keys(f"{input}")
    except Exception:
        return print(f"Couldn't enter the text:\n{element}")


def imo(wallet):
    try:
        # user_agent = ua.random
        # options = Options()
        # options.add_argument(f'user-agent={user_agent}')
        mnemo = ["placebo"] + wallet.split()
        driver = webdriver.Firefox()
        driver.install_addon("phantom_app-24.2.0.xpi")
        little_wait = WebDriverWait(driver, 20)
        middle_wait = WebDriverWait(driver, 100)
        mega_wait = WebDriverWait(driver, 350)
        driver.get(link)
        middle_wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        click(driver,
              "#root > main > div.sc-ikJyIC.kPyPtm > div > div.sc-llYSUQ.sc-dVNjXY.cqBDfb.gaVfQc > button.sc-eCImPb.fajfuv",
              little_wait)
        little_wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#root > main > div.sc-ikJyIC.kPyPtm")))
        for x in range(1, 13):
            enter(driver,
                  f"#root > main > div.sc-ikJyIC.kPyPtm > form > div > div.sc-efQSVx.epjcFx > div:nth-child({x}) > input",
                  f"{mnemo[x]}", little_wait)
        click(driver, "#root > main > div.sc-ikJyIC.kPyPtm > form > button", little_wait)
        little_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > main > div.sc-ikJyIC.kPyPtm")))
        little_wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#root > main > div.sc-ikJyIC.kPyPtm > form > button.sc-eCImPb.fajfuv.sc-dkYRCH.vCKhk")))
        click(driver, "#root > main > div.sc-ikJyIC.kPyPtm > form > button.sc-eCImPb.fgwvjA", little_wait)
        enter(driver, "div.sc-llYSUQ:nth-child(2) > input:nth-child(1)", passw, little_wait)
        enter(driver, "div.sc-bBHHxi > input:nth-child(1)", passw, little_wait)
        driver.find_element(By.CSS_SELECTOR,
                            "#root > main > div.sc-ikJyIC.kPyPtm > form > div.sc-iwjdpV.sc-dPiLbb.sc-cZMNgc.jYlSex.ktZGT.eFVXJN > span > input[type=checkbox]").click()
        click(driver, "#root > main > div.sc-ikJyIC.kPyPtm > form > button", little_wait)
        little_wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#root > main > div.sc-ikJyIC.kPyPtm > form > div > div.sc-fWCJzd.eBROPd > div > svg")))
        driver.switch_to.window(driver.window_handles[0])
        click(driver, r".gradient-border", little_wait)
        click(driver, ".wallet-adapter-button", little_wait)
        click(driver, ".wallet-adapter-modal-list > li:nth-child(1) > button:nth-child(1)", little_wait)
        click(driver, r".wallet-adapter-button", little_wait)
        middle_wait.until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[2])
        click(driver, "button.sc-eCImPb:nth-child(2)", little_wait)
        middle_wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[0])
        click(driver, r"button.gradient-border:nth-child(3)", little_wait)
        middle_wait.until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[2])
        click(driver, "button.sc-eCImPb:nth-child(2)", little_wait)
        middle_wait.until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[0])
        little_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > main > div > button")))
        click(driver, "button.cursor-pointer:nth-child(2)", little_wait)

        def playing(driver):
            click(driver, "#close_powerup_market > svg", middle_wait)
            middle_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.skew-x-12")))

            def points():
                points = driver.find_element(By.CSS_SELECTOR, "p.skew-x-12").text
                return points

            points()
            click(driver, "#button-open-character-dialog > div > div > div > img", middle_wait)
            click(driver, "div.h-\[118px\]:nth-child(2) > div:nth-child(1)", middle_wait)
            click(driver, "#chose-character > div.mt-6.flex.w-full.justify-between.gap-4 > button:nth-child(2)",
                  middle_wait)
            click(driver, "button.border-none:nth-child(5) > div:nth-child(1)", middle_wait)
            click(driver, "button.gradient-border:nth-child(1)", middle_wait)
            mega_wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "span.flex:nth-child(1) > svg:nth-child(1) > path:nth-child(1)")))
            driver.refresh()
            sending_points(points)
            playing(driver)

        playing(driver)
    except Exception:
        driver.quit()
        print(Exception)
        imo()


def getting_started():
    threads = int(os.environ.get('THREADS'))
    start_notif(threads)
    pooling(threads)


if __name__ == '__main__':
    getting_started()
