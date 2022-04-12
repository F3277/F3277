mport discord
import asyncio
import colorama
import json
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import random
import time
import aiohttp
from discord.utils import get
from discord.utils import find
from discord import Permissions

asyncio.get_event_loop().set_debug(True)



cum = commands.Bot(command_prefix="c!", intents=discord.Intents.all())


token = "OTYxOTExMjg5MjA1MTIxMDI0.Yk_3sg.wpqZZngPGTxzgAFWCptwlyH2Q0Q"

cum.remove_command('help')



# quando il bot viene runnato viene segnalato il suo funzionamento e attivita con @cum.event che imprime nella shell/cmd "CumBot Tst.exe 𝔗𝔢𝔰𝔱𝔦𝔪𝔬𝔫𝔢 𝔡𝔦 𝔅𝔯𝔢𝔰𝔠𝔦𝔞 𝔑.1"
@cum.event
async def on_ready():
    await cum.change_presence(activity=discord.Streaming(name="Twitch: quackki", url='https://www.twitch.tv/quackki'))
print('''CumBot 
TsT.exe
𝔗𝔢𝔰𝔱𝔦𝔪𝔬𝔫𝔢 𝔡𝔦 𝔅𝔯𝔢𝔰𝔠𝔦𝔞 𝔑.1''')


#Inizio help cmd
@cum.command()
async def helps(ctx, *args):
     await ctx.message.delete()
     retStr = str(
     """```fix\nc!helps - Mostra questo comando\n\nc!frocio/c!gay - quanto sei frocio?\n\nc!niggarate/c!negro - quanto sei negro?\n\nc!ban - Banna un membro (permesso richiesto: bannare membri)\n\nc!kick - Kicka un membro (peremsso richiesto: kickare membri)\n\nc!whois/c!userinfo - Info su un utente\n\nc!say - permette di scrivere con il bot (ES: n!say test)\n\nc!mcount\membercount - Count dei membri\n\nc!clear - Cancella una quantitra di messaggi (max:2000)\n\nc!snipe - Snipera l'ultimo messaggio inviato\n\nc!serverinfo/sinfo - Info sul Server\n\nc!avatar/av - MOstra avatar Membro\n\nc!meme - meme fun\n```"""
)
     embed = discord.Embed(color=800080, title="CumGuy CMDS")
     embed.add_field(name="Help", value=retStr)
     embed.set_image(url='https://cdn.discordapp.com/attachments/871409478992539658/962445311039643779/pngwing.com.png')


     await ctx.send(embed=embed)
#Termine help cmd

#quando entra senda un emebd con scritto embed=discord.Embed(title="CumGuy è entrato ohssy", description=f"""Bot ideato da TsT per {guild.name}, il prefiz è c!
@cum.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == '💬parla-qua',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        embed=discord.Embed(title="CumGuy è entrato ohssy", description=f"""
        Bot ideato da TsT per {guild.name}, il prefix è c!
        
        """, color=0xd89522)
        await general.send(embed=embed)


snipe_message_author = {}
snipe_message_content = {}

#event snipe
@cum.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(15)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

#Inizio Snipe cmd
@cum.command(aliases=["Snipe"])
async def snipe(ctx):
    await ctx.message.delete()
    channel = ctx.channel
    try:
        em = discord.Embed(
          title = f"L'ultimo messaggio cancellato in #{channel.name} è: ", description = snipe_message_content[channel.id], color=0x9b59b6)
        em.set_footer(text = f"Inviato da: {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except KeyError:
        await ctx.send(f" nessun messaggio da sniperare in #{channel.name}")
#Termine Snipe cmd

@cum.event
async def on_member_join(member):
    channel = cum.get_channel(963104489835995206)
    embed=discord.Embed(title=f"Welcome {member.name}", description=f"Benvenuto negro di merda in {member.guild.name}!") 
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/843969304164827199/856980660057407488/Fermo-1.png')
    await channel.send(embed=embed)
    role =   discord.utils.get(member.guild.roles, name="nuovo ruolo")
    role3 = discord.utils.get(member.guild.roles, name="palenuovo ruolo")
    await member.add_roles(role, role3)



#gay rate
@cum.command(aliases=["gay"])
async def frocio(ctx):

    await ctx.message.delete()
    embed = discord.Embed(
        title="FrocioRate",
        description=
        f"{ctx.author.mention} sei {random.randrange(101)}% frocio",
        color=0x9b59b6)
    embed.set_image(url='https://cdn.discordapp.com/attachments/942025137144856637/962425232734449664/download-1.jpg')
    await ctx.send(embed=embed)

@cum.command(aliases=["niggarate"])
async def negro(ctx):

    await ctx.message.delete()
    embed = discord.Embed(
        title="NegroRate",
        description=
        f"{ctx.author.mention} sei {random.randrange(101)}% negro, se sei sopra il 50% allora fai parte di una minoranza complimenti",
        color=0x9b59b6)
    embed.set_image(url='https://cdn.discordapp.com/attachments/871409478992539658/962429678486949899/collage-arresto-presunti-scafisti-trapani.JPG')
    await ctx.send(embed=embed)

  
#Inizio Ban cmd
@cum.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member=None, reason=None):
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        embed1 = discord.Embed(title="ERROR:", description="questo messaggio è apparso perchè: ho hai provato ad auto kickarti oppure non hai inserito chi kickare, ciccione 😟.", color=0x9b59b6)
        await ctx.send(embed=embed1)
        return
    if reason == None: 
        reason = 'Nessuna Motivazione Inserita.'
    await member.ban(reason=reason)
    await ctx.channel.send(f"@{ctx.message.author} ha bannato {member} dal server | Motivo :{reason}")
