from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)

# driver.get('https://www.google.com/')
driver.get('http://www.tsetmc.com/Loader.aspx?ParTree=15131F')
######
# searchbox = driver.find_element_by_class_name('gLFyf')
# # searchbox = driver.find_element_by_xpath("/html/body/div/div[5]/form/div[2]/div[1]/div[1]/div/div[2]/input")
# searchbox.send_keys("python")
# searchbox.send_keys(Keys.ENTER)
#
#
# searchbox = driver.find_element_by_class_name('r').find_elements_by_tag_name("a")
#
# s = searchbox[0]
# s.get_attribute('href')
#
# print(s.get_attribute('href'))
#######
# for i in searchbox:
#     print(i)
# results = \
# driver.find_element_by_xpath("/html/body/div[8]").find_element_by_id("cnt").find_elements_by_class_name("mw")[
#     1].find_element_by_id("rcnt").find_element_by_id("center_col").find_element_by_id("rso")
# titels = results.find_elements_by_class_name("bkWMgd")
# for i in titels:
#     gclass = i.find_elements_by_class_name("g")
#     if gclass != 0:
#         for subclass in gclass:
#             rclass = subclass.find_elements_by_class_name("r")
#             if rclass != 0:
#                 for subclass2 in rclass:
#                     atag = subclass2.find_elements_by_tag_name("a")[0]
#                     if atag.find_elements_by_class_name("LC20lb") != 0:
#                         for finalresult in atag.find_elements_by_class_name("LC20lb"):
#                             nfr = finalresult.find_element_by_class_name("S3Uucc")
#                             print(atag.get_attribute('href'))
#                             print(nfr.get_attribute('innerHTML'))




