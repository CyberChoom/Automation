from BDDBehave.utils.config_reader import ConfigReader
from BDDBehave.webelements.browser import Browser


def before_all(context):
    configs = ConfigReader("C:/Users/user/Desktop/Automation/BDDBehave/Bucket/login_tests/steps/config.ini")
    context.configs = configs


def before_scenario(context, scenario):
    configs = context.configs
    browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
    context.browser = browser


def after_scenario(context, scenario):
    context.browser.shutdown()
