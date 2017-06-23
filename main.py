# from gmusicapi import Musicmanager
#
# manager = Musicmanager()
# manager.__init__()
# # log_result = manager.perform_oauth()
# log_result = manager.login()
# print(log_result)
# if log_result:
#     music = manager.get_purchased_songs()
#     print(music)
#
from gmusicapi import Mobileclient

api = Mobileclient()
api.login('mail@gmail.com', 'pass', Mobileclient.FROM_MAC_ADDRESS)
# => True

library = api.get_all_songs()
f = open('text.txt', 'w', encoding='utf-8')

for item in library:
    buff_str = (item['title'] + '//' + item['artist'] + '//' + item['album'] + '//' + item['composer']) + '\n'
    f.write(buff_str)

#Add Parse user playlist
library = api.get_all_user_playlist_contents()
f = open('text2.txt', 'w', encoding='utf-8')

for item in library:
    buff_str = (item['title'] + '//' + item['artist'] + '//' + item['album'] + '//' + item['composer']) + '\n'
    print(buff_str)
    f.write(buff_str)


api.logout()
f.close
