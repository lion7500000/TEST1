bs_user = 'lion74'
bs_pw =  'y2HxEGBDfLA2mp9A3nks'
from selenium import webdriver
#import allure
#from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from features.application import Application




def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome()
    #context.driver = webdriver.Safari()
    #context.driver = webdriver.Firefox()

    #### EventFiringWebDriver ####
    #context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())

    ### Browser Stack ###
    #desired_cap = {
    #    'browser': 'Chrome',
    #    'browser_version': '78.0',
    #    'os': 'OS X',
    #    'os_version': 'Catalina',
    #     'name': 'Remoute case Test'
    #}

    #url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    #url = f'http://{bs_user}:{bs_pw}@api.browserstack.com / automate / sessions / < session - id >.json'

    #context.driver = webdriver.Remote( url, desired_capabilities=desired_cap )

    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    context.driver.wait = WebDriverWait(context.driver, 25)
    context.app = Application(context.driver)

    #### HEADLESS ####
    #options = webdriver.ChromeOptions()
    #options.add_argument( 'headless' )
    #context.driver = webdriver.Chrome( chrome_options=options )



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()