# -*- coding: utf-8 -*-
import requests
from lxml import html


def get_number(str):
    """
    Номер участка из адресной строки
    >>> get_number("участок № 214")
    '214'
    >>> get_number("уч.№130")
    '130'
    >>> get_number("уч.№135a")
    '135a'
    >>> get_number("уч.№135 a")
    '135a'
    >>> get_number("уч.№ 135 a")
    '135a'
    """
    res = str
    for i, c in enumerate(str):
        if c.isdigit():
            res = str[i:]
            break
    # remove space
    return res.replace(" ", "")

# Результаты - выписки по кадастровым номерам
# 6 объектов
# https://xn--c1adzl.online/order?id=46aa379c-711a-4a94-b7f6-fae772a3f6db
# 34 объектов
# https://xn--c1adzl.online/order?id=5510f2eb-5081-47ca-a7a7-242ffd6e72bc
# 456 объектов
# https://егрн.online/order?id=c680020e-2a91-43f2-bde9-143520ebf826
# <https://xn--c1adzl.online/order?id=c680020e-2a91-43f2-bde9-143520ebf826>

# Подставляем URL вручную
# url = 'https://xn--c1adzl.online/order?id=46aa379c-711a-4a94-b7f6-fae772a3f6db'
# url = 'https://xn--c1adzl.online/order?id=5510f2eb-5081-47ca-a7a7-242ffd6e72bc'
# url = 'https://егрн.online/order?id=c680020e-2a91-43f2-bde9-143520ebf826'
# заказ 17.10.2019 - 245 выписок
url = 'https://егрн.online/order?id=49d85e70-4c18-475e-b602-e9b9e20c77c1'

if __name__ == "__main__":
    r = requests.get(url)
    base_url = r.url.rsplit('/', 1)[0]
    tree = html.fromstring(r.text)

    items_list = tree.xpath('//div[@class="clearfix"]')
    print(len(items_list))

    for i, item in enumerate(items_list):
        # 47:07:0162002:306 - Выписка о переходе прав на объект недвижимости
        name = item.xpath('.//p[2]/b/text()')[0].strip()
        kadastr_no = name.split("-")[0].strip()
        name = name.split("-")[-1].strip()
        # Ленинградская область, Всеволожский район, в районе пос. Стеклянный,  СНТ &quot;Березка&quot;, участок № 111
        address = item.xpath('.//p[4]/text()')[0].strip()
        number = get_number(address)
        print(i, kadastr_no, name)
        print(address, number)

        href_zip = item.xpath('.//a[1]/@href')[0]
        # print(href_zip)
        href_pdf = item.xpath('.//a[2]/@href')[0]
        # print(href_pdf)

        # download files
        r_zip = requests.get(base_url + href_zip)
        with open("doc/уч. %s %s_%s.zip" % (number, name, kadastr_no.replace(':', '_')), 'wb') as output_file:
            output_file.write(r_zip.content)
        r_pdf = requests.get(base_url + href_pdf)
        with open("doc/уч. %s %s_%s.pdf" % (number, name, kadastr_no.replace(':', '_')), 'wb') as output_file:
            output_file.write(r_pdf.content)
