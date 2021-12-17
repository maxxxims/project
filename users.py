

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

    def del_playlist(self, name, i=-1):
        if i == -1:
            del self.playlists[name]
        if i >= 0 and i - 1 < len(self.playlists):
            self.playlists[name].pop(i-1)

    def get_playlist_size(self):
        return len(self.playlists)

    def get_id(self):
        return self.id

    def get_name_track(self):
        s = ''
        for k in self.playlists:
            s += str(k) + ' =='
            for links in self.playlists[k]:
                s+=' ' + links
            s+= ','
        return s


if __name__ == '__main__':
    users = {'34': 10}
    u1 = USER('228')
    u2 = USER('228')
    u1.add_playlist('http||', 'mm')
    u1.add_playlist('http123123||', 'mm')
    u1.add_playlist('http123123||', 'second')
   #u1.del_playlist('second')
    #u1.del_playlist('mm', 2)
    print(u2.get_name_track())