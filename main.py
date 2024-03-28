from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import itertools, random, json, requests, time, pyautogui
from playsound import playsound
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
BASE_URL = "https://api-create-account.onfing.ir"
PANEL_USERNAME = "nima"
PANEL_PASSWORD = "Nima1234"
USERNAME = random.sample([''.join(combo) for combo in list(itertools.combinations(LETTERS,7))],1)[0]
PASSWORD = f"A{random.sample([''.join(combo) for combo in list(itertools.combinations(LETTERS,7))],1)[0]}"
FIRST_NAME = random.sample([''.join(combo) for combo in list(itertools.combinations(LETTERS,7))],1)[0]
LAST_NAME = random.sample([''.join(combo) for combo in list(itertools.combinations(LETTERS,7))],1)[0]
EMAIL = f"{USERNAME}@outlook.com"
BIRTH_MONTH = 'july' 
BIRTH_DAY = f"{random.randint(1, 28):02d}"
BIRTH_YEAR = str(random.randint(1990, 2004))

driver = webdriver.Chrome()
# seleniumwire_options = {'proxy': {'http': PROXY["proxy_address"], 'verify': False}}
try:
    driver.maximize_window()
    driver.get("https://signup.live.com/signup")
    time.sleep(10)
    email = driver.find_element(By.XPATH, """//*[@id="MemberName"]""").send_keys(EMAIL)
    time.sleep(1)
    driver.find_element(By.XPATH, """//*[@id="iSignupAction"]""").click()
    time.sleep(10)
    driver.find_element(By.ID, "PasswordInput").click()
    pyautogui.write(PASSWORD)
    time.sleep(1)
    driver.find_element(By.XPATH, """//*[@id="iSignupAction"]""").click()
    time.sleep(10)
    driver.find_element(By.XPATH, """//*[@id="FirstName"]""").send_keys(FIRST_NAME)
    driver.find_element(By.XPATH, """//*[@id="LastName"]""").send_keys(LAST_NAME)
    time.sleep(1)
    driver.find_element(By.XPATH, """//*[@id="iSignupAction"]""").click()
    time.sleep(1)
    try:
        birth_month = driver.find_element(By.XPATH, """//*[@id="BirthMonth"]""").send_keys(BIRTH_MONTH)
        time.sleep(1)
        birth_day = driver.find_element(By.XPATH, """//*[@id="BirthDay"]""").send_keys(BIRTH_DAY)  
        time.sleep(1)
        birth_year = driver.find_element(By.XPATH, """//*[@id="BirthYear"]""").send_keys(BIRTH_YEAR)
        time.sleep(1)
    except:
        # playsound('./note.mp3')
        input("please enter to continue : ")
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, """//*[@id="iSignupAction"]""").click()
        time.sleep(20)
        input("if you are solved capcha please click enter key : ")
        time.sleep(10)
        driver.find_element(By.XPATH, """//*[@id="id__0"]""").click()
        time.sleep(20)
        driver.find_element(By.XPATH, """//*[@id="idBtn_Back"]""").click()
        time.sleep(30)
    except:
        # playsound('./note.mp3')
        print("you are wrong")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    try:
        driver.get("https://outlook.com")
        time.sleep(20)
        EMAIL_COOKIE = json.dumps(driver.get_cookies())
    except:
        # playsound('./note.mp3')
        print('you are wrong')

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    time.sleep(10)
    try:
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input").send_keys(EMAIL)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input").send_keys(FIRST_NAME + " " +LAST_NAME)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input").send_keys(USERNAME)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/label/input").send_keys(PASSWORD)
    except:
        # playsound('./note.mp3')
        input("please enter to continue : ")
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input").send_keys(EMAIL)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input").send_keys(FIRST_NAME + " " +LAST_NAME)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input").send_keys(USERNAME)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/label/input").send_keys(PASSWORD)

    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/div").click()
    time.sleep(10)

    try:
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").send_keys(BIRTH_MONTH)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").send_keys(BIRTH_DAY)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").send_keys(BIRTH_YEAR)
    except:
        # playsound('./note.mp3')
        input("please enter to continue : ")
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").send_keys(BIRTH_MONTH)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").send_keys(BIRTH_DAY)
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").send_keys(BIRTH_YEAR)

    driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div/div[6]").click()
    
    input("if you are account created please click enter key : ")
    INSTA_COOKIE = json.dumps(driver.get_cookies())
    input("if you are go to threads please click enter key : ")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[3])
    driver.get("https://www.threads.net/")
    THREADS_COOKIE = json.dumps(driver.get_cookies())
    time.sleep(10)
    requests.post(f"{BASE_URL}/create_accounts/add_account", json={
        "full_name": FIRST_NAME + " " +LAST_NAME,
        "username": USERNAME,
        "password": PASSWORD,
        "insta_cookie": INSTA_COOKIE,
        "threads_cookie": THREADS_COOKIE,
        "email": EMAIL,
        "email_password": PASSWORD,
        "email_cookie": EMAIL_COOKIE,
        "phone_number": "",
        # "proxy_id": PROXY["id"],
        "birth_date": f"{BIRTH_DAY} - {BIRTH_MONTH} - {BIRTH_YEAR}"
    })
except Exception as e:
    # playsound('./note.mp3')
    print(e)
    driver.close()