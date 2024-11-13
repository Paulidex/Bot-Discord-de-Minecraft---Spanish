import discord
from discord.ext import commands, tasks
from webserver import keep_alive
import datetime
import asyncio
from urllib import parse, request
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="+", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print('El bot está listo')

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(name="En " + str(len(bot.guilds)) + " servidores. Prefijo +"))

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title='Comandos',
        description='Aquí están los comandos que puedes utilizar para mejorar tu experiencia en Discord y en el servidor de Minecraft.',
        color=discord.Color.purple()
    )
    embed.add_field(name='`+ip`', value='Muestra la IP del servidor de Minecraft.', inline=False)
    embed.add_field(name='`+normas`', value='Clasificación de normas del servidor de Minecraft: graves, leves, juicio y staff.', inline=False)
    embed.add_field(name='`+leves`', value='Muestra las normas leves.', inline=False)
    embed.add_field(name='`+graves`', value='Muestra las normas graves.', inline=False)
    embed.add_field(name='`+juicio`', value='Muestra las normas aplicables en el juicio.', inline=False)
    embed.add_field(name='`+staff`', value='Muestra las normas del staff de Minecraft.', inline=False)
    embed.add_field(name='`+clanes`', value='Muestra las reglas para los clanes.', inline=False)
    embed.add_field(name='`+comandos`', value='Lista de comandos que puedes usar en el servidor.', inline=False)
    embed.add_field(name='`+tienda`', value='Página de donaciones y rangos.', inline=False)
    embed.add_field(name='Emergencia', value='Para reportar un bug o problema de OlympusBot, contacta a la creadora Paulidex.', inline=False)
    embed.set_footer(text='Para contrataciones, contactar a Paulidex#9510.')
    await ctx.send(embed=embed)

@bot.command()
async def a(ctx):
    await ctx.send('El bot está funcionando correctamente')

@bot.command()
async def tienda(ctx):
    await ctx.send('Visita nuestra tienda para ver nuestros rangos y realizar donaciones ^.^ `https://olympusland.tebex.io`')