#Termine Ban cmd

@cum.command()
async def nuke(ctx):
 await ctx.channel.send(f"{ctx.message.author} cazzo pensi di fare negro, che clown. ")

#Inizio Kick cmd
@cum.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member=None, reason=None):
    await ctx.message.delete()
    if member == None or member == ctx.message.author:
        embed1 = discord.Embed(title="ERROR:", description="questo messaggio è apparso perchè: ho hai provato ad auto kickarti oppure non hai inserito chi kickare, ciccione 😟.", color=0x9b59b6)
        await ctx.send(embed=embed1)
        return
    if reason == None: 
        reason = 'Nessuna Motivazione Inserita.'
    await member.kick(reason=reason)
    await ctx.channel.send(f"{ctx.message.author} ha kickato {member} dal server | Motivo :{reason}")
#Termine kick cmd

#Inizio av show cmd
@cum.command(aliases=["avatar"])
async def av(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.purple(),
                          timestamp=ctx.message.created_at,
                          title=f"Avatar Utente - {member}")
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)
#Termine av show cmd

format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

#Inizio Server Info Cmd
@cum.command(aliases=["sinfo"])
@commands.guild_only()
async def serverinfo(ctx):
    embed = discord.Embed(
        color=discord.Color.purple()
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Informazioni su **{ctx.guild.name}**: ", value = f" ID: {ctx.guild.id} \nOwner: **{ctx.guild.owner}** \n Posizione: {ctx.guild.region} \nCreazione Server: {ctx.guild.created_at.strftime(format)} \n{ctx.guild.member_count} \nCanali: **{channels}** Testuali **{text_channels}** Vocali, **{voice_channels}** Categorie **{categories}** \nVerifica: {str(ctx.guild.verification_level).upper()} \nAttività: {', '.join(f'{x}' for x in ctx.guild.features)}")
    await ctx.send(embed=embed)
#Termine Sinfo cmd
  
#Inizio Whois cmd
@cum.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(),
                          timestamp=ctx.message.created_at,
                          title=f"Info utente - {member}")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="UserName:", value=member.display_name)

    embed.add_field(
        name="Account creato il:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Joinnato il:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Ruoli:",
                    value="".join([role.mention for role in roles]))
    embed.add_field(name="Ruolo più alto:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)
  
#Inizio say cmd
@cum.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    allowed_mentions = discord.AllowedMentions(users=True,
                                               roles=False,
                                               everyone=False)
    await ctx.send(arg, allowed_mentions=allowed_mentions)
#Termine say cmd
  
#Inizio member count cmd
@cum.command(aliases=["membercount"])
async def mcount(ctx):

    await ctx.message.delete()
    embed = discord.Embed(
        title="Member count",
        description=
        f"Ci sono {ctx.guild.member_count} membri",
        color=0x9b59b6)
    await ctx.send(embed=embed)
#Termine member count commands
  
#Inizio clear cmd
@cum.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount)
#Termine clear cmd

@cum.command(aliases=["h"])
async def hentai(ctx):
  await ctx.message.delete()
  
  embed = discord.Embed(colour=discord.Colour.purple(),
                          timestamp=ctx.message.created_at, title="CumGuy hentai cmd", description="Hentai Fresco Per Te")  
  async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/hentai/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)
          
