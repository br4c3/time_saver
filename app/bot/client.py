import discord

from app.core.app import app


class TimeSaver(discord.Client):

    async def on_ready(self):
        app.logger.info(
            f"Logged on as {self.user}"
        )

    async def on_message(self, message):
        if message.author == self.user:
            return

        app.logger.info(
            f"Message from {message.author}: "
            f"{message.content}"
        )