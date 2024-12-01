import telebot

TOKEN = 'YOUR_BOT_TOKEN'

bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: len(query.query) == 0)
def empty_query(inline_query):
    try:
        r = types.InlineQueryResultArticle(
            id='1',
            title='Play 2D Runner',
            input_message_content=types.InputTextMessageContent(message_text='Click to play the game'),
            url='http://yourserver.com/yourgame.html',
            thumb_url='http://yourserver.com/thumbnails/game_thumbnail.jpg',
            description='A fun 2D runner game built with HTML5.'
        )
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    bot.polling(none_stop=True)