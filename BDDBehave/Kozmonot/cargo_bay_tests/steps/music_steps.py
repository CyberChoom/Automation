from behave import given, when, then

from BDDBehave.utils.config_reader import ConfigReader
from BDDBehave.webelements.browser import Browser
from BDDBehave.Kozmonot.pages.login_page import LoginPage
from BDDBehave.Kozmonot.pages.add_music_page import MusicPage


URL = "http://18.212.223.46:3000/"
configs = ConfigReader("C:/Users/user/Desktop/Automation/BDDBehave/Kozmonot/cargo_bay_tests/steps/config.ini")

""" 
    Given user is logged in
    And user launched the 'Add Music Product' page
    When user enters <artist_name>
    * <album_name>
    * <format>
    * <quantity>
    * <media_condition>
    * <sleeve_condition>
    * <opening_price>
    * <asking_price>
    And clicks the 'Add Product' button
    Then the Music Product is added 
"""


@given('user is logged in')
def verify_user_logged_in(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser
    login_page = LoginPage(context.browser)
    login_page.click_sign_in_menu()
    login_page.enter_email(configs.get_user1_email())
    login_page.enter_password(configs.get_user1_password())
    login_page.sign_in()
    login_page.verify_username()
    context.login_page = login_page


@given('user launched the "Add Music Product" page')
def launch_music_page(context):
    music_page = MusicPage(context.browser)
    music_page.open_music_page()
    context.music_page = music_page


@when('user enters "{artist_name}"')
def fill_artist_name(context, artist_name):
    music_page = context.music_page
    if artist_name == "None":
        pass
    else:
        music_page.add_artist_name(context, artist_name)


@when('user enters g "{album_name}" in album_name field')
def enter_album_name(context, album_name):
    music_page = context.music_page
    if album_name == "None":
        pass
    else:
        music_page.add_artist_name(context, album_name)


@when('"{format}" in format field')
def enter_music_format(context, format):
    music_page = context.music_page
    if format == "None":
        pass
    else:
        music_page.select_format(context, format)


@when('"{quantity}" in quantity field')
def enter_music_quantity(context, quantity):
    music_page = context.music_page
    if quantity == "None":
        pass
    else:
        music_page.add_quantity(context, quantity)


@when('"{media_condition}" in media_condition field')
def enter_media_condition(context, media_condition):
    music_page = context.music_page
    if media_condition == "None":
        pass
    else:
        music_page.select_media_condition(context, media_condition)


@when('"{sleeve_condition}" in sleeve_condition field')
def enter_sleeve_condition(context, sleeve_condition):
    music_page = context.music_page
    if sleeve_condition == "None":
        pass
    else:
        music_page.select_sleeve_condition(context, sleeve_condition)


@when('"{opening_price}" in opening_price field')
def enter_opening_price(context, opening_price):
    music_page = context.music_page
    if opening_price == "None":
        pass
    else:
        music_page.add_opening_price(context, opening_price)


@when('"{asking_price}" in asking_price field')
def enter_asking_price(context, asking_price):
    music_page = context.music_page
    if asking_price == "None":
        pass
    else:
        music_page.add_asking_price(context, asking_price)


@when('clicks the "Add Product" button')
def add_product(context):
    music_page = context.music_page
    music_page.add_product(context)


@then('the Music Product is added')
def result(context):
    print("Success")
