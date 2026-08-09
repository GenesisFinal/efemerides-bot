import os
import sys
import time
import tweepy
from datetime import datetime

# Autenticación desde variables de entorno de GitHub o valores fallback
API_KEY = os.environ.get("X_API_KEY", "4yCRi8uVLirR7zk2k3AxfTAeS")
API_SECRET = os.environ.get("X_API_SECRET", "exFOhMMZA14PM2V618vcfTSphz0aoiVRn3Ltou0XinOKZOOHZH")
ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN", "YjNIWU8xa0dTR2F3emtxOVFEanUyazhWQXBmMklEYkJuSnUwODRYWFhhT2JIOjE3ODYyMzA1MzEzOTQ6MToxOmF0OjE")

POSTS = [
    {
        "time": "08:40",
        "text": "Un 9 de agosto de 1821 se oficializaba la creación de la Universidad de Buenos Aires (UBA) bajo la gestión de Martín Rodríguez y Bernardino Rivadavia. Cuna académica de 5 Premios Nobel e institución insignia de la educación argentina. 🇦🇷🎓\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/uba_fundacion_1821_clay.jpg"
    },
    {
        "time": "08:50",
        "text": "El 9 de agosto de 1945, la bomba atómica \"Fat Man\" explotó sobre Nagasaki. Liberó 21 kilotones de TNT y cobró más de 70.000 vidas, acelerando el fin de la Segunda Guerra Mundial y dejando una huella imborrable. 🇯🇵🕊️\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/nagasaki_atomic_1945_clay.jpg"
    },
    {
        "time": "09:00",
        "text": "El 9 de agosto de 1974, acorralado por el escándalo de espionaje político Watergate y la inminencia de un juicio político, Richard Nixon presentó su renuncia a la presidencia de los Estados Unidos. Un hito sin precedentes en la historia política global. 🇺🇸📜\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/nixon_resignation_1974_clay.jpg"
    },
    {
        "time": "09:10",
        "text": "¡Debut de una leyenda de la animación! El 9 de agosto de 1930, Betty Boop apareció por primera vez en pantalla en el corto \"Dizzy Dishes\" de Fleischer Studios. De caniche animado a ícono eterno de la era del jazz. 🎨✨\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/betty_boop_1930_clay.jpg"
    },
    {
        "time": "09:20",
        "text": "El 9 de agosto de 1988 falleció Ramón Valdés, el inolvidable \"Don Ramón\" en El Chavo del 8. Con su carisma único e interpretación entrañable, conquistó a generaciones enteras en toda América Latina y España. 🇲🇽🎭\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/don_ramon_valdes_clay.jpg"
    },
    {
        "time": "09:30",
        "text": "El 9 de agosto de 2013 nos dejaba Eduardo Falú, virtuosísimo guitarrista y compositor salteño. Coautor de piezas inmortales como \"Zamba de la Candelaria\" y \"La tonada del viejo amor\", referencia ineludible del folclore argentino. 🎸🇦🇷\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/eduardo_falu_guitar_clay.jpg"
    },
    {
        "time": "09:40",
        "text": "Un 9 de agosto de 1963 nacía Whitney Houston, una de las voces más portentosas en la historia de la música. Ganadora de 6 premios Grammy y récord absoluto de ventas con \"El Guardaespaldas\". Su voz sigue marcando época. 🎤✨\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/whitney_houston_clay.jpg"
    },
    {
        "time": "09:50",
        "text": "El 9 de agosto de 1986, en Knebworth Park ante más de 100.000 personas, Queen ofreció su último concierto en vivo con Freddie Mercury. El cierre legendario del \"Magic Tour\" que pasó a la historia grande del rock mundial. 🎸👑\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/queen_knebworth_1986_clay.jpg"
    },
    {
        "time": "10:00",
        "text": "El 9 de agosto de 1936, el mítico Jesse Owens ganaba su 4ta medalla dorada en los JJ.OO. de Berlín al triunfar en el relevo 4x100m. Una gesta deportiva y un golpe histórico a la propaganda de supremacía aria nazi. 🏅🏃‍♂️\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/jesse_owens_plastilina.jpg"
    },
    {
        "time": "10:10",
        "text": "El 9 de agosto de 1914 fallecía el presidente argentino Roque Sáenz Peña. Su legado imperecedero: la Ley 8.871 de 1912 que instauró el voto secreto, universal y obligatorio en la República Argentina. 🗳️🇦🇷\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/roque_saenz_pena_clay.jpg"
    },
    {
        "time": "10:20",
        "text": "El 9 de agosto de 1956, la incorporación de los aviones Corsair F4U-5 dio nacimiento formal a la Segunda Escuadrilla Aeronaval de Caza y Ataque de la Armada Argentina, con heroica actuación posterior en Malvinas. ✈️🇦🇷\n\nMás acá: https://elactuario.substack.com/p/efemerides-del-9-de-agosto",
        "image": "images/escuadrilla_aeronaval_clay.jpg"
    }
]

def publish_all_with_delays():
    client = tweepy.Client(
        consumer_key=API_KEY,
        consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN
    )
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET)
    api_v1 = tweepy.API(auth)
    
    print("Iniciando secuencia de publicación en GitHub Actions...")
    for idx, post in enumerate(POSTS):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Publicando posteo {idx+1}/{len(POSTS)} ({post['time']} hs)...")
        try:
            media_id = None
            if os.path.exists(post['image']):
                media = api_v1.media_upload(post['image'])
                media_id = media.media_id
                print(f"  -> Imagen subida OK: {post['image']}")
            
            if media_id:
                res = client.create_tweet(text=post['text'], media_ids=[media_id])
            else:
                res = client.create_tweet(text=post['text'])
            print(f"  ✅ TWEET PUBLICADO! ID: {res.data['id']}")
        except Exception as e:
            print(f"  ❌ ERROR al publicar: {e}")
            
        if idx < len(POSTS) - 1:
            print("  -> Esperando 10 minutos (600 s) para el siguiente posteo...")
            time.sleep(600)

if __name__ == "__main__":
    publish_all_with_delays()
