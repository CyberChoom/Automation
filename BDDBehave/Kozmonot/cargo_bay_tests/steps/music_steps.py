from behave import given, when, then
from BDDBehave.utils.remote_config_reader import RemoteConfigReader
from BDDBehave.Kozmonot.pages.login_page import LoginPage
from BDDBehave.Kozmonot.pages.add_music_page import MusicPage


configs = RemoteConfigReader("C:/Users/user/Desktop/Automation/BDDBehave/Kozmonot/cargo_bay_tests/steps/config.json")


""" 
    Given user is logged in
    And user launched the 'Add Music Product' page
    When user enters <artist_name>
    And <album_name>
    And <format>
    And <quantity>
    And <media_condition>
    And <sleeve_condition>
    And <opening_price>
    And <asking_price>
    And clicks the 'Add Product' button
    Then the Music Product is added 
"""


@given('user is logged in')
def verify_user_logged_in(context):
    login_page = LoginPage(context.browser)
    login_page.click_sign_in_menu()
    login_page.enter_email(configs.get_user1_email())
    login_page.enter_password(configs.get_user1_password())
    login_page.sign_in()
    login_page.verify_login()
    context.login_page = login_page


@given('user launched the "Add Music Product" page')
def launch_music_page(context):
    music_page = MusicPage(context.browser)
    music_page.open_music_page()
    context.music_page = music_page


@when('user enters "{artist_name}" in artist name field')
def fill_artist_name(context, artist_name):
    music_page = context.music_page
    if artist_name == "None":
        pass
    else:
        music_page.add_artist_name(artist_name)


@when('"{album_name}" in album name field')
def enter_album_name(context, album_name):
    music_page = context.music_page
    if album_name == "None":
        pass
    else:
        music_page.add_album_name(album_name)


@when('"{format}" in format field')
def enter_music_format(context, format):
    music_page = context.music_page
    if format == "None":
        pass
    else:
        music_page.select_format(format)


@when('"{quantity}" in quantity field')
def enter_music_quantity(context, quantity):
    music_page = context.music_page
    if quantity == "None":
        pass
    else:
        music_page.add_quantity(quantity)


@when('"{media_condition}" in media condition field')
def enter_media_condition(context, media_condition):
    music_page = context.music_page
    if media_condition == "None":
        pass
    else:
        music_page.select_media_condition(media_condition)


@when('"{sleeve_condition}" in sleeve condition field')
def enter_sleeve_condition(context, sleeve_condition):
    music_page = context.music_page
    if sleeve_condition == "None":
        pass
    else:
        music_page.select_sleeve_condition(sleeve_condition)


@when('"{opening_price}" in opening price field')
def enter_opening_price(context, opening_price):
    music_page = context.music_page
    if opening_price == "None":
        pass
    else:
        music_page.add_opening_price(opening_price)


@when('"{asking_price}" in asking price field')
def enter_asking_price(context, asking_price):
    music_page = context.music_page
    if asking_price == "None":
        pass
    else:
        music_page.add_asking_price(asking_price)


@when('clicks the "Add Product" button')
def add_product(context):
    music_page = context.music_page
    music_page.add_product()


@then('the Music Product is added')
def success(context):
    music_page = context.music_page
    music_page.verify_adding_product()


@then('the Music Product is not added, warning message: "This field is required." is shown underneath the empty fields')
def warning(context):
    music_page = context.music_page
    music_page.verify_error()
