import discord  # Importa la biblioteca de discord.py para interactuar con la API de Discord.
from discord.ext import commands, tasks  # Importa módulos adicionales para manejar comandos y tareas en bucle con discord.py.
from webserver import keep_alive  # Importa una función personalizada `keep_alive` para mantener el bot en línea.
import datetime  # Importa la biblioteca `datetime` para manejar y manipular fechas y horas.
import asyncio  # Importa asyncio para funciones asíncronas, esenciales para operaciones no bloqueantes.
from urllib import parse, request  # Importa módulos para trabajar con URLs y hacer solicitudes HTTP.
import re  # Importa el módulo de expresiones regulares `re` para analizar patrones de texto.

# Configuración de permisos del bot (intents)
# Discord permite a los bots utilizar "intenciones" o "intents" para definir a qué eventos y datos pueden acceder.
# Estos intents controlan los permisos del bot de manera específica, mejorando la seguridad y privacidad en Discord.

# Primero, se crea un objeto de intents llamado `intents`, utilizando `discord.Intents.default()`.
# `discord.Intents.default()` devuelve un conjunto básico de permisos predefinidos que el bot puede utilizar.
intents = discord.Intents.default()  

# A continuación, se activa el permiso específico `message_content` en el objeto `intents`.
# `message_content` es un permiso que permite al bot acceder al texto de los mensajes en los canales de texto.
# Este permiso es fundamental para que el bot pueda leer y responder a comandos de los usuarios.
# Sin este permiso, el bot no puede ver el contenido del mensaje y, por lo tanto, no puede responder a los comandos.
intents.message_content = True  

# Creación del bot
# Se inicializa el bot utilizando la clase `commands.Bot` de discord.py, configurando el prefijo de comando,
# desactivando el comando de ayuda predeterminado y asignando los intents configurados.

# - `command_prefix="+":` Define el prefijo que los usuarios deben utilizar para los comandos del bot, en este caso `+`.
#    Esto significa que cualquier comando debe comenzar con `+`.
# - `help_command=None`: Desactiva el comando de ayuda predeterminado de `discord.py`, permitiendo definir un comando de ayuda personalizado.
# - `intents=intents`: Pasa el objeto `intents` con los permisos configurados, necesario para que el bot funcione correctamente con los permisos establecidos.
bot = commands.Bot(command_prefix="+", help_command=None, intents=intents)


# Evento de inicialización del bot
# `@bot.event` es un decorador que indica que la función siguiente es un evento de discord.py.
# Los eventos en discord.py son funciones que se activan automáticamente al ocurrir ciertos sucesos en Discord.

# La función `on_ready` se define como asincrónica utilizando `async def`, lo cual permite al bot realizar 
# múltiples tareas a la vez sin bloquear otras operaciones. Esto es útil en entornos donde el bot
# debe responder rápidamente y manejar múltiples eventos al mismo tiempo, como mensajes o comandos.

# `on_ready` representa el evento que ocurre cuando el bot se conecta a Discord y está listo para ser utilizado.
# Este evento se activa una sola vez, cuando el bot se ha conectado y ha cargado toda la información necesaria.
@bot.event
async def on_ready():
    # La función imprime el mensaje "El bot está listo" en la consola para indicar al programador que el bot se ha conectado correctamente.
    # Este mensaje de confirmación ayuda a verificar que la conexión ha sido exitosa.
    print('El bot está listo')


# Tarea en bucle para cambiar el estado del bot
# `@tasks.loop` es un decorador que permite crear una tarea en bucle que se ejecuta repetidamente con un intervalo especificado.
# En este caso, se establece un intervalo de 10 segundos, lo que significa que la función siguiente se ejecutará cada 10 segundos.

