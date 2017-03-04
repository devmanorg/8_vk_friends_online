import vk
import getpass

APP_ID = 5827034


def get_user_login():
    login = getpass.getpass("Write your VK.com login: ")
    assert login, 'No login'
    return login


def get_user_password():
    password = getpass.getpass("Write your VK.com password: ")
    assert password, 'No password'
    return password


def make_vk_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    vk_api = vk.API(session)
    return vk_api


def get_online_friends(vk_api):
    online_friends = vk_api.friends.getOnline()
    online_friends_data = vk_api.users.get(user_ids=online_friends)

    return [(name['first_name'], name['last_name']) for name in online_friends_data]


def output_friends_to_console(friends_online):
    print("Друзья онлайн: \n")
    for friend in friends_online:
        print("%s %s" % (friend[0], friend[1]))


if __name__ == '__main__':
    my_login = get_user_login()
    my_password = get_user_password()
    my_vk_api = make_vk_session(my_login, my_password)
    my_friends_online = get_online_friends(my_vk_api)
    output_friends_to_console(my_friends_online)
