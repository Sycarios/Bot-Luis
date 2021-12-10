import unittest
import config
class Test_config(unittest.TestCase): #Test if there is something in these variables
    def test_Luis_key(self):
        key=config.DefaultConfig.LUIS_API_KEY
        self.assertTrue(key) 
    def test_Luis_id(self):
        id=config.DefaultConfig.LUIS_APP_ID
        self.assertTrue(id)
    
    def test_Luis_Host_Name(self):
        host=config.DefaultConfig.LUIS_API_HOST_NAME
        self.assertTrue(host)
    
    def test_APPINSIGHTS_INSTRUMENTATION_KEY(self):
        Ikey=config.DefaultConfig.APPINSIGHTS_INSTRUMENTATION_KEY
        self.assertTrue(Ikey)

    def test_APPID(self):
        Appid=config.DefaultConfig.APP_ID
        self.assertTrue(Appid)

    def test_APP_Password(self):
        Apppass=config.DefaultConfig.APP_PASSWORD
        self.assertTrue(Apppass)
    


