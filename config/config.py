import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
"mongo_connection" : "mongodb://nraboy:password1234@localhost:27017/",
"postgres_connection" : "postgresql+psycopg2://postgres:postgres@localhost:5432/oltp_db"

}
with open("config.ini", 'w') as config_file:
    config.write(config_file)