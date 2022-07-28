import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
token = config["settings"]["token"]
admins = config["settings"]["admin_id"]
user = config["database"]["user"]
password = config["database"]["password"]
host = config["database"]["host"]
db = config["database"]["db"]

if "," in admins:
    admins = admins.split(",")
else:
    if len(admins) >= 1:
        admins = [admins]
    else:
        admins = []
        print("***** Вы не указали админ ID *****")
