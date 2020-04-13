import telepot
import time, sys
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from pprint import pprint


bot = telepot.Bot("1222241280:AAE9DEiQVzT8LReLjNXMUk3vs65kff2fx84")


def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	keyboard = InlineKeyboardMarkup(inline_keyboard =  [[InlineKeyboardButton(text = "Bene😄", callback_data = '1'),InlineKeyboardButton(text = "Male😱", callback_data = '2')],
														[InlineKeyboardButton(text = "Voglio ascoltare The Dance of Eternity", callback_data = '5')]])
	lista = ["Ciao", "Come stai?"]

	if msg['text'] == "Ciao":
		bot.sendMessage(chat_id,"Ciao amico, come stai?", reply_markup = keyboard)

	elif msg['text'] == "Come stai?":
		bot.sendMessage(chat_id, "Sto bene grazie😄")

	else:
		bot.sendMessage(chat_id, "Ah cavolo, mi dispiace😭")

	


def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')


	if query_data == '1':
		keyboard = InlineKeyboardMarkup(inline_keyboard =  [[InlineKeyboardButton(text = "Come stai tu?", callback_data = '3'),InlineKeyboardButton(text = "No", callback_data = '4')],])
		bot.sendMessage(from_id,"Fantastico, non mi chiedi come sto io?", reply_markup = keyboard)

		#bot.sendPhoto(from_id, photo=open('C:/Users/Tommaso/Desktop/BotTelegram/JohnPetrucci.jpg', 'rb'))
		#bot.sendAudio(from_id, audio=open('C:/Users/Tommaso/Desktop/BotTelegram/TheDanceofEternity.mp3', 'rb'))
	if query_data == "2":
		bot.sendMessage(from_id,"Accidenti, cosa succede?")

		#bot.sendPhoto(from_id, photo=open('C:/Users/Tommaso/Desktop/BotTelegram/hnou.png', 'rb'))
		#bot.sendAudio(from_id, audio=open('C:/Users/Tommaso/Desktop/BotTelegram/HNOU.mp3', 'rb'))
	if query_data == "3":
		bot.sendMessage(from_id,"Sto bene grazie")

	if query_data == "4":
		bot.sendMessage(from_id,"Vaffanculo stronzo")

	if query_data == "5":
		bot.sendAudio(from_id, audio=open('C:/Users/Tommaso/Desktop/BotTelegram/botdaprova/TheDanceofEternity.mp3', 'rb'))


bot.message_loop({'chat': on_chat_message,'callback_query':on_callback_query})







'''def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	keyboard = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "Lista dei servizi", callback_data = 'servizi')],])

	bot.sendMessage(chat_id, "Cliccando il bottone qua sotto potrai accedere alla lista dei servizi disponibili", reply_markup = keyboard)

def on_callback_query(msg):
	query_id, from_id, query_data = telepot.glance(msg, flavor = 'callback_query')

	if query_data == "servizi":
		keyboard = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "Gestione villaggio clash of clans", callback_data = 'clash')],
		[InlineKeyboardButton(text = "Allenatore Fortnite base", callback_data = '2')],
		[InlineKeyboardButton(text = "Allenatore osu!", callback_data = '3')],
		[InlineKeyboardButton(text = "Lezioni di HTML", callback_data = '4')],
		[InlineKeyboardButton(text = "Lezioni di Python", callback_data = '5')],
		[InlineKeyboardButton(text = "Lezioni di Java", callback_data = '6')]])

		bot.sendMessage(from_id,"Qua sotto è elencata la lista dei servizi disponibili.\nCliccare sul servizio desiderato per controllare i prezzi.", reply_markup = keyboard)
		print("2")
		if query_data == "clash":
			print("1")
			keyboard1 = InlineKeyboardMarkup(inline_keyboard = [[InlineKeyboardButton(text = "Acquistare servizio", callback_data = 'a1')],
			[InlineKeyboardButton(text = "Torna indietro", callback_data = 'indietro')]])

			bot.sendMessage(from_id, "Per la gestione del tuo villaggio clash of clans questi sono i prezzi:\n1 settimana: 5€\n2 settimane: 10€\n3 settimane: 15€\n1 mese: 20€",reply_markup = keyboard1)
			if query_data == "indietro":
				bot.sendMessage(from_id,"INDIETRO")

bot.message_loop({'chat': on_chat_message, 'callback_query': on_callback_query})'''

while 1:
	time.sleep(3)
