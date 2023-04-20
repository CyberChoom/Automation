import time
from selenium.webdriver.common.by import By
from smoke.utils.remote_config_reader import RemoteConfigReader
from smoke.webelements.browser import Browser
from smoke.webelements.UIElement import UIElement as Element

# Using Config Reader
configs = RemoteConfigReader("config.json")
browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time(), configs.get_remote_username(),
                  configs.get_remote_access_key(), configs.get_desired_cap())
driver = browser.get_driver()
driver.maximize_window()

# Inputting search request and launching search
search_field = Element(browser, By.XPATH, "//input[@id='search']")
search_field.enter_text(configs.get_search_request())
search_field.submit()

# Opening the chosen video
chosen_video = Element(browser, By.XPATH, f"//yt-formatted-string[contains(.,'{configs.get_video_name()}')]")
chosen_video.click()

# Confirming the video is playing
video_player = Element(browser, By.XPATH, "//div[@id='movie_player']").get_attribute("class")
print(video_player)
assert "playing-mode" in video_player

# Waiting for the ads section to finish
while "ad-interrupting" in Element(browser, By.XPATH, "//div[@id='movie_player']").get_attribute("class"):
    time.sleep(5)
else:
    print("Ads finished")

# Total duration of the video
duration = Element(browser, By.CSS_SELECTOR, ".ytp-progress-bar").get_attribute_until_present("aria-valuemax")
print(duration)

# Setting play time to 1/3
time_needed = int(duration)/3
print(time_needed)
driver.execute_script(f'document.getElementsByTagName("video")[0].currentTime={str(time_needed)}')
time.sleep(5)

# Verifying the video continues to play
assert "playing-mode" in Element(browser, By.XPATH, "//div[@id='movie_player']").get_attribute("class")
print("Success")

# Marking a session as Passed or Failed via the REST API
if "playing-mode" in Element(browser, By.XPATH, "//div[@id='movie_player']").get_attribute("class"):
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": '
                          '{"status":"passed", "reason": "Verification passed"}}')
else:
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": '
                          '{"status":"failed", "reason": "Verification failed"}}')

browser.shutdown()
