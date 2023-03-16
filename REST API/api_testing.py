import requests

APIKEY = "Hidden for Privacy reasons"
TOKEN = "Hidden for Privacy reasons"
url = "https://api.trello.com/"


def create_new_board(name):
    """
    Creates a new board
    :param name: new board name
    :return: None
    """
    endpoint = "1/boards/"
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': name
    }
    response = requests.post(url=url + endpoint, json=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def get_user_boards():
    """
    This function returns information about all the boards that the user has access to
    :return: list of dict
    """
    endpoint = "1/members/me/boards"
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=url + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json


def get_board_id(name):
    """
    Returns the id of the specified board
    :param name: name of the board
    :return: int
    """
    id = None
    response = get_user_boards()
    for board in response:
        if board['name'] == name:
            id = board['id']
            break

    if id is None:
        print("No boards found with the name: {}".format(name))
    return id


def create_new_list(board_name, list_name):
    """
    Creates a new list in the chosen board
    :param board_name: the board to create the new list in
    :param list_name: the new list to be created
    :return: None
    """
    board_id = get_board_id(board_name)
    endpoint = "1/boards/{}/lists".format(board_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': list_name
    }

    response = requests.request(
        "POST",
        url+endpoint,
        params=params
    )

    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def get_lists(board_name):
    """
    This function returns information about all the lists that the user has access to
    :param board_name: name of the board containing the lists
    :return: list of dict
    """
    board_id = get_board_id(board_name)
    endpoint = "1/boards/{}/lists".format(board_id)

    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=url + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json


def get_list_id(board_name, list_name):
    """
    Returns the id of the specified list
    :param board_name: name of the board
    :param list_name: name of the list
    :return: int
    """
    id = None
    response = get_lists(board_name)
    for list in response:
        if list['name'] == list_name:
            id = list['id']
            break

    if id is None:
        print("No lists found with the name: {}".format(list_name))
    return id


def create_new_card_in_list(board_name, list_name, card_name):
    """
    Creates a new card in the chosen list
    :param board_name: the board to create the new card in
    :param list_name: the list to create the new card in
    :param card_name: the new card to be created
    :return: None
    """
    list_id = get_list_id(board_name, list_name)
    endpoint = "1/lists/{}/cards".format(list_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }

    response = requests.request(
        "POST",
        url + endpoint,
        params=params
    )

    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def get_cards_in_list(board_name, list_name):
    """
    This function returns information about all the cards that the user has access to
    :param board_name: name of the board containing the lists
    :param list_name: name of the list containing the cards
    :return: list of dict
    """
    list_id = get_list_id(board_name, list_name)
    endpoint = "1/lists/{}/cards".format(list_id)

    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    response = requests.get(url=url + endpoint, params=params)
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    return response_json


def get_card_id(board_name, list_name, card_name):
    """
    Returns the id of the specified card
    :param board_name: name of the board
    :param list_name: name of the list
    :param card_name: name of the card
    :return: int
    """
    id = None
    response = get_cards_in_list(board_name, list_name)
    for card in response:
        if card['name'] == card_name:
            id = card['id']
            break

    if id is None:
        print("No cards found with the name: {}".format(card_name))
    return id


def update_card(board_name, list_name, card_name, **kwargs):
    """
    Updates card information
    :param board_name: name of the board the card is located in
    :param list_name: name of the list the card is located in
    :param card_name: name of the card to be updated
    :param kwargs: card's parameters to be updated.
    :return: None
    """
    card_id = get_card_id(board_name, list_name, card_name)
    endpoint = "{}1/cards/{}".format(url, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }
    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def delete_card(board_name, list_name, card_name):
    """
    Deletes the card
    :param board_name: name of the board the card is located in
    :param list_name: name of the list the card is located in
    :param card_name: name of the card to be deleted
    :return: None
    """
    card_id = get_card_id(board_name, list_name, card_name)
    endpoint = "{}1/cards/{}".format(url, card_id)
    params = {
        'key': APIKEY,
        'token': TOKEN,
        'name': card_name
    }

    response = requests.request(
        "DELETE",
        endpoint,
        params=params
    )
    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


def archive_list(board_name, list_name, **kwargs):
    """
    Archives the list
    :param board_name: name of the board the list is located in
    :param list_name: name of the list to be archived
    :param kwargs: parameters to confirm archiving of the list. (value - Set to true to close (archive) the list
    :return: None
    """
    list_id = get_list_id(board_name, list_name)
    endpoint = "{}1/lists/{}/closed".format(url, list_id)
    params = {
        'key': APIKEY,
        'token': TOKEN
    }

    for key, value in kwargs.items():
        params[key] = value

    response = requests.request(
        "PUT",
        endpoint,
        params=params
    )

    assert response.status_code == 200
    assert response.reason == "OK"
    assert response.ok
    response_json = response.json()
    print(response_json)


if __name__ == "__main__":
    create_new_board("Automation")
    create_new_list("Automation", "Test List")
    create_new_card_in_list("Automation", "Test List", "Important Card")
    update_card("Automation", "Test List", "Important Card", desc="Advanced automation techniques")
    delete_card("Automation", "Test List", "Important Card")
    archive_list("Automation", "Test List", value="true")
