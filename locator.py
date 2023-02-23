from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    SEARCH_BUTTON = (By.ID, 'search-button')
    CREATE_SENTENCE_BUTTON = (By.ID, 'create-sentence-link')
    EXAMPLE_SENTENCE_LINK = (By.PARTIAL_LINK_TEXT, "Example sentence for screenshot")
    TEST_ORIGINAL_SENTENCE = (By.LINK_TEXT, "Test Original Sentence")

class SearchResultsPageLocators(object):

    """A class for search results locators. All search results locators should
    come here"""

class CreateSentencePageLocators(object):
    SUBMIT_SENTENCE_BUTTON = (By.ID, 'submit-sentence')
    
    """A class for search results locators. All search results locators should
    come here"""

    