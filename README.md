# 🍽 Home Recipe Telegram Bot

Простой Telegram-бот, который предлагает быстрые домашние рецепты по запросу — на завтрак, обед или ужин.

## Как пользоваться

Напишите боту:
- `что на завтрак?`
- `что на обед?`
- `что на ужин?`

Или нажмите кнопку на клавиатуре. Бот пришлёт случайный рецепт с ингредиентами и шагами приготовления.

---

## Установка и запуск

### 1. Создай бота в Telegram

1. Открой [@BotFather](https://t.me/BotFather) в Telegram
2. Напиши `/newbot` и следуй инструкциям
3. Скопируй полученный токен

### 2. Клонируй репозиторий

```bash
git clone https://github.com/pyroman30/home-recipe-telegram-bot.git
cd home-recipe-telegram-bot
```

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Задай токен

Скопируй `.env.example` в `.env` и вставь свой токен:

```bash
cp .env.example .env
```

Отредактируй `.env`:
```
TELEGRAM_BOT_TOKEN=твой_токен_здесь
```

Загрузи переменную окружения:

```bash
# Linux/macOS
export $(cat .env | xargs)

# Windows PowerShell
$env:TELEGRAM_BOT_TOKEN="твой_токен"
```

### 5. Запусти бота

```bash
python bot.py
```

---

## Структура проекта

```
├── bot.py          # Основной код бота
├── recipes.py      # База рецептов
├── requirements.txt
├── .env.example
└── .gitignore
```

## Добавление рецептов

Открой `recipes.py` и добавь новый рецепт в нужный раздел (`завтрак`, `обед`, `ужин`) по образцу:

```python
{
    'name': 'Название рецепта',
    'time': '15 минут',
    'ingredients': ['ингредиент 1', 'ингредиент 2'],
    'steps': ['Шаг 1', 'Шаг 2']
}
```