memes = ['https://cdn.discordapp.com/attachments/963110197587496971/963110300767375500/IMG_20220324_165126.jpg', 'https://cdn.discordapp.com/attachments/961916202236649502/963110371961475183/Screenshot_20211027_142039.jpg', 'https://cdn.discordapp.com/attachments/961916202236649502/963110446490079282/peppe_brescia.png', 'https://cdn.discordapp.com/attachments/961916202236649502/963110490458947614/Vero.png',
'https://cdn.discordapp.com/attachments/961916202236649502/962622689888063508/1649577480161.png',
'https://cdn.discordapp.com/attachments/926111396758945854/950516735876935721/95835925fb42a9c16716b25027c3deb1ab960b18fcbc3c884bd2405e2c54100e_1.png',
'https://cdn.discordapp.com/attachments/926111396758945854/951944148473249802/Picsart_22-03-11_18-23-50-483.jpg',
'https://cdn.discordapp.com/attachments/926111396758945854/933316185037107250/20200310_125510.jpg', 
'https://cdn.discordapp.com/attachments/926111396758945854/933316184651227166/lyon.jpg',
'https://cdn.discordapp.com/attachments/926111396758945854/933315539785367612/image0-2-1.png',
'https://cdn.discordapp.com/attachments/926111396758945854/932921583868190730/IMG_7354.jpg',
'https://cdn.discordapp.com/attachments/926111396758945854/926164825069989938/KA-designs-swastika-copy-635x357.jpg',
'https://cdn.discordapp.com/attachments/926111396758945854/926164824440860772/1492590360_nazifurry.jpg',
'https://cdn.discordapp.com/attachments/926111396758945854/926136764433846292/d5dd94979922e0d2308966ea213a635fbe0d8422eea0fe780b0adebf2574755f.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926136764341575680/IMG-20210311-WA0077.JPG',
'https://cdn.discordapp.com/attachments/926111396758945854/926130604779655168/Screenshot_20211107-174148_TikTok.JPG'
'https://cdn.discordapp.com/attachments/926111396758945854/926133204488970290/e35ec905-c9eb-4337-b50d-e74e4d17d51e.JPG',
'https://cdn.discordapp.com/attachments/926111396758945854/926131008221356072/6E422C78-C2C2-4265-8EF3-22057E3A6EEF.GIF',
'https://cdn.discordapp.com/attachments/926111396758945854/926131008221356072/6E422C78-C2C2-4265-8EF3-22057E3A6EEF.GIF',
'https://cdn.discordapp.com/attachments/926111396758945854/926129681026150551/image0.JPG',
'https://cdn.discordapp.com/attachments/963117374356209665/963117552123400272/JLJdk2HSF7AAAAAASUVORK5CYII.jpg',
'https://cdn.discordapp.com/attachments/963117374356209665/963118390250197073/images_89.jpeg',
'https://cdn.discordapp.com/attachments/963117374356209665/963118390443130940/download.jpeg',
'https://cdn.discordapp.com/attachments/963117374356209665/963118518952407040/FB_IMG_1626812829876.jpg',
'https://cdn.discordapp.com/attachments/963117374356209665/963118974885838848/Screenshot_20210711-1738012.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963118975171035176/Screenshot_20210711-1733372.png',
'https://cdn.discordapp.com/attachments/961916202236649502/963116713753337876/steamuserimages-a.akamaihd.jpg',
'https://cdn.discordapp.com/attachments/926111396758945854/926163801127133184/Screenshot_20211111-113804_WhatsApp.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926131262551363654/57c5d0893aa9ea1bab1b5101d6954579.JPG',
'https://cdn.discordapp.com/attachments/961916202236649502/963116714541854840/7c25b562-b12d-4ed5-8ca7-6c365076d55b.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963120168786071622/60f94f9fdb370d0f3ca0ce78f1ee4acf.gif',
'https://cdn.discordapp.com/attachments/961916202236649502/963116714785136660/image0-29.png-1.jpg',
'https://cdn.discordapp.com/attachments/961916202236649502/963116715233910884/motivate.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963120170656747550/IMG_20210424_231819_774.jpg',
'https://cdn.discordapp.com/attachments/963117374356209665/963120169058697236/cumLEGGNDARIA-removebg-preview.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963120169876590592/image0-4.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963120169876590592/image0-4.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963122034777424002/Screenshot_20210522-2219292.png',
'https://cdn.discordapp.com/attachments/963117374356209665/963122031543582740/IMG_2573.png',
'https://cdn.discordapp.com/attachments/926111396758945854/926165512940048384/20201203_025801.gif',
'https://cdn.discordapp.com/attachments/926111396758945854/926125546855874620/19DD863E-5C45-4102-9DCE-E32D24AD60C9.gif',
'https://cdn.discordapp.com/attachments/926111396758945854/926121813694636102/PicsArt_07-28-06.10.05.JPG',
'https://cdn.discordapp.com/attachments/926111396758945854/926121108518891600/gay-nazi-flag.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926118847629643816/Mematic_20210625_025017.JPG',
'https://cdn.discordapp.com/attachments/926111396758945854/926118842990739486/image0.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926118668369268756/Schermata_2021-01-21_alle_12.57.09.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926118658105815081/IMG-20210206-WA0008.JPG',
'https://cdn.discordapp.com/attachments/926111396758945854/926116748661497896/unknown-1.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926116751110971432/unknown-3.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926116751794655262/unknown-2.PNG',
'https://cdn.discordapp.com/attachments/926111396758945854/926115260308545586/Screenshot_20210726_214801.JPG',
'https://cdn.discordapp.com/attachments/926111396758945854/926114646899961916/frocizzato.PNG'
]

@cum.command(aliases=["Memes"])
async def meme(ctx):
 await ctx.message.delete()
 embed = discord.Embed(
   title="Meme cmd",
   colour=discord.Colour(0x9b59b6),
   description="Meme cmd eseguito con successo",
   timestamp=datetime.datetime.utcfromtimestamp(1580842764)
    )
 embed.set_image(url=(random.choice(memes)))

 await ctx.send(embed=embed)
 

cum.run(token) #run bot
