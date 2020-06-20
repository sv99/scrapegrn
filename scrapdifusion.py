# -*- coding: utf-8 -*-
# svolkov 23.09.2019
#
# загрузка электронной версии учебников, доступных на https://campus.difusion.com/sections/librosdigitales
# для доступа к книге генерируется уникальный URL - по нему получаем JPG картинки с amazonaws.com
# URL получаем из инструментов разработчика
#
import requests

if __name__ == "__main__":
    server = "https://dif-unity-prod.s3.amazonaws.com/system/uploads/content/file"
    uid = "da4ad7ce-d575-4b61-88fd-b3395803b064" # Aula3 Internacional, 252 paginas
    #uid = "56c14168-61a8-4830-9790-5352a2e23630" # Aula4 Internacional
    #uid = "b33bee24-7130-41e7-b958-b705a000e335" # Aula5 Internacional
    #uid = "69b20c22-f693-4ca4-af09-62cfc9c8e4bb" # Expertos B2
    #uid = "59e69a9e-7f4e-4a49-80b1-798b3e336e66" # Gente Hoy 3, 317 paginas

    for i in range(250, 300):
        url = "%s/%s/media/%d.jpg" % (server, uid, i)
        print(i, url)
        r = requests.get(url)
        if r.status_code != 200:
            print("Return status_code: %d" % r.status_code)
            continue
        with open("doc/%d.jpg" % i, 'wb') as output_file:
            output_file.write(r.content)

