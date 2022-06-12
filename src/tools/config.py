import json
import os
import shutil


class Config:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        with open('./static/config.json') as f:
            self.config = json.load(f)

        self.isCorrectConfig()

    def save(self):
        with open('./static/config.json', 'w+') as f:
            json.dump(self.config, f)

    def isCorrectConfig(self):
        try:
            assert 'dir' in self.config
            assert 'hj' in self.config
            assert 'gj' in self.config
            assert 'width' in self.config['hj']
            assert 'width' in self.config['gj']
            assert 'height' in self.config['hj']
            assert 'height' in self.config['gj']
        except AssertionError as e:
            print('잘못된 config')
