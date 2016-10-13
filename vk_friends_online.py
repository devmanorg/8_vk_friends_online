import vk
import getpass

APP_ID = 5302596  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass.getpass('Password:')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    print(api)
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    pass

if __name__ == '__main__':

    login = get_user_login()
    password = get_user_password()

    login = '375297722502'
    password = '754816f6280dd1f97bb22c8925d662a3'


    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
