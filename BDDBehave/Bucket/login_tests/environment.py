from BDDBehave.utils.remote_config_reader import RemoteConfigReader
from BDDBehave.webelements.browser import Browser


def before_all(context):
    configs = RemoteConfigReader("C:/Users/user/Desktop/Automation/BDDBehave/Bucket/login_tests/steps/config.json")
    context.configs = configs


def before_scenario(context, scenario):
    configs = context.configs
    browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time(), configs.get_remote_username(),
                      configs.get_remote_access_key(), configs.get_desired_cap())
    context.browser = browser


def after_scenario(context, scenario):
    context.browser.shutdown()
