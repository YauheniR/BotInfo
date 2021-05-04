import os
import Parser
import telebot

bot = telebot.TeleBot("1723167933:AAHwue5q2bjdtyqSzvCFu4XBfUAx7lYd_qM", parse_mode=None)
files = os.listdir(path='C:\\orders\\')
for file in files:
    print('Файл ' + file + ' загружен')
clients = Parser.parsingFilesToClients(files)
sortedClients = Parser.initDistance(clients)
print('Бот ожидает запрос')


@bot.message_handler(content_types='text')
def send_info(message):
    for client in sortedClients:
        print(client.time)
        print(client)
        bot.send_message(message.chat.id, client)
    print("Запрос выполнен!")
    print('Бот ожидает следующий запрос')


bot.polling(none_stop=True)
