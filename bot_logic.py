from users import *
import yt
#from main import send

file_name = 'users.txt'


def cache_users(my_users):
    with open(file_name, 'a') as file:
        for k in my_users:
            file.write(str(k))
            file.write(' none')
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
    UserNames = read_cache()

    UserNames = add_play_list('360709031', UserNames, 'http')
    UserNames = add_play_list('360709031', UserNames, 'http')

    for k in UserNames:
        print(k, UserNames[k].playlists)

