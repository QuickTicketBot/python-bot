# BISMILLAH ARRAHMAN ARRAHEEM
import random
import shutil
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
import os
import subprocess
from selenium.webdriver.chrome.service import Service as ChromeService
import sys
from jafri_chromedriver_installer import installer
import pyautogui
import platform
import pytz
import urllib.parse


def clear_session_data(profile_path):
    session_dirs = [
        "Default/Cache",
        "Default/Code Cache",
        "Default/Service Worker",
        "Default/Session Storage",
        "Default/Local Storage",
        "Default/IndexedDB",
        "Default/Cookies",
        "Default/History",
        "Default/Visited Links",
        "Default/Top Sites",
        # "Default/Preferences",  # optional
    ]
    for rel_path in session_dirs:
        abs_path = os.path.join(profile_path, rel_path)
        try:
            if os.path.isdir(abs_path):
                shutil.rmtree(abs_path)
            elif os.path.isfile(abs_path):
                os.remove(abs_path)
        except Exception as e:
            print(f"Error deleting {abs_path}: {e}")


def load_driver():
    try:
        chrome_profile = f"{os.getcwd()}/chrome_profile"
        clear_session_data(chrome_profile)
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={chrome_profile}")
        # options.add_argument(f'load-extension={os.getcwd()}/CapMonst_extension')
        options.add_argument('--no-sandbox')
        options.add_argument('--log-level=3')
        options.add_argument('--lang=en')
        options.add_argument('start-maximized')
        options.add_argument('lang=en')
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])  # Removes navigator.webdriver flag
        # installer.install_chromedriver()
        driver = webdriver.Chrome(options=options)

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
        time_to_book = data[24].split('==')[1].strip()
        api_key = data[25].split('==')[1]
        url = data[26].split('==')[1]
        time_list = get_time_list(start_time_input, end_time_input)

        return date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, time_to_book, api_key, url, time_list
    except:
        print_log("Error in loading data make sure you've entered data in correct form.")
        print_log(custom_traceback(traceback.format_exc()))


def add_extenstion_api_key(driver, api_key):
    driver.get("chrome-extension://pabjfbciaedomjjfelfafejkppknjleh/popup.html")
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

    for i in range(50):
        driver.find_element(By.ID, "client-key-input").send_keys(Keys.BACKSPACE)
    driver.find_element(By.ID, "client-key-input").send_keys(api_key)
    wait(1)
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

    loop_num = 0
    while "verify you are human" in driver.page_source.lower() or 'review the security of your connection before proceeding.' in driver.page_source.lower():
        loop_num += 1
        wait(0.1)
        if loop_num == 100:
            driver.refresh()
            print_log(f"Page has been refreshed due to cloudflare got stuck.")
            wait(1)
        if 'ERROR_CAPTCHA_UNSOLVABLE' in driver.page_source:
            driver.refresh()
            print_log(f"Page has been refreshed due to ERROR_CAPTCHA_UNSOLVABLE")
            wait(1)

    if cloudflare_appear_flag:
        if "verify you are human" not in driver.page_source.lower() or 'review the security of your connection before proceeding.' not in driver.page_source.lower():
            print_log(f"Cloudflare solved.")


def scroll_to_the_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.3)  # Let scroll finish
    if element.is_displayed():
        print_log("Scrolled and element is visible")
        return


