from aiogram import types
from loader import dp
from googlesearch import search
from utils.google_search import Google
# from utils.misc import rate_limit


# import telebot, wikipedia, re
# import wikipedia, re
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.linear_model import LogisticRegression

# wikipedia.set_lang("ru")

# def clean_str(r):
# 	r = r.lower()
# 	r = [c for c in r if c in ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;']
# 	return ''.join(r)

# def get_dialogues(s):
# 	with open('dialogues.txt', encoding='utf-8') as f:
# 		content = f.read()

# 	blocks = content.split('\n')
# 	dataset = []

# 	for block in blocks:
# 		replicas = block.split('\\')[:2]
# 		if len(replicas) == 2:
# 			pair = [clean_str(replicas[0]), clean_str(replicas[1])]
# 			if pair[0] and pair[1]:
# 				dataset.append(pair)

# 	X_text = []
# 	y = []

# 	for question, answer in dataset[:10000]:
# 		X_text.append(question)
# 		y += [answer]

#     return "".join(y)

# 	# global vectorizer
# 	# vectorizer = CountVectorizer()
# 	# X = vectorizer.fit_transform(X_text)

# 	# global clf
# 	# clf = LogisticRegression()
# 	# clf.fit(X, y)

# def get_wiki(s):
#     try:
#         ny = wikipedia.page(s)
#         wikitext=ny.content[:1000]
#         wikimas=wikitext.split('.')
#         wikimas = wikimas[:-1]
#         wikitext2 = ''
#         for x in wikimas:
#             if not('==' in x):
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         return wikitext2
#     except Exception as e:
#         # return 'В Википедии нет информации об этом'
#         return ''

# def get_answer(s):
#     # s = clean_str(s)
#     # dialogues = get_dialogues(s)
#     # if not len(dialogues) > 0:
#         return get_wiki(s)
#     # else:
#     #     return dialogues


# def clean_str(r):
# 	r = r.lower()
# 	r = [c for c in r if c in alphabet]
# 	return ''.join(r)

# alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;'

# def update():
# 	with open('dialogues.txt', encoding='utf-8') as f:
# 		content = f.read()
	
# 	blocks = content.split('\n')
# 	dataset = []
	
# 	for block in blocks:
# 		replicas = block.split('\\')[:2]
# 		if len(replicas) == 2:
# 			pair = [clean_str(replicas[0]), clean_str(replicas[1])]
# 			if pair[0] and pair[1]:
# 				dataset.append(pair)
	
# 	X_text = []
# 	y = []
	
# 	for question, answer in dataset[:10000]:
# 		X_text.append(question)
# 		y += [answer]
	
# 	global vectorizer
# 	vectorizer = CountVectorizer()
# 	X = vectorizer.fit_transform(X_text)
	
# 	global clf
# 	clf = LogisticRegression()
# 	clf.fit(X, y)

# update()

# def get_generative_replica(text):
# 	text_vector = vectorizer.transform([text]).toarray()[0]
# 	question = clf.predict([text_vector])[0]
# 	return question

# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         wikitext=ny.content[:1000]
#         wikimas=wikitext.split('.')
#         wikimas = wikimas[:-1]
#         wikitext2 = ''
#         for x in wikimas:
#             if not('==' in x):
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         return wikitext2
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'

# @bot.message_handler(commands=['start'])
# def start_message(message):
# 	bot.send_message(message.chat.id,"Здравствуйте, Сэр.")

# question = ""

# def wrong(message):
# 	a = f"{question}\{message.text.lower()} \n"
# 	with open('dialogues.txt', "a", encoding='utf-8') as f:
# 		f.write(a)
# 	bot.send_message(message.from_user.id, "Готово")
# 	update()

# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     # command = message.text.lower()
#     if message == "не так":
#         wrong(message)
#         return 'а как?'
#     # bot.send_message(message.from_user.id, "а как?")
#     # bot.register_next_step_handler(message, wrong)
#     else:
#         global question
#         question = message
#         reply = get_generative_replica(message)
#         if reply=="вики ":
#             return getwiki(message)
#         else:
#             return reply

@dp.message_handler()
async def bot_echo(message: types.Message):
    # answer = get_answer(message.text)
    # if not len(answer) > 0:
    #     await message.answer(get_text_messages(message.text))
    # else:
        # await message.answer_sticker('CAACAgIAAxkBAAIkX1-IhRHPL_m63dRhOutqKUDTiKoGAAJgAQACEBptIsq5BfpP9_oHGwQ')
    
    try:
        for url in search(message.text, stop=20):
            await message.answer(url)
    except Exception as e:
        print('search faild', e)
        search_results = Google.search(message.text)
        if len(search_results) > 0:
            await message.answer(search_results)
        else:
            print('google faild', search_results)
            await message.answer_sticker('CAACAgIAAxkBAAIkX1-IhRHPL_m63dRhOutqKUDTiKoGAAJgAQACEBptIsq5BfpP9_oHGwQ')
            await message.answer('Пиздец я сдох')
            await message.answer('Слишком много смотрел в гугл')

    # global question

    # command = message.text.lower()
    # if command =="не так":
    #     await message.answer("а как?")
    #     a = f"{question}\{message.text.lower()} \n"
    #     with open('dialogues.txt', "a", encoding='utf-8') as f:
    #         f.write(a)
    #     await message.answer("Готово")
    #     update()
    # else:
        
    #     question = command
    #     reply = get_generative_replica(command)
    #     if reply=="вики ":
    #         await message.answer(getwiki(command))
    #     else:
    #         await message.answer(reply)