@tasks.loop(seconds=10)
async def change_status():
    # La función `change_status` se define como asincrónica (usando `async def`), permitiendo que el bot realice esta
    # tarea en paralelo con otras tareas, sin bloquear el procesamiento de otros eventos.

    # `await` indica que el bot debe esperar hasta que `change_presence` complete su ejecución antes de continuar.
    # Esto permite que otras tareas se ejecuten mientras el bot espera, evitando bloqueos en el funcionamiento del bot.

    # `bot.change_presence` es un método que cambia el estado visible del bot en Discord.
    # Aquí, el bot muestra un mensaje en su estado de "jugando", indicando en cuántos servidores está y su prefijo de comando.
    # `len(bot.guilds)` obtiene el número de servidores en los que el bot está presente.
    await bot.change_presence(activity=discord.Game(name="En " + str(len(bot.guilds)) + " servidores. Prefijo +"))


# Comando de ayuda que muestra un mensaje incrustado (embed) con la lista de comandos del bot.
# `@bot.command` es un decorador que convierte la función siguiente en un comando accesible para los usuarios.
# Al usar `@bot.command(name='help')`, se define un comando `+help` que los usuarios pueden escribir para ver la lista de comandos.

@bot.command(name='help')
async def help(ctx):
    # La función `help` es asincrónica, lo que permite al bot manejar esta tarea sin bloquear otras operaciones.
    # La función recibe un parámetro `ctx`, que representa el contexto en el que se llamó al comando y permite acceder
    # al canal donde se debe enviar la respuesta.

    # Crea un mensaje "embed" o incrustado, que es un mensaje estilizado con título, descripción, campos y otros detalles.
    embed = discord.Embed(
        title='Comandos',  # Título del embed
        description='Aquí están los comandos que puedes utilizar para mejorar tu experiencia en Discord y en el servidor de Minecraft.',
        color=discord.Color.purple()  # Color del borde del embed, en este caso morado
    )
    # emebed.add_field (name = 'comando', value = 'descripción', inline = False)
    # Usa `add_field` para añadir cada comando con su respectiva descripción en el embed.
    # El parámetro `name` especifica el nombre del campo (comando), y `value` especifica la descripción.
    # `inline=False` hace que cada campo se muestre en una línea separada.
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
    
    # `embed.set_footer` permite incluir una sección en la parte inferior del mensaje incrustado.
    # Este pie de página puede contener texto que permanezca fijo y visible independientemente de los campos añadidos en el embed.
    # En este caso, el pie de página proporciona información de contacto, indicando cómo comunicarse para contrataciones.
    embed.set_footer(text='Para contrataciones, contactar a Paulidex#9510.')

    # `ctx.send` es un método que envía un mensaje al canal en el que se llamó al comando.
    # `ctx` es el contexto del comando que contiene información sobre cómo y dónde se utilizó, incluyendo el canal y el usuario que ejecutó el comando.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.

    # Aquí, `embed=embed` indica que se enviará el mensaje en formato embed, utilizando el mensaje incrustado
    # que fue definido previamente con el título, descripción, comandos y pie de página.
    await ctx.send(embed=embed)

# Comando para verificar si el bot está funcionando
# `@bot.command()` es un decorador que convierte la función siguiente en un comando de bot.
# Aquí se define un comando sin nombre específico, lo que significa que su nombre será el mismo que el de la función: `a`.
# Los usuarios pueden escribir `+a` para ejecutar este comando y comprobar si el bot está activo.

@bot.command()
async def a(ctx):
    # La función `a` es asincrónica, permitiendo que el bot responda a este comando sin bloquear otras operaciones.
    # El parámetro `ctx` (contexto) contiene información sobre el lugar donde se llamó al comando,
    # incluyendo el canal en el que debe enviarse la respuesta.

    # `ctx.send` es el método que envía un mensaje en el canal desde el que se llamó el comando.
    # Aquí se envía el mensaje "El bot está funcionando correctamente" como confirmación de que el bot está activo.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send('El bot está funcionando correctamente')  # Envía el mensaje de confirmación como prueba.


# Comando para enviar un enlace a la tienda de donaciones
# `@bot.command()` es un decorador que convierte la función siguiente en un comando del bot.
# Aquí se define un comando sin nombre específico, por lo que el nombre del comando será el mismo que el de la función: `tienda`.
# Los usuarios pueden escribir `+tienda` para ejecutar este comando y recibir el enlace de la tienda de donaciones.

