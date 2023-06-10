from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#gọi trình duyệt Chrome và url cần kiểm
driver = webdriver.Chrome()
url ="https://thetestingworld.com/testings/"
driver.get(url)
# tối đa cửa sổ trình duyệt
driver.maximize_window()
time.sleep(2)

# điền tên
username = driver.find_element(By.NAME, "fld_username")
username.send_keys("demo02")
time.sleep(1)

# điền email
email = driver.find_element(By.NAME, "fld_email")
email.send_keys("demo02@gmail.com")
time.sleep(1)

# điền pass
password = driver.find_element(By.NAME, "fld_password")
password.send_keys("demo012345")
time.sleep(1)

# confirm email
c_password = driver.find_element(By.NAME, "fld_cpassword")
c_password.send_keys("demo012345")
time.sleep(1)

# chọn dob
dob = driver.find_element(By.NAME, "dob")
dob.send_keys("06/27/1990")
dob.send_keys(Keys.ENTER)
time.sleep(1)

# điền phone
phone = driver.find_element(By.NAME, "phone")
phone.send_keys("09111111111")
time.sleep(1)

# diền address
address = driver.find_element(By.NAME, "address")
address.send_keys("ABC Street, CDF Great Hall")
time.sleep(1)

# chọn loại addres
address_type = driver.find_element(By.CSS_SELECTOR,"form[name='register'] > input:nth-of-type(9)")
address_type.click()
time.sleep(1)

# chọn gender
gender = driver.find_element(By.CSS_SELECTOR, "[name='sex']")
gender_object = Select(gender)
gender_object.select_by_value("2")
time.sleep(3)

# chọn country
country = driver.find_element("id", "countryId")
country_object = Select(country)
country_object.select_by_index("20")
time.sleep(5)

# in list country
print("Your country list is: ")
print("**********************")
all_options = country_object.options
for index,option in enumerate(all_options):
    row =f"{index}-{option.text}"
    print(row)
print("**********************")


# chọn state
state = driver.find_element("id", "stateId")
state_object = Select(state)
state_object.select_by_value("415")
time.sleep(5)

# điền zipcode
zipcode = driver.find_element(By.NAME, "zip")
zipcode.send_keys("64009222")
time.sleep(1)

#scroll xuống dưới
driver.find_element(By.NAME, "zip").send_keys(Keys.CONTROL)
driver.find_element(By.NAME, "zip").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# chọn đồng ý term
term_box = driver.find_element(By.NAME, "terms")
term_box.click()
time.sleep(1)

# nhân nút signup
signup_btn = driver.find_element(By.CSS_SELECTOR, "input[value='Sign up']")
signup_btn.click()
time.sleep(5)