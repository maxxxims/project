import vk_api
from vk_api.longpoll import  VkLongPoll, VkEventType
from users import *
import yt



def send(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message': text, 'random_id': 0})


file_name = 'users.txt'


def cache_users(my_users):
    with open(file_name, 'a') as file:
        for k in my_users:
            file.write(str(k))
            if my_users[k].get_playlist_size() == 0:
                file.write(' none')
            else:
                file.write(my_users[k].get_name_track())
            file.write('\n')
        file.close()


def read_cache():
    with open(file_name, 'r') as file:
        result = {}
        for k in file:
            k = k[:-1].split(' ')
            usr = USER(k[0])
            for play_list in k:
                if play_list == 'none':
                    break

            result[k[0]] = usr
        return result


def add_play_list(id, my_users, link):
    my_users[id].add_playlist(link)
    return  my_users



def bot_logic(msg):
    if msg[:6] == 'включи':
        if not (id in UserNames):
            UserNames[id] = users.USER(id)
            cache_users(UserNames)
        send(id, yt.YouTube_request(msg[7:]))





if __name__ == '__main__':
    tk = ''
    UserNames = read_cache()
    #print(UserNames.keys(), (str(id) in UserNames.keys()), str(id))

    vk_session = vk_api.VkApi(token=tk)
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                id = str(event.user_id)

                if msg[:6] == 'включи':
                    if not(str(id) in UserNames.keys()):
                        print(id)
                        UserNames[id] = USER(id)
                        cache_users(UserNames)
                    send(id, yt.YouTube_request(msg[7:]))

                if msg[:6] == 'добавь':
                    link = yt.YouTube_request(msg[7:])
                    UserNames = add_play_list(id, UserNames, link)
                    #cache_users(UserNames)
                    send(id, UserNames[id].get_name_track())

