from smoke.utils.json_file_reader import JsonFileReader


class RemoteConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self):
        return self.reader.get_browser()

    def get_wait_time(self):
        return self.reader.get_wait_time()

    def get_user1_email(self):
        return self.reader.get_user1_email()

    def get_user1_password(self):
        return self.reader.get_user1_password()

    def get_url(self):
        return self.reader.get_url()

    def get_remote_username(self):
        return self.reader.get_remote_username()

    def get_remote_access_key(self):
        return self.reader.get_remote_access_key()

    def get_desired_cap(self):
        return self.reader.get_desired_cap()

    def get_search_request(self):
        return self.reader.get_search_request()

    def get_video_name(self):
        return self.reader.get_video_name()

