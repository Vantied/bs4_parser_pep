# Парсер документации Python

Консольная утилита, которая собирает данные с docs.python.org и peps.python.org.

## Режимы работы

- `whats-new` — статьи «Что нового» для каждой версии Python с авторами и редакторами.
- `latest-versions` — версии Python, их статусы и ссылки на документацию.
- `download` — скачивает архив документации последней версии в PDF (A4).
- `pep` — обходит все PEP, считает количество документов в каждом статусе и сообщает, если статус в общей таблице не совпадает со статусом на странице PEP.

## Особенности

- Вывод в консоль, красивой таблицей (`-o pretty`) или в CSV-файл (`-o file`).
- Кеширование запросов через requests-cache, очистка кеша флагом `-c`.
- Логирование в файл с ротацией, прогресс-бар tqdm.

## Технологии

Python 3.10+, requests, requests-cache, BeautifulSoup4, lxml, PrettyTable, tqdm, argparse, pytest.

## Как запустить

```bash
git clone https://github.com/Vantied/bs4_parser_pep.git
cd bs4_parser_pep
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd src
python main.py pep -o pretty
python main.py -h             # справка по всем режимам
```

## Автор

Иван Богатов — [GitHub](https://github.com/Vantied) · Telegram [@Ivan_bogatov55](https://t.me/Ivan_bogatov55)
