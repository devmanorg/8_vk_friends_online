import vk
import getpass

APP_ID = -1


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass.getpass('Password:')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_online_id = api.friends.getOnline()
    friends_online_id_str = ','.join([str(i) for i in friends_online_id])
    friends_online = api.users.get(
        user_ids=friends_online_id_str,
        fields='first_name, last_name'
    )

    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])

if __name__ == '__main__':

    login = get_user_login()
    password = get_user_password()

    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
