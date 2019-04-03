import json

class SettingsManager(object):
    def __init__(self):
        self.settings = {}
        self.refresh()

    def refresh(self):
        try:
            script_json = open("src/server/settings.json", "r")
            self.settings = json.load(script_json)
            return 0
        except Exception:
            return 500
    
    def getSettings(self):
        return self.settings

settingsManager = SettingsManager()