@bot.command()
async def tienda(ctx):
    # La función `tienda` es asincrónica, lo que permite que el bot responda a este comando sin bloquear otras operaciones.
    # El parámetro `ctx` (contexto) proporciona información sobre el lugar donde se llamó al comando,
    # incluyendo el canal en el que debe enviarse la respuesta.

    # `ctx.send` es el método que envía un mensaje en el canal desde el cual se llamó el comando.
    # Aquí, el mensaje enviado incluye el enlace a la tienda de donaciones con un mensaje amigable.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send('Visita nuestra tienda para ver nuestros rangos y realizar donaciones ^.^ `https://olympusland.tebex.io`')


# Comando para mostrar la IP del servidor de Minecraft
# `@bot.command()` es un decorador que convierte la función siguiente en un comando del bot.
# Como no se especifica un nombre, el comando usará el nombre de la función: `ip`.
# Los usuarios pueden escribir `+ip` para ejecutar este comando y recibir la IP del servidor de Minecraft.

# Comando que muestra la IP del servidor de Minecraft
# `@bot.command()` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Al no especificar un nombre en el decorador, el comando se ejecutará escribiendo `+ip`, permitiendo que los usuarios vean la IP del servidor.

@bot.command()
async def ip(ctx):
    # Define `ip` como una función asincrónica para que el bot pueda manejar este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # Un embed es un mensaje visualmente estructurado que permite incluir un título, descripción, color, y más,
    # ofreciendo un formato organizado y atractivo para los usuarios.

    # En este embed:
    # - `title='Servidor Minecraft Java'` establece el título del embed, que se mostrará en la parte superior y en un tamaño de texto más grande.
    # - `description='...'` define el contenido principal, que incluye la IP del servidor y las versiones compatibles.
    # - `color=discord.Color.purple()` establece un color morado para el borde del embed, lo que lo hace visualmente destacado.
    embed = discord.Embed(
        title='Servidor Minecraft Java',  # Título del embed
        description='Versión 1.16.5 - 1.17.1: play.olympusland.xyz',  # Descripción con la IP y versiones del servidor
        color=discord.Color.purple()  # Color del borde del embed
    )

    # Añade un pie de página al embed para proporcionar contexto adicional.
    # `set_footer` coloca un texto en la parte inferior del embed. En este caso, el pie de página sugiere al usuario
    # que escriba `+help` para ver otros comandos del bot.
    embed.set_footer(text='Para ver más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, mostrando la IP y versiones del servidor de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)


# Comando que muestra cómo acceder a las normas del servidor
# `@bot.command()` es un decorador que convierte la función siguiente en un comando del bot.
# Como no se especifica un nombre, el comando usará el nombre de la función: `normas`.
# Los usuarios pueden escribir `+normas` para ejecutar este comando y recibir información sobre cómo ver las normas del servidor.

@bot.command()
async def normas(ctx):
    # La función `normas` es asincrónica, lo cual permite que el bot responda a este comando sin bloquear otras operaciones.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde se llamó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `ctx.send` es el método que envía un mensaje en el canal donde se activó el comando.
    # Aquí, el mensaje informa que las normas están clasificadas y sugiere comandos para ver cada tipo de norma.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send('Las normas están clasificadas en graves, leves, staff y juicio. Para verlas, escribe `+graves` `+leves` `+staff` `+juicio` `+clanes`')


# Comando que muestra las normas leves del servidor
# `@bot.command(name='leves')` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Con `name='leves'`, el comando se ejecuta escribiendo `+leves`, permitiendo que los usuarios vean las normas leves.

@bot.command(name='leves')
async def leves(ctx):
    # Define `leves` como una función asincrónica para permitir que el bot maneje este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo al bot enviar la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # Un embed es un mensaje visualmente estructurado que permite incluir un título, descripción, color, y más,
    # ofreciendo un formato organizado y atractivo para los usuarios.

    # En este embed:
    # - `title='Normas Leves'` establece el título del embed, que se mostrará en la parte superior y en un tamaño de texto más grande.
    # - `description='...'` define el contenido principal, que enumera las normas leves del servidor.
    # - `color=discord.Color.purple()` establece un color morado para el borde del embed, lo que lo hace visualmente destacado.
    embed = discord.Embed(
        title='Normas Leves',  # Título del embed
        description='1) Los bugs están permitidos, pero antes debes consultar su uso con alguien del staff. \n'
                    '2) No insultar a otros jugadores si no es de su agrado. \n'
                    '3) Evita hacer flood (ejemplo: holaaaaaa), spam o texto innecesario que sature el chat. \n'
                    '4) No se permite tener más de dos relojes de Redstone; generadores de lag y cargadores de chunks están prohibidos. \n'
                    '5) Las mascotas son propiedad privada; está prohibido matarlas intencionalmente, aunque no estén en una zona protegida. \n'
                    '6) Los lobos no pueden ser utilizados como armas para PVP. \n'
                    '7) En caso de problemas aislados, el staff puede realizar reuniones para encontrar una solución justa. \n'
                    '8) No salirse de un juicio.',  # Normas leves listadas en la descripción
        color=discord.Color.purple()  # Borde morado
    )

    # Añade un pie de página al embed para proporcionar contexto adicional.
    # `set_footer` coloca un texto en la parte inferior del embed. Aquí se sugiere al usuario que escriba `+help` para ver más comandos
    # y se le informa que las normas son acumulativas.
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, que presenta las normas de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)

