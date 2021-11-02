import dbus

bus = dbus.SessionBus()
for service in bus.list_names():
    if service.startswith('org.mpris.MediaPlayer2.'):
        player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')

        metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata',
                              dbus_interface='org.freedesktop.DBus.Properties')

_title = str(metadata["xesam:title"])
_album = str(metadata["xesam:album"])
__artist = "%s" % ''.join([str(v) for v in metadata["xesam:artist"]])
_artist = list(__artist.split(","))
# _artist = list(__artist.split("&"))
artist = []

for i in _artist:
    i = i.lstrip()
    i = i.rstrip()
    artist.append(i)
    
print(f"Title : {_title}")
print(f"Album : {_album}")
print(f"Artist : {artist}")

from requests import get
from json import loads


_url = (f'https://api.lyrics.ovh/v1/{artist[0].replace(" ", "-")}/{_title.replace(" ", "-")}')
print(_url)
print()
response = get(_url)
json_data = loads(response.content)
lyrics = json_data["lyrics"]
# sansfirstline = lyrics.split('\n', 1)[1]
# print(sansfirstline)
print(lyrics)
