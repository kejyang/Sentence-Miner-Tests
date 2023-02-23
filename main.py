import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locator import *
import page

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        s = Service(r"C:\Users\kyang\Downloads\geckodriver.exe")
        self.driver = webdriver.Firefox(service = s)
        self.driver.get('http://localhost:3000/')
    
    def test_press_example(self):
        mainPage = page.MainPage(self.driver)
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(MainPageLocators.EXAMPLE_SENTENCE_LINK)
        )
        mainPage.click_example_sentence()
        assert mainPage.get_example_sentence_page()

    def test_create_link(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_create_button() 
        createPage = page.CreatePage(self.driver)
        createPage.original_sentence_element = "Test Original Sentence"
        createPage.trans_sentence_element = "Test Translated Sentence"
        createPage.words_element = "Test words"
        createPage.click_create_sentence_button()
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Test Original Sentence"))
        )
        assert mainPage.check_test_sentence()  

    def test_search_results(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_text_element = "Example"
        mainPage.click_search_button()
        assert mainPage.is_example_found()   

    def tearDown(self):
        pass
        """ self.driver.close()  """

if __name__ == '__main__':
    unittest.main()