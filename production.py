# BISMILLAH ARRAHMAN ARRAHEEM
import os
os.environ['DISPLAY'] = ':1'  # Use the virtual display

import random
import traceback
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep as wait
from selenium import webdriver
from datetime import datetime
from datetime import timedelta
import time
import schedule
import subprocess
from selenium.webdriver.chrome.service import Service as ChromeService
import sys
from jafri_chromedriver_installer import installer
import pyautogui
import platform

def setup_proxy():
    PROXIES = [
       "22347aaf0f62e90dcd23__cr.it:c1929c8f6c32c506@gw.dataimpulse.com:823",
    ]
    proxy = random.choice(PROXIES)
    auth, ip_port = proxy.split('@')
    PROXY_USER, PROXY_PASS = auth.split(':')
    PROXY_HOST, PROXY_PORT = ip_port.split(':')

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy", "tabs", "unlimitedStorage", "storage",
            "<all_urls>", "webRequest", "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        }
    }
    """

    background_js = f"""
    var config = {{
        mode: "fixed_servers",
        rules: {{
            singleProxy: {{
                scheme: "http",
                host: "{PROXY_HOST}",
                port: parseInt({PROXY_PORT})
            }},
            bypassList: ["localhost"]
        }}
    }};
    chrome.proxy.settings.set({{value: config, scope: "regular"}}, function() {{}});
    function callbackFn(details) {{
        return {{
            authCredentials: {{
                username: "{PROXY_USER}",
                password: "{PROXY_PASS}"
            }}
        }};
    }}
    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {{urls: ["<all_urls>"]}},
        ['blocking']
    );
    """

    ext_dir = 'proxy_auth_extension'
    os.makedirs(ext_dir, exist_ok=True)
    with open(os.path.join(ext_dir, 'manifest.json'), 'w') as f:
        f.write(manifest_json)
    with open(os.path.join(ext_dir, 'background.js'), 'w') as f:
        f.write(background_js)

    return ext_dir


def load_driver():
    try:

        options = webdriver.ChromeOptions()


        ext_dir = setup_proxy()

        extension_path = os.path.join(os.getcwd(), "CapMonst_extension")
        print(f"Loading extension from: {extension_path}")
        options.add_argument(f'--load-extension=/var/www/python-bot/CapMonst_extension,{os.path.abspath(ext_dir)}')
        options.add_argument(f'--disable-extensions-except=/var/www/python-bot/CapMonst_extension,{os.path.abspath(ext_dir)}')

        # options.add_argument(f'load-extension={extension_path}')  # Note the '--' prefix
        # options.add_argument(f'load-extension={os.getcwd()}/CapMonst_extension')
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')
        options.add_argument('--lang=en')
        options.add_argument('start-maximized')
        options.add_argument('lang=en')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        
        # Add WSL-specific options

        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument(f'--user-data-dir=/tmp/chrome-profile-new')
        # Add consistent window size
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])  # Removes navigator.webdriver flag
        installer.install_chromedriver()
        driver = webdriver.Chrome(options=options)

        driver.get("https://whatismyipaddress.com/")
        wait(5)
        # # chrome.exe --remote-debugging-port=9250 --user-data-dir=remote-profile
        # options = Options()
        # options.add_experimental_option('debuggerAddress', 'localhost:9250')
        # driver = webdriver.Chrome(options=options)
    except Exception as e:
        print_log(f"Failed to load chrome, Make sure your Chrome is updated...")
        print_log(custom_traceback(traceback.format_exc()))

    return driver


def custom_traceback(traceback):
    if 'Stacktrace:' in traceback:
        return traceback.split('Stacktrace:')[0]
    else:
        return traceback


def print_log(message):
    time_stemp = str(datetime.now())
    time_stemp = f"{time_stemp.split('.')[0]}:{time_stemp.split('.')[1][0:2]}"
    msg = f"{time_stemp} - {message}"
    print(msg)
    log_file = open('data_files/logs.txt', 'a')
    log_file.write(f"{msg}\n")


def get_time_list(start_time, end_time):
    start = datetime.strptime(start_time, "%I:%M %p")
    end = datetime.strptime(end_time, "%I:%M %p")
    time_list = []
    current_time = start
    while current_time <= end:
        time_list.append((current_time.strftime("%I:%M %p").lstrip("0")))
        current_time += timedelta(minutes=1)  # Increment by 1 minute

    return time_list


def get_data():
    try:
        data = open('data_files/data.txt', 'r').read().split('\n')
        date_to_book = data[0].split('==')[1]
        full_price = data[1].split('==')[1]
        r_f_rap_mic_card = data[2].split('==')[1]
        r_f_rap_museo_ebraico_roma = data[3].split('==')[1]
        r_f_rap_villa_farnesina = data[4].split('==')[1]
        reduced_fair = data[5].split('==')[1]
        free_roma_pass = data[6].split('==')[1]
        f_a_t_r_disabled_person = data[7].split('==')[1]
        f_a_t_r_person_accompanying_the_disabled_person = data[8].split('==')[1]
        f_a_t_r_italian_teacher_with_miur_module = data[9].split('==')[1]
        f_a_t_r_fine_arts_teacher_sutdent = data[10].split('==')[1]
        f_a_t_r_cultural_heritage_teacher_student = data[11].split('==')[1]
        f_a_t_r_journalist = data[12].split('==')[1]
        f_a_t_r_tourist_interpreter = data[13].split('==')[1]
        f_a_t_r_iccrom_member = data[14].split('==')[1]
        f_a_t_r_icom_members_individual = data[15].split('==')[1]
        f_a_t_r_ministry_of_culture_staff = data[16].split('==')[1]
        f_a_t_r_eu_teachers_attested_cultural_subjects = data[17].split('==')[1]
        free_addition_under_18 = data[18].split('==')[1]
        group_leader = data[19].split('==')[1]
        guide_pass = data[20].split('==')[1]
        tour_guide = data[21].split('==')[1]
        start_time_input = data[22].split('==')[1]
        end_time_input = data[23].split('==')[1]
        api_key = data[24].split('==')[1]
        url = data[25].split('==')[1]
        time_list = get_time_list(start_time_input, end_time_input)

        return date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, api_key, url, time_list
    except:
        print_log("Error in loading data make sure you've entered data in correct form.")
        print_log(custom_traceback(traceback.format_exc()))


# def add_extenstion_api_key(driver, api_key):
#     driver.get("chrome-extension://pabjfbciaedomjjfelfafejkppknjleh/popup.html")
#     WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

#     driver.find_element(By.ID, "client-key-input").send_keys(api_key)
#     wait(5)
#     driver.find_element(By.ID, "client-key-save-btn").click()
#     wait(2)


def add_extenstion_api_key(driver, api_key):
    driver.get("chrome-extension://pabjfbciaedomjjfelfafejkppknjleh/popup.html")
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    input_elem = driver.find_element(By.ID, "client-key-input")
    existing_value = input_elem.get_attribute("value")

    # Check if the existing value is already the same as the new API key
    if existing_value == api_key:
        print("API key already exists. No need to update.")
        return

    input_elem.clear()
    input_elem.send_keys(api_key)
    wait(5)
    driver.find_element(By.ID, "client-key-save-btn").click()
    wait(2)


def time_to_refresh_the_page_func(time_to_refresh_the_page):
    if time_to_refresh_the_page != "":
        current_time = datetime.now().time()
        if current_time < time_to_refresh_the_page:
            print_log(f"Waiting for '{time_to_refresh_the_page}' to refresh page")
            while True:
                current_time = datetime.now().time()
                if current_time >= time_to_refresh_the_page:
                    break
                else:
                    time.sleep(0.001)  # wait for 1 second


def input_tickets(driver, element_text, input_text, span_or_label):
    if input_text != "":
        try:
            if span_or_label == 'label':
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, f"//div[@data-convention-label='{element_text}']")))
                driver.find_element(By.XPATH, f"//div[@data-convention-label='{element_text}']").find_element(By.TAG_NAME, "input").send_keys(Keys.BACKSPACE)
                driver.find_element(By.XPATH, f"//div[@data-convention-label='{element_text}']").find_element(By.TAG_NAME, "input").send_keys(Keys.BACKSPACE)
                driver.find_element(By.XPATH, f"//div[@data-convention-label='{element_text}']").find_element(By.TAG_NAME, "input").send_keys(input_text)
                driver.find_element(By.XPATH, f"//div[@data-convention-label='{element_text}']").find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)
                print_log(f"{element_text} '{input_text}' entered")
                wait(1)
            if span_or_label == 'span':
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, f"//div[span[text()='{element_text}']]")))
                driver.find_element(By.XPATH, f"//div[span[text()='{element_text}']]").find_element(By.TAG_NAME, "input").send_keys(Keys.BACKSPACE)
                driver.find_element(By.XPATH, f"//div[span[text()='{element_text}']]").find_element(By.TAG_NAME, "input").send_keys(Keys.BACKSPACE)
                driver.find_element(By.XPATH, f"//div[span[text()='{element_text}']]").find_element(By.TAG_NAME, "input").send_keys(input_text)
                driver.find_element(By.XPATH, f"//div[span[text()='{element_text}']]").find_element(By.TAG_NAME, "input").send_keys(Keys.ENTER)
                print_log(f"{element_text} '{input_text}' entered")
                wait(1)
        except:
            print_log(f"Failed to enter '{input_text}' in '{element_text}'")
            # print(custom_traceback(traceback.format_exc()))


def wait_for_captcha_to_solved_cloudflare(driver):
    cloudflare_appear_flag = False
    if "verify you are human" in driver.page_source.lower() or 'review the security of your connection before proceeding.' in driver.page_source.lower():
        print_log(f"Cloudflare appears, Waiting for it to solve")
        cloudflare_appear_flag = True

    while "verify you are human" in driver.page_source.lower() or 'review the security of your connection before proceeding.' in driver.page_source.lower():
        pass

    if cloudflare_appear_flag:
        if "verify you are human" not in driver.page_source.lower() or 'review the security of your connection before proceeding.' not in driver.page_source.lower():
            print_log(f"Cloudflare solved.")


def hold_the_ticket(driver, date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, url, time_list, time_to_refresh_the_page):
    if url[-1] == '/':
        url_with_date = f"{url}?t={date_to_book}"
    else:
        url_with_date = f"{url}/?t={date_to_book}"

    selected_time = ""
    print_log(f"Opening '{url_with_date}'")
    driver.get(url_with_date)
    wait_for_captcha_to_solved_cloudflare(driver)

    if time_to_refresh_the_page != "":
        time_to_refresh_the_page_func(time_to_refresh_the_page)
        print_log(f"Opening '{url_with_date}'")
        driver.get(url_with_date)
        wait_for_captcha_to_solved_cloudflare(driver)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "abc-slotpicker-group")))
    driver.execute_script("window.scrollBy(0, 2500);")
    wait(2)
    driver.execute_script("window.scrollBy(2501, 5000);")
    for inner_label in driver.find_element(By.CLASS_NAME, "abc-slotpicker-group").find_elements(By.TAG_NAME, "label"):
        if inner_label.get_attribute('class') != 'unselectable':
            if inner_label.text.strip() in time_list:
                selected_time = inner_label.text.strip()
                print_log(f"Selecting time '{selected_time}'")
                inner_label.click()
                print_log(f"Time '{selected_time}' Selected")
                break

    if selected_time != "":
        input_tickets(driver, 'Full price', full_price, 'span')
        if r_f_rap_mic_card != '' or r_f_rap_museo_ebraico_roma != '' or r_f_rap_villa_farnesina != '':
            driver.find_element(By.XPATH, f"//div[span[text()='Reduced fare (R.A.P.)']]").find_element(By.CLASS_NAME, "shrink-button").click()
            print_log("Clicked on 'Choose' for 'Reduced fare (R.A.P.)'")
            input_tickets(driver, 'Mic Card', r_f_rap_mic_card, 'label')
            input_tickets(driver, 'Museo ebraico Roma', r_f_rap_museo_ebraico_roma, 'label')
            input_tickets(driver, 'Villa Farnesina', r_f_rap_villa_farnesina, 'label')
        input_tickets(driver, 'Reduced fare', reduced_fair, 'span')
        input_tickets(driver, 'Free (Roma Pass)', free_roma_pass, 'span')
        driver.execute_script("window.scrollBy(0, 1800);")
        if any((f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects)):
            driver.find_element(By.XPATH, f"//div[span[text()='Free according to regulation']]").find_element(By.CLASS_NAME, "shrink-button").click()
            print_log("Clicked on 'Choose' for 'Free according to regulation'")
            input_tickets(driver, 'Disabled person', f_a_t_r_disabled_person, 'label')
            input_tickets(driver, 'Person accompanying the disabled person', f_a_t_r_person_accompanying_the_disabled_person, 'label')
            input_tickets(driver, 'Italian teacher with MIUR module', f_a_t_r_italian_teacher_with_miur_module, 'label')
            input_tickets(driver, 'Fine Arts teacher-student', f_a_t_r_fine_arts_teacher_sutdent, 'label')
            input_tickets(driver, 'Cultural Heritage teacher-student', f_a_t_r_cultural_heritage_teacher_student, 'label')
            input_tickets(driver, 'Journalist', f_a_t_r_journalist, 'label')
            input_tickets(driver, 'Tourist interpreter', f_a_t_r_tourist_interpreter, 'label')
            input_tickets(driver, 'ICCROM member', f_a_t_r_iccrom_member, 'label')
            input_tickets(driver, 'ICOM Members (Individual)', f_a_t_r_icom_members_individual, 'label')
            input_tickets(driver, 'Ministry of culture staff', f_a_t_r_ministry_of_culture_staff, 'label')
            input_tickets(driver, 'EU teachers attested cultural subjects', f_a_t_r_eu_teachers_attested_cultural_subjects, 'label')
        input_tickets(driver, 'Free admission Under18 according to regulation', free_addition_under_18, 'span')
        driver.execute_script("window.scrollBy(0, 1800);")
        if group_leader != '' or guide_pass != '' or tour_guide != '':
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "tariff-category-button")))
            if 'collapsed' in driver.find_element(By.CLASS_NAME, "tariff-category-button").get_attribute('class'):
                driver.find_element(By.CLASS_NAME, "tariff-category-button").click()
                print_log(f"Clicked on 'Group carrier' tab")
            input_tickets(driver, 'Guide Pass', guide_pass, 'span')
            input_tickets(driver, 'Group leader', group_leader, 'span')
            input_tickets(driver, 'Tourist guide', tour_guide, 'span')
    else:
        print_log(f"There's no time slot available for '{time_list[0]} - {time_list[-1]}'")


def main(date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, api_key, url, time_list, time_to_refresh_the_page):
    driver = load_driver()
    print_log("Browser open")

    print_log(f"Starting screen recording script...")
    recording_script_path = os.path.join(os.getcwd(), 'screen_recording_script.py')
    try:
        if sys.platform.startswith('win'):
            subprocess.Popen(['python', recording_script_path])
        elif sys.platform == 'darwin':
            subprocess.Popen(['python3', recording_script_path])
    except:
        print_log("Failed to open 'screen_recording_script.py'.")
        print_log(traceback.format_exc())

    print_log("Adding API Key in CapMonst Extension")
    add_extenstion_api_key(driver, api_key)
    print_log(f"API Key Entered successfully")

    while True:
        try:
            hold_the_ticket(driver, date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, url, time_list, time_to_refresh_the_page)
            wait(5)
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'partial-cart')))
            if driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text != '':
                print_log(f"Ticket has been hold for '15 minutes', Press CTRL+C or COMMAND+C to stop the loop.")
                while driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text != '':
                    try:
                        temp_expiration_time = driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text
                        if temp_expiration_time == '01:00':
                            print_log(f"Expiration time '{temp_expiration_time} minutes', Press CTRL+C or COMMAND+C to stop the loop.")
                            wait(60)
                            break
                        elif temp_expiration_time.split(':')[1] == '00':
                            print_log(f"Expiration time '{temp_expiration_time} minutes', Press CTRL+C or COMMAND+C to stop the loop.")
                            wait(2)

                    except:
                        pass
        except KeyboardInterrupt:
            print_log("Loop interrupted by keyboard")
            break
        except:
            print_log(custom_traceback(traceback.format_exc()))
            driver.quit()
            print_log("Browser closed, Due to error.")

            driver = load_driver()
            print_log("Browser open")

            print_log("Adding API Key in CapMonst Extension")
            add_extenstion_api_key(driver, api_key)
            print_log(f"API Key Entered successfully")

    wait(1000000)
    # print_log("Browser will be closed in 2 minutes. Meanwhile you may check the site and booking detail on club's page.")
    # wait(120)
    # driver.quit()


def start_bot():
    time_to_start_the_bot = input("Enter time to start the bot eg.23:59:50 OR press ENTER to run bot now: ")
    time_to_refresh_the_page = input("Enter time refresh page eg. HH:MM:SS : ")
    if time_to_refresh_the_page != "":
        time_to_refresh_the_page = datetime.strptime(time_to_refresh_the_page, "%H:%M:%S").time()

    date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, api_key, url, time_list = get_data()
    print_log(f"You've entered parameters: Date '{date_to_book}' - Time '{start_time_input}-{end_time_input}' - Full Price '{full_price}'")

    if len(time_to_start_the_bot) == 8:
        print_log(f"Bot is waiting for '{time_to_start_the_bot}' to start the bot")

        def start():
            print_log("Bot is running...")
            main(date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, api_key, url, time_list, time_to_refresh_the_page)
            print_log("Bot stopped.")

        schedule.every().day.at(time_to_start_the_bot).do(start)

        while True:
            schedule.run_pending()
            wait(1)
    else:
        print_log("Bot is running...")
        main(date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, api_key, url, time_list, time_to_refresh_the_page)
        print_log("Bot stopped.")


if __name__ == '__main__':
    start_bot()

