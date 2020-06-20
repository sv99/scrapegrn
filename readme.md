scrap egrn results
==================

10.09.2019

Получены на почту ссылки на результаты запросов по кадастровым номерам.
На страничках ссылки на файлы по каждому объекту.

3 запроса - 6, 34 и 456 объектов

**Решение**

Простейший последовательный скраппинг.

В выписке информация о каждом объекте хранится в блоке `<div class="clearfix">`

```html
<div class="clearfix">
    <p>
        <b class="text-success">
            готово                    </b>
    </p>
    <p>
        <b>47:07:0162002:306 - Выписка о переходе прав на объект недвижимости</b>
    </p>
    <p>
    </p>
    <p>
        Ленинградская область, Всеволожский район, в районе пос. Стеклянный,  СНТ &quot;Березка&quot;, участок № 111                </p>
                        <p>
            Скачать
            <a class="btn btn-default btn-xs" target="_blank" rel="nofollow" href="/order/download?id=0dc2c46c-ce06-418f-b6da-9173e018b2fb&format=xml">zip с ЭЦП</a>
            <a class="btn btn-default btn-xs" target="_blank" rel="nofollow" href="/order/download?id=0dc2c46c-ce06-418f-b6da-9173e018b2fb&format=pdf">pdf</a>
            <a class="btn btn-default btn-xs" target="_blank" rel="nofollow" href="/order/download?id=0dc2c46c-ce06-418f-b6da-9173e018b2fb&format=html">html</a>
        </p>
    
</div>
```

Инициализация
-------------

```bash
pyenv local 3.7
python -m venv venv
./venv/bin activate
pip install pipenv

# initial
pipenv install requests lxml
# restore environment from Pipfile.lock

pipenv install --system
```  

Запуск
------

Сейчас нужно прописать URL вручную.

Дополнительная конфигурация для запуска doctest для функции get_number()

**18.10.19** еще одна выписка на 245 объектов. Выяснилось, что есть два кадастровых номера
для участка 195 - для того, чтобы не перетирался файл добавил в конец
кадастровый номер 47:07:0162002:89 -> 47_07_0162002_89
