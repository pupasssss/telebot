from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#кнопки
btn1 = KeyboardButton('як справи')
btn2 = KeyboardButton('може по пивку')
btn3 = KeyboardButton('купи мені машину')
btn4 = KeyboardButton('випадкове число')

marcup = ReplyKeyboardMarkup(resize_keyboard = True).add(btn1, btn2,  btn3, btn4)