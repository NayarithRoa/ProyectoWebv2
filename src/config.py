class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_DATABASE_HOST ='localhost'
    MYSQL_DATABASE_USER ='root'
    MYSQL_DATABASE_DB='seguimientousuarios' 
    MYSQL_DATABASE_PORT=3306

config = {
    'development': DevelopmentConfig
}