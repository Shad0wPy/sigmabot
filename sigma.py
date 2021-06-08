import discord
import json
from discord.ext import commands
from discord.utils import get

sigma = commands.Bot(command_prefix='*', help_command=None)
warnings = {}

token = "ODMzMDA3MjgwMzA3MTc1NDc1.YHsEfA.YkXNbo69EhvB50wuH8dJxQnFWSE"

#Permet de mettre un statut au bot ^^
@sigma.event
async def on_ready():
    print("Sigma est prêt !")
    await sigma.change_presence(status=discord.Status.online,
                                activity=discord.Game("*help | Créer par miaoumania#1017 et ₴Ⱨ₳ĐØ₩ĐɆV#7683"))

#Cette commande nous permet de connaître des infos sur le bot ヾ(•ω•)o
@sigma.command(aliases=['bot'])
async def botinfos(ctx):
    embed = discord.Embed(title="Information sur le bot !",
                          description="**Infos principales :**"
                                      "Le bot Sigma est entièrement codé en Python, avec le module `discord.py` et le module `json` \n"
                                      "Le script du bot à principalement été codé par <@490834874022756363> et le reste par <@761298593406910465>. \n"
                                      "Le bot est host sur un serveur de 200MB de RAM et de 1GB de stockage ! \n"
                                      "/n"
                                      "**Infos supplémentaires :**"
                                      "Nombre de lignes dans le script : `409` \n"
                                      "Version de Python : `3.8` \n"
                                      "Version du serveur host : `Pterodactyl Deamon`",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#L'une des commandes les plus importantes : les règles ╰(*°▽°*)╯
@sigma.command(aliases=['regle'])
async def regles(ctx):
    embed = discord.Embed(title="Règles du serveur :",
                          description="Le règlement du serveur se résume aux [ToS](https://discord.com/terms) et ["
                                      "Guidelines](https://discord.com/guidelines) de Discord. \n \n Tout membre du "
                                      "staff se réserve le droit d'appliquer la sanction lui semblant appropriée à un "
                                      "membre ne respectant pas l'un des points mentionnés dans les conditions et la "
                                      "charte d'utilisation de Discord et des lois francophones.",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Eheh, je suis dedans :3, on peut voir les membres du staff de SIGMΛ
@sigma.command()
async def staff(ctx):
    embed = discord.Embed(title="Les membres du staff :",
                          description="`@👑・Fondateurs` : <@490834874022756363> \n\n`👑・Administrateurs` : <@761298593406910465> <@630819991117234176> \n\n`⚡・Super Modérateurs` : <@699214343178551296> \n\n`🌌・Modérateurs` : <@768897650049155112> \n\n"
                                      "/n/n"
                                      "Total : `5` membres du staff SIGMΛ \n\n",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Je vois pas l'utilité de cette commande.. Mais elle permet de voir notre logo :O
@sigma.command(aliases=['serveuravatar'])
async def serveravatar(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/788793873106206758/789550458493992960/83458149cc4ab1baee5d5d3b0d25576f.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Pas besoin de vous faire un dessin, ça affiche juste l'avatar d'un mec
@sigma.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


#Quelques infos sur notre serveur ça fait pas de mal >:3
@sigma.command(aliases=['info'])
async def infos(ctx):
    embed = discord.Embed(title="Présentation de Sιgmα",
                          description="SIGMΛ (aka. SIGMA, Sigma, Sιgmα, Σ) est un serveur Discord communautaire avec "
                                      "comme but principal la discussion et le partage. Il a ouvert ses portes le 19 "
                                      "décembre 2020, fondé par <@490834874022756363>.\n Un bot a été codé "
                                      "spécialement pour le serveur ! \n Des animations, évenements, tournois, "
                                      "concours... ont lieu régulièrement ! Des giveaways de jeux EpicGames sont "
                                      "disponibles à tous les paliers de membres importants !",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Ici, miaoumania il s'est fait plaiz, 100 niveaux : ça fait beacoup là non ?
@sigma.command(aliases=['niveau'])
async def niveaux(ctx):
    embed = discord.Embed(title="Les niveaux du serveur :",
                          description="Les niveaux du serveur vont de 0 à 100, avec un rôle pour chaque niveau. \n\nDu Niveau 1 au Niveau 100 , en passant par le Niveau 10 , le Niveau 50, ou encore le Niveau 78. \n\n Le classement des membres du serveur et la liste de tous les rôles disponibles peut être trouvée [ici](https://arcanebot.xyz/lb/sigma).",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#En gros avec ça le bot c un perroquet :D
@sigma.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, channel: discord.TextChannel, *, message):
    await channel.send(message)


#Là, c'est quand ça capote D:
@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Usage de la commande impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


#Bon, ça nous permet de connaître quelques commandes du bot, pas besoin d'avoir Bac+178 pour comprendre
@sigma.command(aliases=['aide'])
async def help(ctx):
    embed = discord.Embed(title="Les différentes commandes du bot sigma :",
                          description="`*infos` affiche la présentation du serveur. \n`*regles` affiche les règles du serveur.\n`*salons` affiche les différents salons du serveur. \n`*staff` affiche les membres du staff de Sigma. \n `*bot` affiche les infos du bot \n`*candidature` affiche le formulaire pour soumettre sa candidature d'entrée dans le staff. \n`*suggestion` affiche les consignes pour soumettre une suggestion. \n`*reportinfos` affiche les consignes pour soumettre un report. \n`*serveravatar` affiche le logo du serveur. \n`*avatar @nomdel'utilisateur` affiche l'avatar de l'utilisateur mentionné. \n`*niveaux` affiche les différents niveaux disponibles sur le serveur.\n`*ping` affiche le ping du bot.\n`*pipo` affiche le fameux gif du pipo. \n`*serverinfo` affiche les informations du serveur.\n`*suggest [votre suggestion]` envoie la suggestion proposée.\n`*report [votre report] permez de report, de signaler un bug, etc.`\n`*help` affiche cette page. ",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Si tu sais pas comment faire une suggestion, ça peut aider
@sigma.command(aliases=['suggestions'])
async def suggestion(ctx):
    embed = discord.Embed(title="Comment suggérer une modification ou un ajout ? ",
                          description="Pour cela, rendez-vous dans le <#788817193709469746> (en traveaux) et tapez la commande ***suggest** suivie de votre suggestion.",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()

#La même chose qu'au dessus mais pour les reports cette fois
@sigma.command(aliases=['reportinfo'])
async def reportinfos(ctx):
    embed = discord.Embed(title="Comment report quelqu'un ou un bug ?",
                          description="Si vous voulez report quelqu'un, merci de nous indiquer son pseudo **sans** le mentionner ou nous donner son **ID** avec le plus de détails possibles. \n"
                                      "/n"
                                      "Si vous voulez report un bug, merci de nous indiquer dans quel salon cela est arrivé, et de nous donner les details du bug pour permettre à notre staff de le régler le plus vite possible.",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()

#Si tu veux entrer dans note secte *hum hum* je veux dire staff, remplit le formulaire
@sigma.command(aliases=['candid', 'candidatures'])
async def candidature(ctx):
    embed = discord.Embed(title="Comment soumettre sa candidature pour entrer dans le staff ? ",
                          description="Pour cela, rendez-vous sur [cette page](https://docs.google.com/forms/d/e/1FAIpQLSdiYRTJVfQ6fIZdj7IY6PjBlZRsYbN-o7tQY2o-bhOpfDwG4w/viewform?usp=pp_url), et répondez aux questions. Un administrateur vous recontactera pour vous donner les résultats.",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Noice, si tu sais quel  channel sert à quoi bah viens ici lol
@sigma.command(aliases=['salon', 'channel', 'channels'])
async def salons(ctx):
    embed = discord.Embed(title="Les salons du serveur :",
                          description="<#788782269018931202> ・ La présentation du serveur ヾ(•ω•)o \n<#788780806230900766> ・ Règlement du serveur ψ(.-. )> \n`━━━━━📜━━━━━` \n<#788784016001859585> ・ Salon qui contient les annonces du serveur (￣3￣)╭ \n <#788800922842955857> ・ Salon des arrivées, départs, warns, invitations... (*^_^*) \n<#788764210443059200> ・ Salon textuel pour bavarder (*^▽^*) \n<#788801331040616449> ・ Pour partagez des images, vidéos, gifs ou memes q(≧▽≦q)\n<#788783889828675655> ・ Salon réservé aux commandes des bots ! ╰(*°▽°*)╯\n<#788817193709469746> ・ Salon utilisé pour suggérer une modification ou un ajout ( •̀ ω •́ )✧\n`━━━━━🎉━━━━━`\n<#789055875268083783> ・ Le salon des cadeaux !!! (^∇^)\n<#788820483553755197> ・ Dans ce salon, un fait intéressant ou insolite est publié chaque jour o(*￣▽￣*)o\n<#788817474350743562> ・ Chaque membre peut publier un mot ou expression afin de compléter la phrase infinie (◠‿◠)\n (***TOUTS LES SALON SONT EN TRAVEAUX !***)",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


#Cheh un ban ( •̀ ω •́ )✧
@sigma.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")


#Bah ça à re-capoter
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bannissement de l'utilisateur impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


#Il s'en sort avec un simple avertissement, chanceux...
@sigma.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user, reason=reason)
            await ctx.send(f"{user} à été unban.")
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")


#CHEH TU RESTES BAN ( •̀ ω •́ )ψ
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Débannissement de l'utilisateur impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


#Exclusion... ça finit souvent dans le bureau du principal..
@sigma.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason=reason)
    await ctx.send(f"{user} à été kick pour la raison suivante: {reason}")
    await ctx.message.delete()


#Ou pas :D
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Exclusion de l'utilisateur impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


#Effacer toutes les preuves d'un crime >:D
@sigma.command(pass_context=True, aliases=['purge', 'clean', 'delete'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int):
    await ctx.channel.purge(limit=limit + 1)


#Sauf si on est nul :(
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nettoyage des messages impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


@sigma.command()
@commands.has_permissions(manage_roles=True)
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name="Muted",
                                            permissions=discord.Permissions(send_messages=False, speak=False),
                                            reason="Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages=False, speak=False)
    return mutedRole


async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role

    return await createMutedRole(ctx)


@sigma.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseignée"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été mute !")
    await ctx.message.delete()


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Mute de l'utilisateur impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


@sigma.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member, *, reason="Aucune raison n'a été renseignée"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason=reason)
    await ctx.send(f"{member.mention} a été unmute !")
    await ctx.message.delete()


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Unmute de l'utilisateur impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


@sigma.command()
@commands.has_permissions(manage_messages=True)
async def modo(ctx):
    embed = discord.Embed(title="Les différentes commandes de modération du bot sigma :",
                          description="`*ban @utilisateur raison` Banni l'utilisateur mentionné. \n`*unban utilisateur#XXXX` Dé-banni l'utilisateur tagué.\n`*clear X` Supprime X messages. \n`*kick @utilisateur raison` Exclu l'utilisateur mentionné. \n`*mute @utilisateur raison` Rend muet l'utilisateur mentionné. \n`*unmute @utilisateur raison` Rend la parole à l'utilisateur mentionné. \n `*say #salon message` Envoie le message demandé dans le salon demandé.\n`*modo` affiche cette page.\n`*mp @utilisateur message` Envoie le message demandé à l'utilisateur mentionné. \n`*vote` permet de faire voter les membres. \n`.annonce` Envoi d'une annonce dans le channel __*<En cours>*__ \n***Aministrateurs seulement.***",
                          color=0x2F3136)
    await ctx.send(embed=embed)
    await ctx.message.delete()


@modo.error
async def modo_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Usage de la commande impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


@sigma.command(aliases=['dm'])
@commands.has_permissions(administrator=True)
async def mp(ctx, user: discord.User, *, value):
    await user.send(f"{value}")


@mp.error
async def mp_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Usage de la commande impossible. Vous n'avez pas les permissions nécessaires.")
    await ctx.message.delete()


@sigma.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(sigma.latency, 1)))
    await ctx.message.delete()


@sigma.command()
async def pipo(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/788764210443059200/790987611442905130/inconnu.gif")
    await ctx.message.delete()


@sigma.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str("SIGMΛ est un serveur Discord communautaire avec comme but principal la discussion et le partage.")

    id = str(ctx.guild.id)

    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title="SIGMΛ",
        description=description,
        color=0x2F3136
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Fondateur", value="<@490834874022756363>", inline=True)
    embed.add_field(name="ID", value=id, inline=True)
    embed.add_field(name="Région", value="Europe", inline=True)
    embed.add_field(name="Nombre de membres", value=memberCount, inline=True)

    await ctx.send(embed=embed)
    await ctx.message.delete()

@sigma.command()
async def suggest(ctx, *, description):
    ': Suggest a command. Provide the command name and description'
    embed = discord.Embed(title='Nouvelle suggestion', description=f'Suggéré par: {ctx.author.mention}', color=discord.Color.blurple())
    embed.add_field(name='Description', value=description)
    channel = ctx.guild.get_channel(845124536893440030)
    msg = await channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await ctx.message.delete()


@sigma.command()
@commands.has_permissions(administrator=True)
async def vote(ctx, *, description):
    'Commande vote'
    embed = discord.Embed(title='C\'est l\'heure de voter !', description=f'Vote par: {ctx.author.mention}', color=discord.Color.green())
    embed.add_field(name='Description', value=description)
    channel = ctx.guild.get_channel(845124536893440030)
    msg = await channel.send(embed=embed)
    await msg.add_reaction('✔')
    await msg.add_reaction('❌')
    await ctx.message.delete()

@sigma.command()
async def vote(ctx, *, description):
    'Commande report'
    embed = discord.Embed(title='Nouveau report !', description=f'Report éfféctué par: {ctx.author.mention}', color=discord.Color.red())
    embed.add_field(name='Description', value=description)
    channel = ctx.guild.get_channel(845124536893440030)
    msg = await channel.send(embed=embed)
    await msg.add_reaction('✔')
    await msg.add_reaction('❌')
    await ctx.message.delete()

@sigma.command()
@commands.has_permissions(administrator=True)
async def annonce(ctx, *, description):
    'Commande annnonce'
    embed = discord.Embed(title='Annonce !', description=f'Annonce éfféctuée par: {ctx.author.mention}', color=discord.Color.blurple())
    embed.add_field(name='Description', value=description)
    channel = ctx.guild.get_channel(845124536893440030)
    msg = await channel.send(embed=embed)
    await msg.add_reaction('✔')
    await ctx.send(f"@everyone")
    await ctx.message.delete()

sigma.run(token)
