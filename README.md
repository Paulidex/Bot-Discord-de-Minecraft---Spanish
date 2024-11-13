# Bot de Discord para Gestión de Servidor de Minecraft

Un bot de Discord en Python para administrar comunidades de servidores de Minecraft, con comandos integrados, aplicación de reglas y una conexión fluida con el servidor para mejorar la participación de los usuarios.

## Características

- **Prefijo Personalizable**: Configura un prefijo único para acceder a los comandos del bot.
- **Actualizaciones Automáticas de Estado**: Actualiza el estado del bot cada 10 segundos, mostrando en cuántos servidores está activo.
- **Comando de Ayuda Detallado**: Accede fácilmente a la lista de comandos con `+help`.
- **Comandos de Reglas Comprensivos**: Ofrece comandos separados para diferentes categorías de reglas (e.g., reglas leves, graves, del staff).
- **Integración con Servidor de Minecraft**: Proporciona la IP del servidor, comandos de juego y explicaciones de reglas.
- **Operación Continua en Replit**: Mantiene el bot activo en Replit y evita su desconexión utilizando un servidor web minimalista en Flask y UptimeRobot.

## Documentación y Archivos de Código

El proyecto incluye cuatro archivos principales:

1. **Dos Archivos Documentados**: Contienen comentarios y explicaciones detalladas del código, ideales para aquellos que desean comprender a fondo la funcionalidad y estructura del bot.
2. **Dos Archivos Sin Documentación**: Proporcionan una versión simplificada sin comentarios, pensada para el despliegue o para quienes prefieren trabajar con un código más limpio.

Tener tanto versiones documentadas como no documentadas permite a los usuarios elegir el archivo que mejor se adapte a sus necesidades, ya sea para estudiar el código o para un despliegue eficiente y sin distracciones.

## Requisitos

- **Python 3.6+**
- Biblioteca `discord.py` para la interacción con la API de Discord.
- `Flask` para la funcionalidad del servidor web.

Instala las dependencias con:
```bash
pip install discord flask
```

## Uso

### 1. Clona o Descarga el Proyecto
   
   ```bash
   git clone https://github.com/tuusuario/minecraft-discord-bot.git
   cd minecraft-discord-bot
   ```

### 2. Configura Tu Token de Bot

   Reemplaza `"YOUR_BOT_TOKEN"` en la función `bot.run()` con tu token de bot de Discord.

### 3. Sube el Proyecto a Replit

   - Sube el código a Replit y ejecuta el bot en la nube para mantenerlo activo.
   - Configura el bot para usar un servidor web "Keep Alive" en Replit para que UptimeRobot pueda monitorearlo y mantenerlo en funcionamiento.

### 4. Configura Uptime con UptimeRobot

   Para mantener el bot activo las 24/7, sigue estos pasos en [UptimeRobot](https://uptimerobot.com):

   - Crea una cuenta en UptimeRobot y selecciona “Agregar Nuevo Monitor”.
   - Elige el tipo de monitor HTTP.
   - Ingresa la URL de tu proyecto desde Replit (ej. `https://tu-repl-nombre.tu-usuario.repl.co`).
   - Establece la frecuencia de verificación (recomendado cada 5 minutos).
   - Esto permitirá que UptimeRobot revise continuamente tu proyecto en Replit, evitando que se desconecte.

### 5. Ejecuta el Bot en Replit
   
   Inicia el bot en Replit ejecutando `python bot.py`. Mientras UptimeRobot monitoree tu página de Replit, el bot permanecerá activo.

## Comandos

### Comandos Generales

- **`+help`**: Muestra todos los comandos y descripciones.
- **`+ip`**: Muestra la dirección IP del servidor de Minecraft.
- **`+tienda`**: Comparte un enlace a la tienda de donaciones en línea del servidor.
- **`+normas`**: Introduce las reglas del servidor, categorizadas por severidad.

### Comandos de Reglas

Cada comando a continuación proporciona reglas específicas del servidor:

- **`+leves`**: Violaciones menores de reglas.
- **`+graves`**: Violaciones graves de reglas.
- **`+juicio`**: Reglas de juicio.
- **`+staff`**: Reglas específicas del staff.
- **`+clanes`**: Reglas de clanes.

### Comandos de Minecraft

- **`+comandos`**: Muestra todos los comandos disponibles en el juego, como teletransporte y economía.

## Operación Continua con UptimeRobot y Replit

Para evitar que el bot se desconecte, especialmente en Replit, el proyecto está configurado con una página web en Replit y se mantiene activo mediante UptimeRobot, que verifica su disponibilidad continuamente.

## Tutorial

Para una guía de configuración visual detallada, sigue el siguiente tutorial en YouTube:  
[![Tutorial en YouTube](https://img.youtube.com/vi/SPTfmiYiuok/0.jpg)](https://youtu.be/SPTfmiYiuok)

Este video muestra cómo subir el bot a Replit y configurarlo con UptimeRobot para mantenerlo activo las 24 horas del día, los 7 días de la semana.
