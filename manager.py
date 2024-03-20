from flask_script import Manager

from app import create_app


from config import configuration

app = create_app(configuration['development'])



if __name__ == '__main__':
    manager = Manager(app)
    manager.run()