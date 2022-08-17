from behave import given, when, then

from utils.config_reader import ConfigReader
from webelements.browser import Browser
from pages.add_music_page import MusicPage


URL = "http://18.212.223.46:3000/"
configs = ConfigReader("")

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


@given("user is logged in")
def verify_user_logged_in(context):
    """browser = Browser(URL, "firefox")
    music_page = MusicPage(browser)
    context.browser = browser
    context.music_page = music_page"""
    music_page.click_sign_in_menu()
    print()


@given("user launched the 'Add Music Product' page")
def launch_music_page(context):
    print()


@when("user enters <artist_name>")
def artist_name(context):
    print()


@when("<album_name>")
def album_name(context):
    print()


@when("<format>")
def music_format(context):
    print()


@when("<quantity>")
def quantity(context):
    print()


@when("<media_condition>")
def media_condition(context):
    print()


@when("<sleeve_condition>")
def sleeve_condition(context):
    print()


@when("<opening_price>")
def opening_price(context):
    print()


@when("<asking_price>")
def asking_price(context):
    print()


@when("clicks the 'Add Product' button")
def add_product(context):
    print()


@then("the Music Product is added")
def result(context):
    print()
