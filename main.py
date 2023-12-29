import ISD_api as isd
import utilities as utils
import line_notify_api as line

config = utils.read_config()


def function_info():
    # if you want to send a message, use this line
    line.send_message("")
    # if you want to use ISD api, use this line
    isd.ISD_api_function(isd.notification_url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Start")
