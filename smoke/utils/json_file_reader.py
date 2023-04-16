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

    def get_remote_username(self):
        if 'remote_username' not in self.data.keys():
            raise Exception("Remote username is not present in the config file")
        return self.data['remote_username']

    def get_remote_access_key(self):
        if 'remote_access_key' not in self.data.keys():
            raise Exception("Remote access key is not present in the config file")
        return self.data['remote_access_key']

    def get_desired_cap(self):
        if 'desired_capabilities' not in self.data.keys():
            raise Exception("Desired cap is not present in the config file")
        return self.data['desired_capabilities']

    def get_search_request(self):
        if 'search_request' not in self.data.keys():
            raise Exception("Search request is not present in the config file")
        return self.data['search_request']

    def get_video_name(self):
        if 'video_name' not in self.data.keys():
            raise Exception("Video name is not present in the config file")
        return self.data['video_name']
