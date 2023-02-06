import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    # 2/5/2023 - V
    # Width, height
    def get_width(self):
        if 'width' not in self.data.keys():
            raise Exception("Width option is not present in the config file")
        return self.data['width']

    def get_height(self):
        if 'height' not in self.data.keys():
            raise Exception("Height option is not present in the config file")
        return self.data['height']

    def get_user1_email(self):
        if 'email' not in self.data.keys():
            raise Exception("email option is not found in user1 section")
        return self.data['email']

    def get_user1_password(self):
        if 'password' not in self.data.keys():
            raise Exception("password option is not found in user1 section")
        return self.data['password']

    def get_url(self):
        if 'url' not in self.data.keys():
            raise Exception("URL option is not present in the config file")
        return self.data['url']
