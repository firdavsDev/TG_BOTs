from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from PIL import Image, ImageDraw
import time





client = TelegramClient('Soatgiigdyidykdkydmgxmgdgmdktsjtdmgdmgdtk', "2772974", "a21236b7def8175e5083f9583a1d4396")
client.start() # TelegramClientni ishga tushuramiz


def tick():
 global time1
 # get the current local time from the PC
 time2 = time.strftime('%H:%M')
 # if time string has changed, update it
if time2 != time1:
    time1 = time2
# create an image if it doesn't exist
img = Image.new('RGB', (640, 640), color = (40, 40, 40))
d = ImageDraw.Draw(img)
# place text in the center
d.text(((640-(len(time2)*22))/2,640/2-30), time2, font = font, fill = (238,238,238))
# save image
img.save('profile.jpg')

upload()


def upload():
    client(DeletePhotosRequest(client.get_profile_photos('me')))
    result = client(UploadProfilePhotoRequest(
     file=client.upload_file('profile.jpg')
 ))


tick()
client.run_until_disconnected()