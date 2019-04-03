import json

class SettingsManager(object):
    def __init__(self):
        self.config = {}
        self.refresh()

    def refresh(self):
        try:
            script_json = open("src\server\settings.json", "r")
            self.config = json.load(script_json)
            return 0
        except Exception:
            return 500
    
    def getConfig(self):
        return self.config

settingManager = SettingsManager()