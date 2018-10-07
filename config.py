#!/usr/bin/env python3

import configparser


class Config:

    SECTION = 'DEFAULT'

    def __init__(self):
        import github_notifier
        self.config_file_path = github_notifier.APP_PATH + '/config.ini'
        self.configParser = configparser.ConfigParser()
        self.configParser.read(self.config_file_path)

    def get(self, name):
        return self.configParser.get(self.SECTION, name)

    def set(self, name, value):
        self.configParser.set(self.SECTION, name, value)

    def update(self):
        self.configParser.write(open(self.config_file_path, 'w'))
