from gmusicapi import Mobileclient
import xlwt


def addheader(stylesheet):
    stylesheet.write(0, 0, 'Название')
    stylesheet.write(0, 1, 'Исполнитель')
    stylesheet.write(0, 2, 'Альбом')
    stylesheet.write(0, 3, 'Композитор')


def add_item_to_page(row, track, page):
    try:
        row += 1
        if 'title' in track:
            page.write(row, 0, track['title'])
        if 'artist' in track:
            page.write(row, 1, track['artist'])
        if 'album' in track:
            page.write(row, 2, track['album'])
        if 'composer' in track:
            page.write(row, 3, track['composer'])
        return row
    except:
        print(row)

api = Mobileclient()
api.login('mail@gmail.com', 'password', Mobileclient.FROM_MAC_ADDRESS)
# => True
library = api.get_all_songs()

# Write all txt
f = open('allTracks.txt', 'w', encoding='utf-8')

for item in library:
    buff_str = (item['title'] + '//' + item['artist'] + '//' + item['album'] + '//' + item['composer']) + '\n'
    f.write(buff_str)
f.close

# Write all to xls
wb = xlwt.Workbook()
names = str('all tracks')
ws = wb.add_sheet(names)
if 'ws' in globals():
    addheader(ws)
i = 0
for item in library:
    if 'ws' in globals():
        i = add_item_to_page(i, item, ws)

library = api.get_all_user_playlist_contents()

for playlist in library:
    name = str(playlist['name'])
    ws2 = wb.add_sheet('Playlist ' + name)
    if 'ws2' in globals():
        addheader(ws2)
    j = 0
    for record in playlist['tracks']:
        try:
            if 'track' in record:
                position = record['track']
                if 'ws2' in globals():
                    j = add_item_to_page(j, position, ws2)
        except:
            print('Error in playlist' + name + 'position : ' + j)

wb.save('music.xls')
api.logout()
