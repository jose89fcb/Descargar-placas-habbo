import requests
import os
import json
import pathlib

os.system("cls")
HabboNombre = input("Escribe el habbo Nombre: ")
os.system("cls")
HabboHotel= input("Escribe el hotel: ")
habbo = requests.get(f"https://www.habbo.{HabboHotel}/api/public/users?name={HabboNombre}")
os.system("cls")
HabboID= habbo.json()['uniqueId']

url = f"https://www.habbo.com/api/public/users/{HabboID}/badges"
data = requests.get(url).json()

Carpeta=input("Escribe el nombre de la carpeta: ")
os.system("cls")
pathlib.Path(f"{Carpeta}").mkdir(parents=True, exist_ok=True)
os.chdir(os.path.join(os.getcwd(),f"{Carpeta}")) 

#os.mkdir(os.path.join(os.getcwd(),Carpeta))


i = 1
reemplazar="https://images.habbo.com/c_images/album1584/"
for key in data:
    link="asda"
    
    try:

     link = 'https://images.habbo.com/c_images/album1584/' + key['code']+".png"
    except TypeError:
     link=f"{reemplazar}"
     print(f"{HabboNombre} No tiene placas en su perfil")
        
    
    response = requests.get(link)

    
    try:

     NombreArchivo = data[0]['code']
    except KeyError:
     NombreArchivo=""    
    if response.status_code == 200:
        if link and not "image/png;" in link:
            with open(f"{link}".replace(f"{reemplazar}",""), "wb") as f:
                img = requests.get(link)
                f.write(img.content)
                print(f"Descargando...",i, link.replace(f"{reemplazar}","").replace(".png",""))
            i += 1