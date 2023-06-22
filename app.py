from server import init_app
#from server.appConfig import config_dict

app = init_app(__name__, ver=5.9)


if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
    