# Comando que muestra las normas graves del servidor
# `@bot.command(name='graves')` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Con `name='graves'`, el comando se ejecuta escribiendo `+graves`, permitiendo que los usuarios vean las normas graves.

@bot.command(name='graves')
async def graves(ctx):
    # Define `graves` como una función asincrónica para permitir que el bot maneje este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # El embed contiene un título, una descripción con las normas graves y un color de borde.
    embed = discord.Embed(
        title='Normas Graves',  # Título del embed
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
                    '16) No explorar, minar o talar en el mundo normal; utiliza /warp recursos.',  # Normas graves listadas en la descripción
        color=discord.Color.purple()  # Color morado para el borde del embed
    )

    # Añade un pie de página al embed para proporcionar contexto adicional.
    # `set_footer` coloca un texto en la parte inferior del embed. Aquí se sugiere al usuario escribir `+help` para ver más comandos
    # y se le informa que las normas son acumulativas.
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, que presenta las normas de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)

# Comando que muestra las normas de juicio
# `@bot.command(name='juicio')` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Con `name='juicio'`, el comando se ejecuta escribiendo `+juicio`, permitiendo que los usuarios vean las normas aplicables en el juicio.

@bot.command(name='juicio')
async def juicio(ctx):
    # Define `juicio` como una función asincrónica para permitir que el bot maneje este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # El embed contiene un título, una descripción con las normas de juicio y un color de borde.
    embed = discord.Embed(
        title='Normas del Juicio',  # Título del embed
        description='1) No interrumpir el juicio. \n'
                    '2) Presentar pruebas. \n'
                    '3) No hacer perder el tiempo al staff que actúe como juez. \n'
                    '4) Leer las normas antes de solicitar un juicio. \n'
                    '5) Solo se permite la presencia de testigos y partes involucradas en el juicio. \n'
                    '6) Solo Owners, Admins y Mods pueden actuar como jueces. \n'
                    '7) Ambas partes (acusados y acusadores) deben estar presentes.',  # Normas del juicio listadas en la descripción
        color=discord.Color.purple()  # Color morado para el borde del embed
    )

    # Añade un pie de página al embed para proporcionar contexto adicional.
    # `set_footer` coloca un texto en la parte inferior del embed. Aquí se sugiere al usuario escribir `+help` para ver más comandos
    # y se le informa que las normas son acumulativas.
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, que presenta las normas de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)


# Comando que muestra las normas de los clanes
# `@bot.command(name='clanes')` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Con `name='clanes'`, el comando se ejecuta escribiendo `+clanes`, permitiendo que los usuarios vean las normas aplicables a los clanes.

