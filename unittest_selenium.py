
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class google_test(unittest.TestCase):
    def setUp(self):
        # create a new chrome session
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

    def test_Google_Search(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("flipkart")
        time.sleep(5)
        self.search_field.submit()
        #list the results
        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        time.sleep(10)
        self.assertGreaterEqual( len(lists), 8)

    def test_Google_job_openings(self):
        #click on about
        abt= self.driver.find_element_by_link_text("About")
        abt.click()
        time.sleep(5)
        #click on careers
        car= self.driver.find_element_by_link_text("Careers")
        #avoid opening in new tab
        clink=car.get_attribute("href")
        self.driver.get(clink)
        time.sleep(5)
        #click on jobs link
        job= self.driver.find_element_by_partial_link_text("Jobs")
        job.click()
        time.sleep(5)
        job= self.driver.find_element_by_partial_link_text("Skip to jobs")
        job.click()
        time.sleep(5)
        joblist=self.driver.find_elements_by_tag_name("h2")
        time.sleep(5)
        self.assertGreaterEqual( len(joblist), 8)

    def test_Google_Search_time(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("flipkart")
        time.sleep(5)
        self.search_field.submit()
        #get search time web element
        time.sleep(5)
        search_time=self.driver.find_element_by_tag_name("nobr")
        #get search time into string
        search_time_str=search_time.text
        #split result by space
        search_time_split=search_time_str.split(" ")
        exact_time=search_time_split[0].replace("(", "")
        self.assertGreaterEqual( 1.0, float(exact_time))

    def tearDown(self):
        #close chrome
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
