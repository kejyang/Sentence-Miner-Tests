from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import *


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""
    #The locator for search box where search string is entered
    locator = 'search-input'

class OriginalSentenceElement(BasePageElement):
    locator = 'originalSentence'

class TransSentenceElement(BasePageElement):
    locator = 'transSentence'

class WordsElement(BasePageElement):
    locator = 'words'

class BasePage(object):
    def __init__(self, driver):
            self.driver = driver

class MainPage(BasePage):
    search_text_element = SearchTextElement()
    def click_create_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.CREATE_SENTENCE_BUTTON)
        element.click()

    def click_search_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click()
    
    def click_example_sentence(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.EXAMPLE_SENTENCE_LINK)
        element.click()

    def get_example_sentence_page(self):
        return "Example sentence for screenshot" in self.driver.page_source

    def is_example_found(self):
        return "Example sentence" in self.driver.page_source
    
    def check_test_sentence(self):
        return "Test Original Sentence" in self.driver.page_source


class SearchPage(BasePage):
    def click_example_sentence(self):
        """Triggers the search"""
        element = self.driver.find_element(*SearchResultsPageLocators.EXAMPLE_SENTENCE)
        element.click()

    def check_test_sentence(self):
        return "Test Original Sentence" in self.driver.page_source
    
    def is_query_Example_found(self):
        return "Example" in self.driver.page_source
    
    def is_example_found(self):
        return "Example sentence" in self.driver.page_source
    
class CreatePage(BasePage):
    original_sentence_element = OriginalSentenceElement()
    trans_sentence_element = TransSentenceElement()
    words_element = WordsElement()
    
    def click_create_sentence_button(self):
        element = self.driver.find_element(*CreateSentencePageLocators.SUBMIT_SENTENCE_BUTTON)
        element.click()