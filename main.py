import os
from telethon import TelegramClient, events
from telegram import Bot

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
DESTINATION = os.environ["DESTINATION_CHANNEL"]

client = TelegramClient("forwarder", API_ID, API_HASH)
bot = Bot(token=BOT_TOKEN)

@client.on(events.NewMessage(chats="Dikystarboy"))
async def forward_message(event):
    await client.forward_messages(
        DESTINATION,
        event.message
    )

client.start()
client.run_until_disconnected()
