import vk_api, json
from vk_api.longpoll import  VkLongPoll, VkEventType
from users import *
import yt




def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }

keyboard = {
    "one_time" : False,
    "buttons" : [
        [get_but('Плейлист', 'positive'), get_but('Добавь', 'positive')],
        [get_but('Повтори', 'positive'), get_but('Команды', 'negative')]

    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))



def send(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message': text, 'random_id': 0, 'dont_parse_links': 0, 'keyboard' : keyboard})


file_name = 'users.txt'

file_help = 'help_file.txt'

def cache_users(my_users):
    with open(file_name, 'w') as file:
        for user_id in my_users:
            file.write(my_users[user_id].cache_user())
            file.write('\n')
        file.close()


def read_cache():
    with open(file_name, 'r') as file:
        result = {}
        for line in file:
            u3 = read_user(line)
            result[u3.get_id()] = u3
        return result


def add_play_list(id, my_users, link, name):
    my_users[id].add_track(link, name)
    return  my_users






if __name__ == '__main__':
    tk = ''
    UserNames = read_cache()

    vk_session = vk_api.VkApi(token=tk)
    longpoll = VkLongPoll(vk_session)

    video_name = ''
    video_counter = 0

    help_file = open(file_help, 'r', encoding='utf-8')
    commands = ''
    for line in help_file:
        commands += line
    help_file.close()


    for event in longpoll.listen():



        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text
                msg_low = msg.lower()
                id = str(event.user_id)

                if not(id in UserNames.keys()):
                    UserNames[id] = USER(id)



                if msg_low.find('включи из плейлиста') == 0:
                    try:
                        track_numbers = [int(i) for i in msg[20:].split(' ')]
                        for i in range(len(track_numbers)):
                            send(id, UserNames[id].get_track(track_numbers[i]))
                            if i > 10:
                                break
                    except:
                        send(id, 'Невозможно включить')


                elif msg_low[:6] == 'включи':
                    try:
                        video_counter = 0
                        video_name = msg[7:]
                        if not(str(id) in UserNames.keys()):
                            print(id)
                            UserNames[id] = USER(id)
                            cache_users(UserNames)
                        send(id, yt.YouTube_request(msg[7:]))

                    except:
                        pass


                if msg_low[:6] == 'добавь':
                    try:
                        if video_name != '':
                            link = yt.YouTube_request(video_name, video_counter)
                            UserNames = add_play_list(id, UserNames, link, video_name)
                            #send(id, UserNames[id].get_name_track())
                        else:
                            send(id, 'Что добавить?')
                    except:
                        pass

                if msg_low[:len('плейлист')] == 'плейлист':
                    send(id, UserNames[id].get_name_track())


                if msg_low[:len('удали номер')] == 'удали номер':
                    try:
                        UserNames[id].del_track(int(msg[len('удали номер')+1:]))

                    except:
                        print('eror number', msg[len('удали номер')+1 :])


                if msg_low == 'повтори' or msg == 'повтори ':
                    if video_name == '':
                        send(id, 'Нет запроса')
                    else:
                        send(id, yt.YouTube_request(video_name, video_counter))


                if msg_low.find('следующ') == 0:
                    try:
                        video_counter += 1
                        send(id, yt.YouTube_request(video_name, video_counter))
                        print(video_counter)
                    except:
                        pass

                if msg_low.find('Команды') == 0:
                    send(id, commands)


                cache_users(UserNames)