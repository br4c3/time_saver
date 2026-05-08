import discord

from app.core.app import app
from app.bot.client import TimeSaver


intents = discord.Intents.default()
intents.message_content = True

client = TimeSaver(
    intents=intents
)

app.logger.info("Starting Discord bot...")

client.run(
    app.config.discord_token
)