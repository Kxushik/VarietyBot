import json
import discord
from discord.ext import commands

with open('botToken.json',"r") as f:
    data = json.load(f)

print(data.get('TOKEN'))


TOKEN  = data.get('TOKEN')


client = commands.Bot(command_prefix ="$")



@client.command(name = "poll")
async def poll(context,*question):
    myEmbed = discord.Embed(title=" ".join(question),description = "Agree or Disagree", color=0x76D7C4)
    myEmbed.set_author(name="Asked by: {}".format(context.author))

    message = await context.message.channel.send(embed=myEmbed)
    await context.message.delete()
    await message.add_reaction("✅")
    await message.add_reaction("❌")

@client.event
async def on_ready():
    print("Bot is online.")


client.run(TOKEN)