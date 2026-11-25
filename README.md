
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone
cd what_to_watch
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Или для пользователей Windows:

```bash
source env/Scripts/activate
```

Установить зависимости:

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Настроить переменные окружения (создать файл `.env`):

```bash
FLASK_APP=opinions_app
FLASK_DEBUG=1
```

Инициализировать и применить миграции:

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

Загрузить начальные данные из CSV:

```bash
flask load_opinions
```

Запустить проект:

```bash
flask run
```