@bot.command()
async def ip(ctx):
    embed = discord.Embed(
        title='Servidor Minecraft Java',
        description='Versión 1.16.5 - 1.17.1: play.olympusland.xyz',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Para ver más comandos, escribe +help')
    await ctx.send(embed=embed)

@bot.command()
async def normas(ctx):
    await ctx.send('Las normas están clasificadas en graves, leves, staff y juicio. Para verlas, escribe `+graves` `+leves` `+staff` `+juicio` `+clanes`')

@bot.command(name='leves')
async def leves(ctx):
    embed = discord.Embed(
        title='Normas Leves',
        description='1) Los bugs están permitidos, pero antes debes consultar su uso con alguien del staff. \n'
                    '2) No insultar a otros jugadores si no es de su agrado. \n'
                    '3) Evita hacer flood (ejemplo: holaaaaaa), spam o texto innecesario que sature el chat. \n'
                    '4) No se permite tener más de dos relojes de Redstone; generadores de lag y cargadores de chunks están prohibidos. \n'
                    '5) Las mascotas son propiedad privada; está prohibido matarlas intencionalmente, aunque no estén en una zona protegida. \n'
                    '6) Los lobos no pueden ser utilizados como armas para PVP. \n'
                    '7) En caso de problemas aislados, el staff puede realizar reuniones para encontrar una solución justa. \n'
                    '8) No salirse de un juicio.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')
    await ctx.send(embed=embed)

@bot.command(name='graves')
async def graves(ctx):
    embed = discord.Embed(
        title='Normas Graves',
        description='1) El uso de multicuentas está prohibido. Si deseas cambiar de cuenta, notifica al staff para transferir tus ítems y propiedades. \n'
                    '2) Hacks están prohibidos y serán sancionados con ip-ban. \n'
                    '3) Destrucción de construcciones protegidas y robo de ítems en zonas de otros jugadores están prohibidos. \n'
                    '4) Cualquier tipo de asesinato como tpakill y spawn kill está prohibido. \n'
                    '5) Prohibido aprovechar bugs, como duplicación o glitches de movilidad. \n'
                    '6) Prohibido el uso de hacks como xray o autoclick. \n'
                    '7) No se permite distribuir enlaces externos sin aprobación del staff. \n'
                    '8) Hablar con respeto al staff y evitar faltas de respeto. \n'
                    '9) Intentos de evadir sentencias aumentarán la pena; ayudar a otro jugador a evadir es sancionable. \n'
                    '10) Mentirle al staff está prohibido. \n'
                    '11) Prohibido hacerse pasar por el staff. \n'
                    '12) No usar otros casos para justificar acciones. \n'
                    '13) Mensajes y construcciones ofensivas están prohibidas. \n'
                    '14) Prohibido escapar de la cárcel. \n'
                    '15) No ayudar a un preso a salir de la cárcel. \n'
                    '16) No explorar, minar o talar en el mundo normal; utiliza /warp recursos.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')
    await ctx.send(embed=embed)

@bot.command(name='juicio')
async def juicio(ctx):
    embed = discord.Embed(
        title='Normas del Juicio',
        description='1) No interrumpir el juicio. \n'
                    '2) Presentar pruebas. \n'
                    '3) No hacer perder el tiempo al staff que actúe como juez. \n'
                    '4) Leer las normas antes de solicitar un juicio. \n'
                    '5) Solo se permite la presencia de testigos y partes involucradas en el juicio. \n'
                    '6) Solo Owners, Admins y Mods pueden actuar como jueces. \n'
                    '7) Ambas partes (acusados y acusadores) deben estar presentes.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')
    await ctx.send(embed=embed)

@bot.command(name='clanes')
async def clanes(ctx):
    embed = discord.Embed(
        title='Normas de los Clanes',
        description='1) Todo tipo de PVP es válido si ambos jugadores pertenecen a un clan. \n'
                    '2) Se permite el grifeo, pero solo a bases de clanes.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')
    await ctx.send(embed=embed)

@bot.command(name='staff')
async def staff(ctx):
    embed = discord.Embed(
        title='Normas del Staff',
        description='1) Las quejas sobre baneos se atienden por Discord. \n'
                    '2) Objetos exclusivos del staff no deben caer en manos de jugadores; ambos involucrados serán sancionados si esto sucede. \n'
                    '3) Responder a las dudas de los jugadores. \n'
                    '4) Saludar a los nuevos jugadores. \n'
                    '5) No abusar del poder. \n'
                    '6) Solo Owners, Admins y Mods pueden sancionar. \n'
                    '7) Tratar a todos los jugadores por igual. \n'
                    '8) No dar ítems del creativo a jugadores; solo por survival. \n'
                    '9) Ser neutral en juicios. \n'
                    '10) La inactividad injustificada puede resultar en expulsión del staff. \n'
                    '11) No revelar novedades en desarrollo a jugadores.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')
    await ctx.send(embed=embed)

@bot.command(name='comandos')
async def comandos(ctx):
    embed = discord.Embed(
        title='Comandos que puedes usar en el servidor',
        description='/tpa (ir a otro jugador) \n'
                    '/tpaccept (aceptar tpa) \n'
                    '/tpahere (traer a otro jugador) \n'
                    '/back (volver al sitio anterior) \n'
                    '/sit (sentarse) \n'
                    '/afk (ausentarse) \n'
                    '/sethome (marcar un home) \n'
                    '/home "nombre" (ir a un home marcado) \n'
                    '/delhome "nombre" (borrar un home) \n'
                    '/ps add "nombre" (agregar persona a tu piedra de protección) \n'
                    '/ps remove "nombre" (quitar persona de tu piedra) \n'
                    '/tienda (ver tienda) \n'
                    '/piedras (información sobre piedra de protección) \n'
                    '/trabajos (para conseguir dinero) \n'
                    '/jobs join "nombre" (unirse a un trabajo) \n'
                    '/jobs remove "nombre" (salir de un trabajo) \n'
                    '/ec (acceder a ender chest) \n'
                    '/pay "cantidad" "nickname" (pagar a otro jugador) \n'
                    '/money (ver tu dinero) \n'
                    '/baltop (ver las personas más ricas en Olympus) \n'
                    '/ah (subasta) \n'
                    '/ah sell "precio" (vender ítem en mano en el ah) \n'
                    '/tienda (comprar piedras, torretas, etc.) \n'
                    '/warp recursos (para recolección de materiales, no recomendado construir aquí) \n'
                    '/warp matadero (conseguir comida) \n'
                    '/warp boda (iglesia) \n\n'
                    'Puedes crear ascensores colocando un bloque de cuarzo con uno de redstone debajo.',
        color=discord.Color.purple()
    )
    embed.set_footer(text='Para ver más comandos, escribe +help')
    await ctx.send(embed=embed)

keep_alive()
bot.run("BOT_TOKEN")