@bot.command(name='clanes')
async def clanes(ctx):
    # Define `clanes` como una función asincrónica para permitir que el bot maneje este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # El embed contiene un título, una descripción con las normas de clanes y un color de borde.
    embed = discord.Embed(
        title='Normas de los Clanes',  # Título del embed
        description='1) Todo tipo de PVP es válido si ambos jugadores pertenecen a un clan. \n'
                    '2) Se permite el grifeo, pero solo a bases de clanes.',  # Normas de clanes en la descripción
        color=discord.Color.purple()  # Color morado para el borde del embed
    )

    # Añade un pie de página al embed para proporcionar contexto adicional.
    # `set_footer` coloca un texto en la parte inferior del embed. Aquí se sugiere al usuario escribir `+help` para ver más comandos
    # y se le informa que las normas son acumulativas.
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, que presenta las normas de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)

# Comando que muestra las normas del staff
# `@bot.command(name='staff')` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Con `name='staff'`, el comando se ejecuta escribiendo `+staff`, permitiendo que los usuarios vean las normas aplicables al staff.

@bot.command(name='staff')
async def staff(ctx):
    # Define `staff` como una función asincrónica para permitir que el bot maneje este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # El embed contiene un título, una descripción con las normas del staff y un color de borde.
    embed = discord.Embed(
        title='Normas del Staff',  # Título del embed
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
                    '11) No revelar novedades en desarrollo a jugadores.',  # Normas del staff listadas en la descripción
        color=discord.Color.purple()  # Color morado para el borde del embed
    )

    # Añade un pie de página al embed para proporcionar contexto adicional.
    # `set_footer` coloca un texto en la parte inferior del embed. Aquí se sugiere al usuario escribir `+help` para ver más comandos
    # y se le informa que las normas son acumulativas.
    embed.set_footer(text='Las normas se acumulan y los castigos pueden variar según la persona. Para más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, que presenta las normas de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)

# Comando que muestra los comandos utilizables en el servidor
# `@bot.command(name='comandos')` convierte la función siguiente en un comando del bot accesible para los usuarios.
# Con `name='comandos'`, el comando se ejecuta escribiendo `+comandos`, permitiendo que los usuarios vean una lista de comandos disponibles en el servidor.

@bot.command(name='comandos')
async def comandos(ctx):
    # Define `comandos` como una función asincrónica para permitir que el bot maneje este comando sin interferir con otras tareas.
    # El parámetro `ctx` (contexto) proporciona información sobre dónde y cómo se ejecutó el comando,
    # permitiendo que el bot envíe la respuesta en el mismo canal.

    # `embed = discord.Embed(...)` crea un mensaje embebido o "embed" para presentar la información de manera estilizada.
    # El embed contiene un título, una descripción con la lista de comandos del servidor y un color de borde.
    embed = discord.Embed(
        title='Comandos que puedes usar en el servidor',  # Título del embed
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
                    'Puedes crear ascensores colocando un bloque de cuarzo con uno de redstone debajo.',  # Comandos del servidor listados en la descripción
        color=discord.Color.purple()  # Color morado para el borde del embed
    )

    # Añade un pie de página al embed.
    # `set_footer` coloca un texto en la parte inferior del embed. En este caso, sugiere al usuario escribir `+help` para ver otros comandos.
    embed.set_footer(text='Para ver más comandos, escribe +help')

    # Envía el mensaje embed en el canal donde el usuario ejecutó el comando.
    # `ctx.send(embed=embed)` utiliza el contexto (`ctx`) para enviar el embed, que presenta los comandos de forma organizada.
    # `await` se utiliza para esperar a que se complete el envío del mensaje antes de continuar con otras operaciones.
    await ctx.send(embed=embed)


# Llama a la función keep_alive para mantener el bot en línea en un servidor web.
keep_alive()

# Inicia el bot. Reemplaza "BOT_TOKEN" con el token real del bot de Discord.
bot.run("BOT_TOKEN")
