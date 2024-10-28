# Recipes

Recipes - это джанго приложение, разработанное в качестве архива семейных рецептов.



## Installation

Перейдите в директорию, в которой находится requirements.txt. Cоздайте и активируйте виртуальное окружение virtualenv.

```bash
python3 -m venv venv
source venv/bin/activate
```
Установите все нужные пакеты.
```bash
pip install -r requirements.txt 
```
Создайте файл local_settings.py и поместите в него: SECRET_KEY.
```bash
touch recipes/local_settings.py 
```
Запустите проект.
```bash
python manage.py migrate 
python manage.py runserver 
```