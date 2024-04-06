##secret.json ve appsettings.json dosyalarını okuyarak gerekli ayarları döndüren sınıf
import json
import os

class AppSetting:
    
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.secret = None
        self.appsettings = None
        self.load_secret()
        self.load_appsettings()
        current_file_path = os.getcwd()
        print(current_file_path)

    def load_secret(self):
        with open(self.path+'/secret.json') as f:
            self.secret = json.load(f)

    def load_appsettings(self):
        with open(self.path+'/appsettings.json') as f:
            self.appsettings = json.load(f)

    def get_secret(self):
        return self.secret
    
    def get_appsettings(self):
        return self.appsettings
    
    