def hold_the_ticket(driver, date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, url, time_list, time_to_book, time_to_refresh_the_page):
    global slot_delete_flag

    time_to_book_encoded = local_time_to_utc_encoded(int(time_to_book.split(' ')[0]), int(time_to_book.split(' ')[1]))
    if url[-1] == '/':
        url_with_date_and_time = f"{url}?t={date_to_book}{time_to_book_encoded}"
    else:
        url_with_date_and_time = f"{url}/?t={date_to_book}{time_to_book_encoded}"

    selected_time = ""
    no_available_slot = False

    if not slot_delete_flag:
        print_log(f"Opening '{url_with_date_and_time}'")
        driver.get(url_with_date_and_time)
        wait_for_captcha_to_solved_cloudflare(driver)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "partial-cart")))
        scroll_to_the_element(driver, driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "slot"))
        if 'select date and time' not in driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "slot").text.lower():
            print_log(f"Time '{time_to_book}' is available")
            selected_time = driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "slot").text.split('at ')[1]
            print_log(f"Time '{selected_time}' Selected via link")
        else:
            print_log(f"Time '{time_to_book}' is not available bot will select time from range.")

        if time_to_refresh_the_page != "":
            time_to_refresh_the_page_func(time_to_refresh_the_page)
            print_log(f"Opening '{url_with_date_and_time}'")
            driver.get(url_with_date_and_time)
            wait_for_captcha_to_solved_cloudflare(driver)
    else:
        selected_time = time_to_book
        print_log(f"Previous time '{selected_time}' is already selected via link")

    if selected_time == "":
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "abc-slotpicker-group")))
        scroll_to_the_element(driver, driver.find_element(By.CLASS_NAME, "abc-slotpicker-group"))
        for inner_label in driver.find_element(By.CLASS_NAME, "abc-slotpicker-group").find_elements(By.TAG_NAME, "label"):
            if inner_label.get_attribute('class') != 'unselectable':
                if 'Available' in inner_label.text.strip():
                    available_slots = inner_label.text.strip().split('Available: ')[1]
                    if int(full_price) <= int(available_slots):
                        temp_selected_time = inner_label.text.strip().split('Available: ')[0]
                        if temp_selected_time in time_list:
                            selected_time = temp_selected_time
                            print_log(f"Selecting time '{selected_time}' from limited availability")
                            scroll_to_the_element(driver, inner_label)
                            inner_label.click()
                            print_log(f"Time '{selected_time}' Selected via limited availability")
                            break
                else:
                    if inner_label.text.strip() in time_list:
                        selected_time = inner_label.text.strip()
                        print_log(f"Selecting time '{selected_time}'")
                        scroll_to_the_element(driver, inner_label)
                        inner_label.click()
                        print_log(f"Time '{selected_time}' Selected")
                        break

    if selected_time != "":
        slot_delete_flag = False
        input_tickets(driver, 'Full price', full_price, 'span')
        if r_f_rap_mic_card != '' or r_f_rap_museo_ebraico_roma != '' or r_f_rap_villa_farnesina != '':
            driver.find_element(By.XPATH, f"//div[span[text()='Reduced fare (R.A.P.)']]").find_element(By.CLASS_NAME, "shrink-button").click()
            print_log("Clicked on 'Choose' for 'Reduced fare (R.A.P.)'")
            input_tickets(driver, 'Mic Card', r_f_rap_mic_card, 'label')
            input_tickets(driver, 'Museo ebraico Roma', r_f_rap_museo_ebraico_roma, 'label')
            input_tickets(driver, 'Villa Farnesina', r_f_rap_villa_farnesina, 'label')
        input_tickets(driver, 'Reduced fare', reduced_fair, 'span')
        input_tickets(driver, 'Free (Roma Pass)', free_roma_pass, 'span')
        if any((f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects)):
            scroll_to_the_element(driver, driver.find_element(By.XPATH, f"//div[span[text()='Free according to regulation']]"))
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
        if group_leader != '' or guide_pass != '' or tour_guide != '':
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "tariff-category-button")))
            scroll_to_the_element(driver, driver.find_element(By.CLASS_NAME, "tariff-category-button"))
            if 'collapsed' in driver.find_element(By.CLASS_NAME, "tariff-category-button").get_attribute('class'):
                driver.find_element(By.CLASS_NAME, "tariff-category-button").click()
                print_log(f"Clicked on 'Group carrier' tab")
            input_tickets(driver, 'Guide Pass', guide_pass, 'span')
            input_tickets(driver, 'Group leader', group_leader, 'span')
            input_tickets(driver, 'Tourist guide', tour_guide, 'span')
    else:
        print_log(f"There's no time slot available for '{time_list[0]} - {time_list[-1]}'")
        no_available_slot = True

    return no_available_slot


