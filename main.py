#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import telebot

"""
Простой бот обратной связи на telebot.
Бот принимает отзыв от пользователя и пересылает его администратору.
"""

# Замените на ваш токен бота, полученный через BotFather
TOKEN = "7615801045:AAGaZdBZydReaP9ts73YxZYtlTt9dioLdGc"
# Замените на ID администратора, которому будут пересылаться отзывы
ADMIN_ID = 1620595306

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Привет!\nЭто бот обратной связи.\nДля отправки отзыва воспользуйтесь командой /feedback или просто напишите сообщение."
    )

@bot.message_handler(commands=["feedback"])
def handle_feedback_command(message):
    bot.send_message(
        message.chat.id,
        "Пожалуйста, напишите ваш отзыв текстом:"
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Если сообщение содержит текст, считаем его отзывом
    if message.text:
        sender = message.from_user.username if message.from_user.username else f"ID {message.from_user.id}"
        feedback_text = message.text
        # Формируем сообщение для администратора
        admin_msg = f"Новый отзыв от {sender}:\n{feedback_text}"
        bot.send_message(ADMIN_ID, admin_msg)
        # Отправляем подтверждение пользователю
        bot.send_message(message.chat.id, "Спасибо за ваш отзыв!")
    else:
        # Если формат сообщения не текстовый
        bot.send_message(message.chat.id, "Пожалуйста, отправьте отзыв в виде текстового сообщения.")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
