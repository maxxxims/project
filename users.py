

class USER:
    def __init__(self, id):
        self.playlists = {}
        self.id = id

    def add_playlist(self, link, name='standart_name_of_playlist'):
        if not(name in self.playlists):

            if name == 'standart_name_of_playlist':
                self.playlists['Плейлист' + str(len(self.playlists) + 2)] = []
            else:
                self.playlists[name] = []

        if name == 'standart_name_of_playlist':
            self.playlists['Плейлист' + str(len(self.playlists) + 1)].append(link)
        else:
            self.playlists[name].append(link)


    def add_track(self, link, name):
        if not(name in self.playlists):
            self.playlists[name] = link

    def del_track(self, i=-1, name=None):
        if i == -1:
            del self.playlists[name]
        numbers_= [u+1 for u in range(len(self.playlists))]
        if i >= 0 and i - 1 < len(self.playlists):
            for el, j in zip(self.playlists, numbers_):
                if j == i:
                    del self.playlists[el]
                    break



    def get_track_number(self):
        return len(self.playlists)

    def get_id(self):
        return self.id

    def get_name_track(self):
        if len(self.playlists) == 0:
            return 'Ваш плейлист пуст!'
        s = ''
        numbers_ = [i+1 for i in range(len(self.playlists))]
        for k, i in zip(self.playlists, numbers_):
            s += str(i) + ') ' + str(k) + '\n'
        return s


    def get_track(self, number):
        if number - 1 < len(self.playlists):
            numbers_ = [i + 1 for i in range(len(self.playlists))]
            for k, i in zip(self.playlists, numbers_):
                if i == number:
                    return self.playlists[k]


    def cache_user(self):
        s = self.id
        for name_track in self.playlists:
            s += '**' + name_track + '**' + self.playlists[name_track]
        return s


def read_user(line):
    s = line[:-1].split('**')
    u = USER(s[0])
    for i in range(1, len(s), 2):
        u.add_track(s[i+1], s[i])
    return u


if __name__ == '__main__':
    users = {'34': 10}
    u1 = USER('228')
    u2 = USER('228')
    u1.add_track('http||', 'mm')
    u1.add_track('http||', 'msada1')
    #u1.del_track(2)
   #u1.del_playlist('second')
    #u1.del_playlist('mm', 2)
    print(u1.cache_user())

    u3 = read_user('users.txt')
    print(u3.get_name_track())
