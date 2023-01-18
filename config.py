from decouple import config
class Config():
    SECRET_KEY=config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('PGSQLUSER')}:{config('PGSQLPASSWORD')}@{config('PGSQLHOST2')}/{config('PGSQLDATABASE')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config={
    'development':DevelopmentConfig
}