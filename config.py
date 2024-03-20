class Config:
    SECRET_KEY="$b`8}TCrd;!Dd$'+:LY8^+O0Z**HlzlhqHoA>8ZqbKNKUWJ?{U"

class DevelopmentConfig(Config):
    DEBUG=True


configuration = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}