def click_on_mid_popup(driver, text):
    if 'update quantity' in text:
        try:
            if "Couldn't update quantity" in driver.find_element(By.CLASS_NAME, "col-reservation").find_element(By.CLASS_NAME, "abc-error").text:
                print_log(f"Alert 'Couldnt update quantity' appeared.")
                driver.find_element(By.CLASS_NAME, "col-reservation").find_element(By.CLASS_NAME, "abc-error").find_element(By.TAG_NAME, "button").click()
                print_log(f"Closed the alert.")
        except:
            pass
    else:
        try:
            driver.find_element(By.XPATH, f"//div[contains(@class, 'abc-error') and .//strong[contains(text(), '{text}')]]")
            print_log(f"Alert '{text}' appeared.")
            driver.find_element(By.XPATH, f"//div[contains(@class, 'abc-error') and .//strong[contains(text(), '{text}')]]").find_element(By.TAG_NAME, "button").click()
            print_log(f"Closed the alert.")
        except:
            pass


def delete_the_cart(driver):
    temp_num = 0
    slot_delete_flag = False
    while temp_num < 10 or not slot_delete_flag:
        temp_num += 1
        try:
            if driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text != "":
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".delete.hide-empty-cart")))
                scroll_to_the_element(driver, driver.find_element(By.CSS_SELECTOR, ".delete.hide-empty-cart"))
                driver.find_element(By.CSS_SELECTOR, ".delete.hide-empty-cart").click()
                print_log(f"Clicked on 'Delete' button")
                wait(1)
                driver.switch_to.alert.accept()
                print_log(f"Popup accepted.")
                wait(3)
                if driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text != "":
                    click_on_mid_popup(driver, "Couldn't update quantity")
                    driver.refresh()
                    print_log(f"Page has been refreshed because slots unable to delete properly")
                    wait_for_captcha_to_solved_cloudflare(driver)
            else:
                slot_delete_flag = True
                click_on_mid_popup(driver, "Cart has expired")
        except:
            wait(1)
            # print_log(custom_traceback(traceback.format_exc()))

    return slot_delete_flag


def local_time_to_utc_encoded(hour: int, minute: int):
    local_tz = pytz.timezone("Europe/Rome")
    local_dt_naive = datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)
    local_dt = local_tz.localize(local_dt_naive)
    utc_dt = local_dt.astimezone(pytz.utc)
    utc_time_str = utc_dt.strftime("T%H:%M:%SZ")

    return urllib.parse.quote(utc_time_str)


