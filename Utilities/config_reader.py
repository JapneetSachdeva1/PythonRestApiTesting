from configparser import ConfigParser

from from_root import from_root

config_file_path = from_root('config.ini')
def readConfig(section, key):
    config = ConfigParser()
    config.read(config_file_path)
    return config.get(section, key)


#print(readConfig("endpoint", "url"))
print("path: "+str(config_file_path))
