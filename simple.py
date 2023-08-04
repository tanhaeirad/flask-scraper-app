import seleniumwire.undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time
import datetime
from random import randint, random as rd
import json


class SCCourtsScraper():
    def __init__(self, county_name, date) -> None:
        self.date = date
        self.county_name = county_name
        self.counties = {
            "Abbeville": "https://publicindex.sccourts.org/abbeville/publicindex/",
            "Aiken": "https://publicindex.sccourts.org/aiken/publicindex/",
            "Allendale": "https://publicindex.sccourts.org/allendale/publicindex/",
            "Anderson": "https://publicindex.sccourts.org/anderson/publicindex/",
            "Bamberg": "https://publicindex.sccourts.org/bamberg/publicindex/",
            "Barnwell": "https://publicindex.sccourts.org/barnwell/publicindex/",
            "Beaufort": "https://publicindex.sccourts.org/beaufort/publicindex/",
            "Berkeley": "https://publicindex.sccourts.org/berkeley/publicindex/",
            "Calhoun": "https://publicindex.sccourts.org/calhoun/publicindex/",
            "Charleston": "https://jcmsweb.charlestoncounty.org/PublicIndex/",
            "Cherokee": "https://publicindex.sccourts.org/cherokee/publicindex/",
            "Chester": "https://publicindex.sccourts.org/chester/publicindex/",
            "Chesterfield": "https://publicindex.sccourts.org/chesterfield/publicindex/",
            "Clarendon": "https://publicindex.sccourts.org/clarendon/publicindex/",
            "Colleton": "https://publicindex.sccourts.org/colleton/publicindex/",
            "Darlington": "https://publicindex.sccourts.org/darlington/publicindex/",
            "Dillon": "https://publicindex.sccourts.org/dillon/publicindex/",
            "Dorchester": "https://publicindex.sccourts.org/dorchester/publicindex/",
            "Edgefield": "https://publicindex.sccourts.org/edgefield/publicindex/",
            "Fairfield": "https://publicindex.sccourts.org/fairfield/publicindex/",
            "Florence": "https://publicindex.sccourts.org/florence/publicindex/",
            "Georgetown": "https://publicindex.sccourts.org/georgetown/publicindex/",
            "Greenville": "https://www.greenvillecounty.org/scjd/publicindex/Disclaimer.aspx",
            "Greenwood": "https://publicindex.sccourts.org/greenwood/publicindex",
            "Hampton": "https://publicindex.sccourts.org/hampton/publicindex/",
            "Horry": "https://publicindex.sccourts.org/horry/publicindex/",
            "Jasper": "https://publicindex.sccourts.org/jasper/publicindex/",
            "Kershaw": "https://publicindex.sccourts.org/kershaw/publicindex/",
            "Lancaster": "https://publicindex.sccourts.org/lancaster/publicindex/",
            "Laurens": "https://publicindex.sccourts.org/laurens/publicindex/",
            "Lee": "https://publicindex.sccourts.org/lee/publicindex/",
            "Lexington": "https://publicindex.sccourts.org/lexington/publicindex/",
            "Marion": "https://publicindex.sccourts.org/marion/publicindex/",
            "Marlboro": "https://publicindex.sccourts.org/marlboro/publicindex/",
            "McCormick": "https://publicindex.sccourts.org/mccormick/publicindex/",
            "Newberry": "https://publicindex.sccourts.org/newberry/publicindex/",
            "Oconee": "https://publicindex.sccourts.org/oconee/publicindex/",
            "Orangeburg": "https://publicindex.sccourts.org/orangeburg/publicindex/",
            "Pickens": "https://publicindex.sccourts.org/pickens/publicindex/",
            "Richland": "https://publicindex.sccourts.org/Richland/PublicIndex/disclaimer.aspx",
            "Saluda": "https://publicindex.sccourts.org/saluda/publicindex/",
            "Spartanburg": "https://publicindex.sccourts.org/spartanburg/publicindex/",
            "Sumter": "https://publicindex.sccourts.org/sumter/publicindex/",
            "Union": "https://publicindex.sccourts.org/union/publicindex/",
            "Williamsburg": "https://publicindex.sccourts.org/williamsburg/publicindex/",
            "York": "https://publicindex.sccourts.org/york/publicindex/"
        }
        self.setup_driver()

    def setup_driver(self) -> None:
        options = uc.ChromeOptions()
        options.accept_insecure_certs = True
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = "/usr/bin/google-chrome"

        # proxy_server_url = self.get_proxy_url()
        # proxy_options = {
        #     'proxy': {
        #         'http': proxy_server_url,
        #         'https': proxy_server_url
        #     },
        #     # 'headless': False
        # }

        # TODO: where selenium driver is initialized
        self.driver = uc.Chrome(
            executable_path="/usr/bin/chromedriver",
            options=options,
            # seleniumwire_options=proxy_options
        )
        # self.driver.set_window_size(1200, 815)
        # self.driver.implicitly_wait(10)
        # self.wait = WebDriverWait(self.driver, 30)
        # # Get Home Page
        # self.driver.get("https://www.sccourts.org/")
        # self.wait.until(
        #     EC.presence_of_element_located((By.TAG_NAME, "body")))
        # self.random_wait()

    def close_driver(self) -> None:
        self.driver.quit()

    # return a list of case numbers, ie ["2023LP03023", ... ]
    # def get_all_casenums(self) -> list:
    #     county_link = self.counties[self.county_name]
    #     self.navigate_to_county_page(county_link)
    #     self.fill_form()
    #     valid_cases = self.get_valid_cases()
    #     return [case_data[0] for case_data in valid_cases]

    # def get_single_case_data(self, case_number) -> tuple:
    #     county_link = self.counties[self.county_name]
    #     self.navigate_to_county_page(county_link)
    #     self.fill_form()
    #     return self.get_case_data(case_number)

    # def fill_form(self):
    #     # do not fill in case number, gets flagged everytime

    #     # SELECT LIST PARTY TYPE => DEFENDANT
    #     dropdown = self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_DropDownListParties")
    #     select = Select(dropdown)
    #     self.random_wait()
    #     select.select_by_value('D')

    #     # SELECT CASE TYPE => LIS PENDENS
    #     dropdown = self.wait.until(EC.element_to_be_clickable(
    #         (By.ID, 'ContentPlaceHolder1_DropDownListCaseTypes')))
    #     select = Select(dropdown)
    #     self.random_wait()
    #     select.select_by_index(11)

    #     # SELECT DATE TYPE => ACTIONS FILED
    #     dropdown = self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_DropDownListDateFilter")
    #     select = Select(dropdown)
    #     self.random_wait()
    #     select.select_by_value('Actions')

    #     # SELECT DATE
    #     date = self.date
    #     self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_TextBoxDateFrom").click()
    #     self.random_short_wait()

    #     from_date = self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_TextBoxDateFrom")
    #     for character in date:
    #         self.random_short_wait()
    #         from_date.send_keys(character)

    #     self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_TextBoxDateTo").click()

    #     to_date = self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_TextBoxDateTo")
    #     for character in date:
    #         self.random_short_wait()
    #         to_date.send_keys(character)

    #     # SEARCH
    #     self.random_wait(10, 20)
    #     self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_ButtonSearch").click()
    #     self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    #     self.check_for_imperva()

    # # Returns a list of tuples of filtered valid cases, [(case_num, name),...]
    # def get_valid_cases(self) -> list:
    #     # test if records are returned.
    #     try:
    #         table = self.driver.find_element(
    #             By.ID, "ContentPlaceHolder1_SearchResults")
    #     except NoSuchElementException:
    #         return []

    #     rows = table.find_elements(By.CSS_SELECTOR, 'tr')

    #     # list<tuples(case_number, defendant_name)>
    #     valid_cases = []

    #     for tr in rows[1:]:
    #         cells = tr.find_elements(By.CSS_SELECTOR, 'td')
    #         name = cells[0].text
    #         case_num = cells[2].text
    #         if self.is_valid_name(name):
    #             valid_cases.append((case_num, name))

    #     return self.filter_duplicates_by_case_number(valid_cases)

    # # visits case page and returns case data tuple, (casenum, name, address)
    # def get_case_data(self, case_number) -> tuple:
    #     valid_cases = self.get_valid_cases()
    #     case_data = None
    #     for case in valid_cases:
    #         if case[0] == case_number:
    #             case_data = case

    #     self.random_wait()
    #     self.driver.find_element(By.LINK_TEXT, case_number).click()
    #     self.wait.until(EC.presence_of_element_located(
    #         (By.TAG_NAME, "body")))
    #     self.check_for_imperva()
    #     self.driver.find_element(
    #         By.ID, "__tab_ContentPlaceHolder1_TabContainerCaseDetails_TabPanel3").click()
    #     self.random_wait()
    #     address = ""
    #     try:
    #         address = self.driver.find_element(
    #             By.CSS_SELECTOR, "#ContentPlaceHolder1_TabContainerCaseDetails_TabPanel3_LabelPanel3Contents td:nth-child(3)").text
    #     except:
    #         pass

    #     return case_data + (address,)

    # # returns first valid name for a case number
    # def get_case_name(self) -> str:
    #     self.get_valid_cases()
    #     pass

    # def is_valid_name(self, name: str) -> bool:
    #     return ',' in name

    # def random_short_wait(self) -> None:
    #     st = rd() + 0.8
    #     time.sleep(st)

    # def random_wait(self, lower_limit=4, upper_limit=10) -> None:
    #     seconds = randint(lower_limit, upper_limit)
    #     time.sleep(seconds)

    # def filter_duplicates_by_case_number(self, valid_cases) -> list:
    #     seen = set()
    #     result = []

    #     for case in valid_cases:
    #         case_number = case[0]
    #         if case_number not in seen:
    #             seen.add(case_number)
    #             result.append(case)

    #     return result

    # def get_previous_weekday_str(self) -> str:
    #     today = datetime.date.today()
    #     one_day = datetime.timedelta(days=1)

    #     while today.weekday() > 4:
    #         today -= one_day

    #     previous_weekday = today - one_day
    #     return previous_weekday.strftime("%m/%d/%Y")

    # def get_proxy_url(self) -> str:
    #     return "https://spc9ctgrtw:410EmypfHibuyMAf4g@us.smartproxy.com:10000"

    # def navigate_to_county_page(self, county_link) -> None:
    #     self.driver.get(county_link)
    #     self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    #     self.random_wait()
    #     self.driver.find_element(
    #         By.ID, "ContentPlaceHolder1_ButtonAccept").click()
    #     self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # def check_for_imperva(self) -> None:
    #     try:
    #         iframe = self.driver.find_element(
    #             By.ID, "main-iframe")
    #     except:
    #         pass
    #     else:
    #         raise ImpervaException


class ImpervaException(Exception):
    def __init__(self, message):
        self.message = message


# get_case_numbers_handler
def lambda_handler(event, context):
    print(event)
    if 'queryStringParameters' in event:
        query_params = event['queryStringParameters']
        county_name = query_params.get('county_name')
        date = query_params.get('date')

        try:
            scraper = SCCourtsScraper(county_name, date)
            scraper.driver.get("https://www.geeksforgeeks.org")
            title = scraper.driver.title
            scraper.close_driver()
        except Exception as e:
            print("An exception occurred: ", str(e))
            print(f"{county_name} Failed")
            return {
                'statusCode': 500,
                'body': f"Scraper failure, {county_name}",
            }
        else:
            return {
                'statusCode': 200,
                'body': title,
            }
    else:
        return {
            'statusCode': 400,
            'body': 'Bad Request',
        }

# x = lambda_handler({'queryStringParameters': {
#                'county_name': 'Richland', 'date': '07/28/2023'}}, None)

# print(x)