def main(date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, time_to_book, api_key, url, time_list, time_to_refresh_the_page):
    global slot_delete_flag
    driver = load_driver()
    print_log("Browser open")

    # print_log(f"Starting screen recording script...")
    # recording_script_path = os.path.join(os.getcwd(), 'screen_recording_script.py')
    # try:
    #     if sys.platform.startswith('win'):
    #         subprocess.Popen(['python', recording_script_path])
    #     elif sys.platform == 'darwin':
    #         subprocess.Popen(['python3', recording_script_path])
    # except:
    #     print_log("Failed to open 'screen_recording_script.py'.")
    #     print_log(traceback.format_exc())
    #
    # print_log("Adding API Key in CapMonst Extension")
    # add_extenstion_api_key(driver, api_key)
    # print_log(f"API Key Entered successfully")

    while True:
        try:
            no_available_slot = hold_the_ticket(driver, date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, url, time_list, time_to_book, time_to_refresh_the_page)
            if not no_available_slot:
                wait(5)
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'partial-cart')))
                if driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text != '':
                    print_log(f"Ticket has been hold for '15 minutes', Press CTRL+C or COMMAND+C to stop the loop.")
                    time_up_flag = False
                    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'expiration-timer')))
                    while driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text != '' or not time_up_flag:
                        try:
                            temp_expiration_time = driver.find_element(By.CLASS_NAME, "partial-cart").find_element(By.CLASS_NAME, "expiration-timer").text
                            if temp_expiration_time == '14:30':
                                time_up_flag = True
                                print_log("TIMES UP!")
                                print_log(f"Expiration time '{temp_expiration_time} minutes', Bot will delete the current selected slot and will reselect it.")
                                slot_delete_flag = delete_the_cart(driver)
                                if slot_delete_flag:
                                    print_log(f"Cart has been deleted successfully.")
                                    break
                            elif temp_expiration_time.split(':')[1] == '00':
                                print_log(f"Expiration time '{temp_expiration_time} minutes', Press CTRL+C or COMMAND+C to stop the loop.")
                                wait(2)
                        except:
                            pass
            # else:
            #     print_log(f"Bot is closing due to there's no slot available for '{time_list[0]} - {time_list[-1]}'")
            #     wait(5)
            #     driver.quit()
            #     print_log(f"Browser closed")
            #     break

        except KeyboardInterrupt:
            print_log("Loop interrupted by keyboard")
            break
        except:
            time_stemp = f"{str(datetime.now()).split('.')[0]}:{str(datetime.now()).split('.')[1][0:2]}".replace(' ', '_').replace('-', '_').replace(':', '_')
            print(time_stemp)
            driver.save_screenshot(f'recordings/{time_stemp}.png')
            print_log(custom_traceback(traceback.format_exc()))
            driver.quit()
            print_log("Browser closed, Due to error.")

            driver = load_driver()
            print_log("Browser open")

            # print_log("Adding API Key in CapMonst Extension")
            # add_extenstion_api_key(driver, api_key)
            # print_log(f"API Key Entered successfully")

    wait(1000000)


def start_bot():
    time_to_start_the_bot = input("Enter time to start the bot eg.23:59:50 OR press ENTER to run bot now: ")
    time_to_refresh_the_page = input("Enter time refresh page eg. HH:MM:SS OR press ENTER: ")
    if time_to_refresh_the_page != "":
        time_to_refresh_the_page = datetime.strptime(time_to_refresh_the_page, "%H:%M:%S").time()

    date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, time_to_book, api_key, url, time_list = get_data()
    print_log(f"You've entered parameters: Date '{date_to_book}' - Time to book '{time_to_book}' - Time range '{start_time_input}-{end_time_input}' - Full Price '{full_price}'")

    if len(time_to_start_the_bot) == 8:
        print_log(f"Bot is waiting for '{time_to_start_the_bot}' to start the bot")

        def start():
            print_log("Bot is running...")
            date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, time_to_book, api_key, url, time_list = get_data()
            main(date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, time_to_book, api_key, url, time_list, time_to_refresh_the_page)
            print_log("Bot stopped.")

        schedule.every().day.at(time_to_start_the_bot).do(start)

        while True:
            schedule.run_pending()
            wait(1)
    else:
        print_log("Bot is running...")
        main(date_to_book, full_price, r_f_rap_mic_card, r_f_rap_museo_ebraico_roma, r_f_rap_villa_farnesina, reduced_fair, free_roma_pass, f_a_t_r_disabled_person, f_a_t_r_person_accompanying_the_disabled_person, f_a_t_r_italian_teacher_with_miur_module, f_a_t_r_fine_arts_teacher_sutdent, f_a_t_r_cultural_heritage_teacher_student, f_a_t_r_journalist, f_a_t_r_tourist_interpreter, f_a_t_r_iccrom_member, f_a_t_r_icom_members_individual, f_a_t_r_ministry_of_culture_staff, f_a_t_r_eu_teachers_attested_cultural_subjects, free_addition_under_18, group_leader, guide_pass, tour_guide, start_time_input, end_time_input, time_to_book, api_key, url, time_list, time_to_refresh_the_page)
        print_log("Bot stopped.")


slot_delete_flag = False

if __name__ == '__main__':
    start_bot()


