from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from myInfo import secrets


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
addExperienceButton = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[2]/div[1]/div/div/div/button')
addExperienceButton.click()
time.sleep(2)

typeIntoBox('//*[@id="input-19"]', 'Software Engineering Intern')
typeIntoBox('//*[@id="input-20"]', 'The Walt Disney Company')
currentlyWorkHereBox = driver.find_element(By.XPATH, '//*[@id="input-21"]')
currentlyWorkHereBox.click()
# time.sleep(20)
typeIntoBox('//*[@id="input-24-dateSectionMonth-input"]', '05')
typeIntoBox('//*[@id="input-24-dateSectionYear-input"]', '2023')
typeIntoBox('//*[@id="input-28"]', "Designing a new website in Angular to replace the outdated Microsoft Sharepoint website for the Minnie Van Team. "
"The new site serves as a platform for managing Minnie Van Cast Members, scheduling Minnie Van Rides for Guests, and managing PII from Guests. "
"Assisted with the development of RESTful services in Java for SQL databases containing Minnie Van and Cast Member information.")


#click 'Add Another' button
addExperienceButton = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[3]/div[2]/div[1]/div/div/div/button')
addExperienceButton.click()
time.sleep(2)
#job title
typeIntoBox('(//input[@class="css-ilrio6"])[4]', 'Software Engineering Intern')
#company
typeIntoBox('(//input[@class="css-ilrio6"])[5]', 'The Walt Disney Company')
#currently work here?
# currentlyWorkHereBox = driver.find_element(By.XPATH, '//*[@id="input-50"]')
# currentlyWorkHereBox.click()
# time.sleep(20)
#startdate
typeIntoBox('(//input[@class="css-72im0m"])[3]', '05')
typeIntoBox('(//input[@class="css-72im0m"])[4]', '2022')

#end date
typeIntoBox('(//input[@class="css-72im0m"])[5]', '08')
typeIntoBox('(//input[@class="css-72im0m"])[6]', '2022')

#role description
typeIntoBox('(//textarea[@class="css-z4c8uq"])[2]', "Created a proof of concept app leveraging Flutter to build iOS native and web applications to integrate various Ticketing functionalities for the Entitlement team. "
"Cooperated on forming a GitHub Build Action Pipeline for all future Flutter apps in the company with AppCenter. "
"Integrated various widgets and RESTful services to highlight Flutter's capabilities.")






time.sleep(100)






