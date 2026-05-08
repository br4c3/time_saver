import discord

import logging
logging.basicConfig(
    filename="app.log",
    filemode="a",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
)


class TimeSaver(discord.Client):
    async def on_ready(self):
        logging.info(f"Logged on as {self.user}!")

    async def on_message(self, message):
        logging.info(f'Message from {message.author}: {message.content}')