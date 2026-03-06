import configparser

config = configparser.ConfigParser()
config.read('config.ini')
config_data = config['DEFAULT']

def get_postgres():
    postgres = config_data['postgres_connection']
    return postgres
def get_mongo():
    mongo = config_data['mongo_connection']
    return mongo