import discord
from chatgpt import *

openai.api_key = API_KEY

class myBot(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print('------')
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!'):
            message.content = formatInputUser(message.content[1:])
            response = getResponse(message.content)
            if "choices" in response.keys():
                for text in response["choices"]:
                    await message.channel.send(text["text"], reference=message)
            else:
                await message.channel.send("Choices key missing, no output.", reference=message)

intents = discord.Intents.default()
intents.message_content = True

client = myBot(intents=intents)
client.run(os.getenv("DISCORD_BOTLPP_APIKEY"))
            