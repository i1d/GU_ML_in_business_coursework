# GU_ML_in_business_coursework
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: catboost, pandas, numpy<br>
API: flask<br>
Данные: с kaggle - https://www.kaggle.com/i1dlmd/real-estate-price-prediction-gu-final/data

Задача: предсказать значение цены на недвижимость. 

Используемые признаки:

DistrictId - идентификационный номер района<br>
Square - площадь<br>
LifeSquare - жилая площадь<br>
KitchenSquare - площадь кухни<br>
Floor - этаж<br>
HouseFloor - количество этажей в доме<br>
HouseYear - год постройки дома<br>
Ecology_1 - экологический показатель местности<br>
Social_1 - социальный показатель местности<br>
Shops_1 - показатель, связанный с наличием магазинов, торговых центров<br>
Price - цена квартиры



Модель: CatBoostRegressor

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/i1d/GU_ML_in_business_coursework.git
$ cd GU_ML_in_business_coursework
$ docker build -t gu/ml_in_business_coursework .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8280:8280 -p 8281:8281 -v <your_local_path_to_pretrained_models>:/app/app/models gu/ml_in_business_coursework
```

### Переходим на localhost:8281
