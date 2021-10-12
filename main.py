import tele_secret
from dict_bot import meaning
# from yt_bot import pyyoutube
from py_weather import getweather
from url_shortener import shorten_url
from telethon import TelegramClient, events

api_id = tele_secret.api_id
api_hash = tele_secret.api_hash
session = tele_secret.session_name

app = TelegramClient(session, api_id, api_hash)

source_group_id =   #Value has to be an Integer value. Enter the source gorup ID here, from where you want the messages forwarded
destination_group_id =   #Value has to be an Integer value. Enter the destination gorup ID here, to where you want the messages forwarded

@app.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    message = event.message
    print(message.message)

    if chat.id == source_group_id:
        await app.forward_messages(destination_group_id, message)

    # ChatIDList is the ID list of the groups where i want the functionality (dictionary, weather forecast, url-shortener etc) to be executed, List elements have to be Integers
    ChatIDList = []

    if any(item == chat.id for item in ChatIDList):

        if message.message.lower() == "/help":
            help_text = '''**Dictionary** :
/dict word

**Url Shortener** :
/tinyurl link

**Weather Forecast** :
/weather city-name

**Youtube Downloader** (unstable):
/yt youtube-link resolution
resolutions available = 360, 720'''
            await message.reply(help_text)

        if message.message.lower().startswith("hi"):
            await message.reply("Hello. How are you?")

        if "who made you" in message.message.lower():
            await message.reply("Dr. Zibran Khan made me.")

        if message.message.lower().startswith(r"/dict"):
            search_term = message.message.lower().replace(r"/dict", '').strip()
            try:
                await message.reply(meaning(search_term))
            except:
                await message.reply("Sorry, this word is not in the dictionary.")

        if message.message.lower().startswith(r"/tinyurl"):
            url = message.message.lower().replace(r"/tinyurl", '').strip()
            short_url = shorten_url(url)
            await message.reply("Here is your shortened url :" + "\n\n" + short_url)

        if message.message.lower().startswith(r"/yt"):
            url_res = message.message.lower().replace(r"/yt ", '').split(" ")
            print(url_res)
            video_title = pyyoutube(url_res[0], url_res[1])
            await app.send_file(chat.id, "video.mp4", caption=video_title)

        if message.message.lower().startswith(r"/weather"):
            city = message.message.lower().replace(r"/weather", '').strip()
            print(city)
            forecast = getweather(city)
            await message.reply(forecast)



app.start()
app.run_until_disconnected()