import sys
from os.path import exists
import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | Made by KXX (MIT License)        |
# ++--------------------------------++

# input your line_notify_token
line_notify_token: ''

# input your isd_api_token
ISD_api_token: ''

# input your isd_api_username
username: ''

#-------------------------------------

"""
                )
    sys.exit()


def read_config():
    """Read the config file.
    Check if the config file exists, if not, create one.
    If it exists, read the config file and return the configuration as a dictionary.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, creating one by default.\nPlease finish filling config.yml")
        config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            config = {
                'line_notify_token': data.get('line_notify_token'),
                'ISD_api_token': data.get('ISD_api_token'),
                'username': data.get('username'),
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml. Please check if the file is correctly filled.\n"
            "If the problem can't be solved, consider deleting config.yml and restarting the program.\n")
        sys.exit()
