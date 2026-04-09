import logging
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from recipes import RECIPES

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

MEAL_KEYWORDS = {
    'завтрак': ['завтрак', 'завтраку', 'завтрака', 'позавтракать'],
    'обед': ['обед', 'обеду', 'обеда', 'пообедать'],
    'ужин': ['ужин', 'ужину', 'ужина', 'поужинать'],
}

KEYBOARD = [['🍳 Завтрак', '🍲 Обед', '🍽 Ужин']]


def detect_meal_type(text: str) -> str | None:
    text = text.lower()
    for meal, keywords in MEAL_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return meal
    return None


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(KEYBOARD, resize_keyboard=True)
    await update.message.reply_text(
        '👋 Привет! Я помогу тебе решить, что приготовить.\n\n'
        'Спроси меня: *что на завтрак?*, *что на обед?* или *что на ужин?*',
        parse_mode='Markdown',
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    meal = detect_meal_type(text)

    if meal is None:
        await update.message.reply_text(
            '🤔 Не понял запрос. Спроси меня:\n'
            '• что на завтрак?\n'
            '• что на обед?\n'
            '• что на ужин?'
        )
        return

    recipe = random.choice(RECIPES[meal])
    ingredients = '\n'.join(f'  • {i}' for i in recipe['ingredients'])
    steps = '\n'.join(f'  {n+1}. {s}' for n, s in enumerate(recipe['steps']))

    response = (
        f'🍴 *{recipe["name"]}*\n\n'
        f'⏱ Время: {recipe["time"]}\n\n'
        f'🛒 *Ингредиенты:*\n{ingredients}\n\n'
        f'👨‍🍳 *Приготовление:*\n{steps}'
    )
    await update.message.reply_text(response, parse_mode='Markdown')


def main():
    import os
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    if not token:
        raise ValueError('Не задана переменная окружения TELEGRAM_BOT_TOKEN')

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info('Бот запущен...')
    app.run_polling()


if __name__ == '__main__':
    main()
