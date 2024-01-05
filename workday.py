from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from myInfo import secrets, experiences


driver = webdriver.Chrome()

# Clear browsing data
# driver.execute_script("window.localStorage.clear();")
driver.get("https://boeing.wd1.myworkdayjobs.com/en-US/EXTERNAL_CAREERS/job/USA---Herndon-VA/Front-End-UI-Software-Developer--Associate-Experienced-_00000407669-2/apply/applyManually")
driver.delete_all_cookies()


wait = WebDriverWait(driver, 10)

def waitForLoad(xpath):
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH,xpath)))
    except:
        print("page couldn't load")


def typeIntoBox(xpath, value):
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(value)

def selectFromDropdown(xpath, n):
    dropdown = driver.find_element(By.XPATH,xpath)
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'nearest'});", dropdown)
    dropdown.click()
    actions = ActionChains(driver)

    #create action chain to automate arrow down to select appropriate dropdown option
    for _ in range(n):
        actions = actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(0.01)
    actions.send_keys(Keys.ENTER)
    actions.perform()

def addWorkExperience(details):
    i = 1
    for experience_key, experience_details in details.items():
        addExperienceButton = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[2]/div[1]/div/div/div/button')
        addExperienceButton.click()
        time.sleep(2)
        experience_number = int(experience_key[-1])
        input_index = (experience_number-1) *3 + 1
        typeIntoBox(f'(//input[@class="css-ilrio6"])[{input_index}]', experience_details['job_title'])
        typeIntoBox(f'(//input[@class="css-ilrio6"])[{input_index + 1}]', experience_details['company'])
        typeIntoBox(f'(//input[@class="css-ilrio6"])[{input_index + 2}]', experience_details['location'])

        if (experience_details['currently_working_here']):
            currentlyWorkHereBox = driver.find_element(By.XPATH, f'(//*[@class="css-1rmmx2s"])[{experience_number}]')
            currentlyWorkHereBox.click()
            # time.sleep(20)
            typeIntoBox(f'(//input[@class="css-72im0m"])[{i}]', experience_details['start_month'])
            i+=1
            typeIntoBox(f'(//input[@class="css-72im0m"])[{i}]', experience_details['start_year'])
            i+=1
        else:
            typeIntoBox(f'(//input[@class="css-72im0m"])[{i}]', experience_details['start_month'])
            i+=1
            typeIntoBox(f'(//input[@class="css-72im0m"])[{i}]', experience_details['start_year'])
            i+=1
            typeIntoBox(f'(//input[@class="css-72im0m"])[{i}]', experience_details['end_month'])
            i+=1
            typeIntoBox(f'(//input[@class="css-72im0m"])[{i}]', experience_details['end_year'])
            i+=1
        typeIntoBox(f'(//textarea[@class="css-z4c8uq"])[{experience_number}]',experience_details['role_description'])

waitForLoad('//*[@id="input-4"]')
#accessing username and password html elements
typeIntoBox('//*[@id="input-4"]', secrets['username'])
typeIntoBox('//*[@id="input-5"]', secrets['password'])
time.sleep(0.1)

#pressing the signin button on the workday page
signin = driver.find_element(By.XPATH,'//*[@id="wd-Authentication-NO_METADATA_ID-uid6"]/div/div[1]/div/form/div[3]/div/div/div/div/div')
signin.click()
time.sleep(0.25)
signin.click()

# signin.send_keys(Keys.ENTER)
# time.sleep(10)


#----------- MY INFORMATION -------------#
waitForLoad('//*[@id="input-1"]')
# while (driver.find_element(By.XPATH, '//*[@id="input-1"]').text != 'Other'):
#     selectFromDropdown('//*[@id="input-1"]', 1)
#     time.sleep(0.5)


# priorEmployee = driver.find_element(By.XPATH,'//*[@id="input-2"]/div[2]/div')
# priorEmployee.click()
# typeIntoBox('//*[@id="input-4"]', 'Dmitri')
# typeIntoBox('//*[@id="input-5"]', 'Morales')
# typeIntoBox('//*[@id="input-6"]', '13951 SW 75 ST')
# typeIntoBox('//*[@id="input-7"]', 'Miami')
# time.sleep(0.1)
# while (driver.find_element(By.XPATH, '//*[@id="input-8"]').text != 'Florida'):
#     selectFromDropdown('//*[@id="input-8"]', 1)
#     time.sleep(0.5)

# typeIntoBox('//*[@id="input-9"]', '33183')

# while (driver.find_element(By.XPATH, '//*[@id="input-11"]').text != 'Mobile'):
#     selectFromDropdown('//*[@id="input-11"]', 1)
#     time.sleep(0.3)

# typeIntoBox('//*[@id="input-13"]', '3059424152')

nextButton = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[5]/div/ul/div/div/div/button')
nextButton.click()


#------------ MY EXPERIENCE ---------------#
waitForLoad('//*[@id="mainContent"]/div/div[3]/div[2]/div[1]/div/div/div/button')
addWorkExperience(experiences)


time.sleep(100)






