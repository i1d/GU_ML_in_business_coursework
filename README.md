# GU_ML_in_business_coursework
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: catboost, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/i1dlmd/real-estate-price-prediction-gu-final/data

Задача: предсказать значение цены на недвижимость. 

Используемые признаки:

DistrictId - идентификационный номер района
Square - площадь
LifeSquare - жилая площадь
KitchenSquare - площадь кухни
Floor - этаж
HouseFloor - количество этажей в доме
HouseYear - год постройки дома
Ecology_1 - экологический показатель местности
Social_1 - социальный показатель местности
Shops_1 - показатель, связанный с наличием магазинов, торговых центров
Price - цена квартиры



Модель: CatBoostRegressor

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/ilmdn/GB_docker_flask_example.git
$ cd ml_in_business_coursework
$ docker build -t gu/ml_in_business_coursework .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8280:8280 -p 8281:8281 -v <your_local_path_to_pretrained_models>:/app/app/models gu/ml_in_business_coursework
```

### Переходим на localhost:8281
