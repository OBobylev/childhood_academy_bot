import telebot as tl
import os
from telebot import types
import gspread

bot_token = os.getenv('TELEGRAM_BOT_TOKEN', '')
googlesheet_id = os.getenv('GOOGLE_SHEET_ID', '')
bot = tl.TeleBot(bot_token)
gc = gspread.service_account(filename='main_page/botnumbersca-64b03e03eedd.json')
sh = gc.open('CA_numbers_bot')
wks = sh.sheet1

bot = tl.TeleBot(bot_token)
f = types.ReplyKeyboardMarkup





@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, f"Здравcтвуйте, {message.from_user.first_name} {message.from_user.last_name}!")
    main(message)
def main(message):
    mrk = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('•	Малышам 1-3 года', callback_data='kids1-3')
    btn4 = types.InlineKeyboardButton('•	Детский сад и начальная школа', callback_data='kindergarden')
    btn2 = types.InlineKeyboardButton('•	Дошкольникам', callback_data='before_school')
    btn3 = types.InlineKeyboardButton('•	Школьникам', callback_data='school')
    btn5 = types.InlineKeyboardButton('•	Английский язык', callback_data='eng_studio')
    btn9 = types.InlineKeyboardButton('•	Репетиторство', callback_data='rep')
    btn6 = types.InlineKeyboardButton('•	Логопед', callback_data='tongue_fixer')
    btn7 = types.InlineKeyboardButton('•	Творчество', callback_data='creativity')
    btn8 = types.InlineKeyboardButton('•	Каникулы', callback_data='holidays')
    btn10 = types.InlineKeyboardButton('•	Записаться на занятия', callback_data='zap')


    mrk.add(btn1, btn2, btn3, btn5, btn9, btn6, btn7, btn8)
    mrk.add(btn4)
    mrk.add(btn10)

    bot.send_photo(message.chat.id,
                   photo=open("main_page/main_page_logo.jpg", 'rb'),
                   caption=open("main_page/main_page_text",
                                mode='r',
                                encoding='utf-8').read(),
                   reply_markup=mrk)




@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "saveNumber":
        bot.send_message(call.message.chat.id, "Введите свое имя, возраст ребенка и номер телефона в сообщении в чат")
        bot.send_message(call.message.chat.id, "Формат:\nИван\n12\n89034521234")

    resp_mrk = types.InlineKeyboardMarkup(row_width=1)
    resp_mrk.add(types.InlineKeyboardButton('•	Записаться на занятия', callback_data='zap'),
                 types.InlineKeyboardButton('Вернуться на главный экран', callback_data='main_screen'),
                 types.InlineKeyboardButton('Заказать звонок', callback_data='saveNumber'))

    if call.data == 'kids1-3':
        kid_mrk = types.InlineKeyboardMarkup(row_width=2)
        kbtn1 = types.InlineKeyboardButton('•	Мой кроха и я 1+', callback_data='kid1')
        kbtn2 = types.InlineKeyboardButton('•	Умняшка 2+', callback_data='kid2')
        kbtn3 = types.InlineKeyboardButton('•	Малыши-гении', callback_data='kid3')
        kbtn4 = types.InlineKeyboardButton('•	Малыши-карандаши', callback_data='kid4')
        kbtn5 = types.InlineKeyboardButton('•	Запуск речи', callback_data='kid5')
        kid_mrk.add(kbtn1, kbtn2, kbtn3, kbtn4, kbtn5)
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/kids1-3/kids.jpg", 'rb'),
                       caption="\nЗдесь представлены все образовательные направления для малышей\n",
                       reply_markup=kid_mrk)

    if call.data == 'kid1':
        bot.send_photo(call.message.chat.id,
                        photo=open("main_page/kids1-3/kid1_photo.jpg", 'rb'),
                        caption=open("main_page/kids1-3/croha_i_ya.txt",
                                     mode='r',
                                     encoding='utf-8').read(),
                        reply_markup=resp_mrk)
    if call.data == 'kid2':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/kids1-3/kid2_photo.jpg", 'rb'),
                       caption=open("main_page/kids1-3/umnyshka.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'kid3':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/kids1-3/kid3_photo.jpg", 'rb'),
                       caption=open("main_page/kids1-3/genii.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'kid4':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/kids1-3/kid4_photo.JPG", 'rb'),
                       caption=open("main_page/kids1-3/karandashi_2.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'kid5':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/kids1-3/kid5_photo.jpg", 'rb'),
                       caption=open("main_page/kids1-3/zapusk_rechi.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)



    if call.data == 'before_school':
        mrk = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('•	Мини-сад', callback_data='bs1')
        btn2 = types.InlineKeyboardButton('•	«Азбука развития» с 3-х лет', callback_data='bs2')
        btn3 = types.InlineKeyboardButton('•	«Читайка» с 4-хлет', callback_data='bs3')
        btn4 = types.InlineKeyboardButton('•	«Открытие мира знаний» с 4-х лет', callback_data='bs4')
        btn5 = types.InlineKeyboardButton('•	«Будущий первоклассник» с 5 лет', callback_data='bs5')
        btn6 = types.InlineKeyboardButton('•	Английский язык с 4-х лет', callback_data='bs6')
        btn7 = types.InlineKeyboardButton('•	Интенсив «Завтра в школу!»', callback_data='bs7')
        btn8 = types.InlineKeyboardButton('•	«Креативная математика» и «Лаборатория мышления»', callback_data='bs8')
        btn10 = types.InlineKeyboardButton('•	Экспресс подготовка к школе', callback_data='bs10')
        mrk.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn10)
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/Before_school.jpg", 'rb'),
                       caption="\nЗдесь представлены все образовательные направления для дошкольников\n",
                       reply_markup=mrk)

    if call.data == 'bs1':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs1_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/mini_sad.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs2':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs2_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/azbuka_razv.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs3':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs3_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/chitayka.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs4':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs4_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/otkritie.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs5':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs5_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/future1st.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs6':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs6_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/eng4-7.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs7':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs7_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/school_tomorrow.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs8':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs8_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/creative_math.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'bs10':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/before_school/bs10_photo.jpg", 'rb'),
                       caption=open("main_page/before_school/exp_school.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'school':
        mrk = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('•	Начальная школа 1-4 класс (семейная форма обучения)', callback_data='sc1')
        btn2 = types.InlineKeyboardButton('•	Репетиторский центр', callback_data='rep')
        btn3 = types.InlineKeyboardButton('•	Скорочтение', callback_data='sc2')
        btn4 = types.InlineKeyboardButton('•	Грамотность 1-4 классы', callback_data='sc3')
        btn5 = types.InlineKeyboardButton('•	«Красивый почерк» - каллиграфия', callback_data='sc4')
        btn6 = types.InlineKeyboardButton('•	Таблица умножения', callback_data='sc5')
        btn7 = types.InlineKeyboardButton('•	Креативная Математика ', callback_data='sc6')
        btn8 = types.InlineKeyboardButton('•	Интенсив «Вспомнить все!»', callback_data='sc7')
        btn9 = types.InlineKeyboardButton('•	Академия наук', callback_data='sc8')
        btn10 = types.InlineKeyboardButton('•	Английский для школьников', callback_data='sc9')

        mrk.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/School_pic.jpg", 'rb'),
                       caption="\nЗдесь представлены все образовательные направления для школьников\n",
                       reply_markup=mrk)
    if call.data == 'sc1':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc1_photo.jpg", 'rb'),
                       caption=open("main_page/school/school1-4.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc2':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc2_photo.jpg", 'rb'),
                       caption=open("main_page/school/scorochtenie.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc3':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc3_photo.jpg", 'rb'),
                       caption=open("main_page/school/gramotnost.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc4':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc4_photo.jpg", 'rb'),
                       caption=open("main_page/school/kaligraphiya.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc5':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc5_photo.jpg", 'rb'),
                       caption=open("main_page/school/tablica_umnog.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc6':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc6_photo.jpg", 'rb'),
                       caption=open("main_page/school/creative_math.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc7':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc7_photo.jpg", 'rb'),
                       caption=open("main_page/school/vsponit_vse.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc8':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc8_photo.jpg", 'rb'),
                       caption=open("main_page/school/academia_nauk.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == 'sc9':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/school/sc9_photo.jpg", 'rb'),
                       caption=open("main_page/school/eng_for_school.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'kindergarden':
        mrk = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('•	Мини-сад ',callback_data='k1')
        btn2 = types.InlineKeyboardButton('•	0 класс', callback_data='k2')
        btn3 = types.InlineKeyboardButton('•	Частная школа 1-4 класс (семейная форма обучения)', callback_data='k3')
        mrk.add(btn1, btn2, btn3)
        bot.send_photo(call.message.chat.id,
                        photo=open("main_page/Kindergarden/kindergarden_photo.jpg", 'rb'),
                        caption="\nЗдесь вы узнаете все информацию о детском садике и начальной школе\n",
                        reply_markup=mrk)
    if call.data == "k1":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Kindergarden/k1_photo.jpg", 'rb'),
                       caption=open("main_page/Kindergarden/mini_sad.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "k2":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Kindergarden/k2_photo.jpg", 'rb'),
                       caption=open("main_page/Kindergarden/0_kurs.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "k3":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Kindergarden/k3_photo.jpg", 'rb'),
                       caption=open("main_page/Kindergarden/nach_school.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)


    if call.data == 'eng_studio':
        mrk = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('•	Дошкольникам',callback_data='bs6')
        btn2 = types.InlineKeyboardButton('•	Школьникам', callback_data='sc9')
        btn3 = types.InlineKeyboardButton('•	Английский для будущих второклассников', callback_data='en1')
        mrk.add(btn1, btn2, btn3)
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Eng_studio/eng_photo.jpg", 'rb'),
                       caption="\nЗдесь вы узнаете  информацию о студии английского языка\n",
                       reply_markup=mrk)
    if call.data == "en1":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Eng_studio/en1_photo.jpg", 'rb'),
                       caption=open("main_page/Eng_studio/en1.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'tongue_fixer':
        mrk = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('•	Логопед',callback_data='tf1')
        btn2 = types.InlineKeyboardButton('•	Дефектолог', callback_data='tf2')
        btn3 = types.InlineKeyboardButton('•	Психолог', callback_data='tf3')
        btn4 = types.InlineKeyboardButton('•	Запуск речи', callback_data='kid5')
        btn5 = types.InlineKeyboardButton('•	Логокомплекс', callback_data='tf5')
        mrk.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(call.message.chat.id,
                        photo=open("main_page/Logoped/Logoped_photo.jpg", 'rb'),
                        caption="\nЗдесь представлены все дополнительные услуги нашей Академии\n",
                        reply_markup=mrk)
    if call.data == "tf1":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Logoped/tf1_photo.jpg", 'rb'),
                       caption=open("main_page/Logoped/logoped.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "tf2":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Logoped/tf2_photo.jpg", 'rb'),
                       caption=open("main_page/Logoped/defectolog.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "tf3":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Logoped/tf3_photo.jpg", 'rb'),
                       caption=open("main_page/Logoped/psiholog.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "tf5":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Logoped/tf5_photo.jpg", 'rb'),
                       caption=open("main_page/Logoped/logocomplecs.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'creativity':
        mrk = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('•	Малыши-карандаши с 3-х лет',callback_data='cr1')
        btn2 = types.InlineKeyboardButton('•	ИЗО, живопись, рисунок', callback_data='cr2')
        btn3 = types.InlineKeyboardButton('•	Правополушарное рисование', callback_data='cr3')
        btn4 = types.InlineKeyboardButton('•	Лепка', callback_data='cr4')
        btn5 = types.InlineKeyboardButton('•	Фабрика волшебства', callback_data='cr5')
        mrk.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Creativity/cr4_photo.jpg", 'rb'),
                       caption="\nЗдесь представлены все творческие направления\n",
                       reply_markup=mrk)
    if call.data == "cr1":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Creativity/cr1_photo.jpg", 'rb'),
                       caption=open("main_page/Creativity/karandashi.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "cr2":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Creativity/cr2_photo.jpg", 'rb'),
                       caption=open("main_page/Creativity/izo_studio.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "cr3":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Creativity/cr3_photo.jpeg", 'rb'),
                       caption=open("main_page/Creativity/p_risovanie.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "cr4":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Creativity/cr4_photo.jpg", 'rb'),
                       caption=open("main_page/Creativity/lepka.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "cr5":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Creativity/cr5_photo.jpeg", 'rb'),
                       caption=open("main_page/Creativity/tv_masterskaya.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'holidays':
        mrk = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton('•	Интенсив «Завтра в школу!»', callback_data='bs7')
        btn3 = types.InlineKeyboardButton('•	Каллиграфия, Таблица умножения, Грамотность', callback_data='h3')
        btn4 = types.InlineKeyboardButton('•	Интенсив «Вспомнить все!»', callback_data='sc7'  )
        mrk.add(btn2, btn3, btn4)
        bot.send_photo(call.message.chat.id,
                        photo=open("main_page/Holidays/good_holidays_photo.jpeg", 'rb'),
                        caption="\nЗдесь представлены все летние программы и интенсивы нашей Академии\n",
                        reply_markup=mrk)
    if call.data == 'h3':
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Holidays/comb_photo.jpg",'rb'),
                       caption=open("main_page/Holidays/comb.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'rep':
        mrk = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('•	Репетитор по русскому языку 1-11 классы',callback_data='rep1')
        btn2 = types.InlineKeyboardButton('•	Репетитор по математике 1- 4 классы', callback_data='rep2')
        btn3 = types.InlineKeyboardButton('•	Репетитор по английскому языку 5-11 классы', callback_data='rep3')
        btn4 = types.InlineKeyboardButton('•	Каллиграфия, Таблица умножения, Грамотность', callback_data='rep4')
        mrk.add(btn1, btn2, btn3, btn4)
        bot.send_photo(call.message.chat.id,
                        photo=open("main_page/Repetitor/rep_photo.jpg", 'rb'),
                        caption=open("main_page/Repetitor/rep_text.txt",
                                mode='r',
                                encoding='utf-8').read(),
                        reply_markup=mrk)
    if call.data == "rep1":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Repetitor/rep1_photo.jpg", 'rb'),
                       caption=open("main_page/Repetitor/rep_rus.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "rep2":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Repetitor/rep2_photo.jpg", 'rb'),
                       caption=open("main_page/Repetitor/rep_math.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "rep3":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Repetitor/rep3_photo.jpg", 'rb'),
                       caption=open("main_page/Repetitor/rep_eng.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)
    if call.data == "rep4":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Repetitor/rep4_photo.jpg", 'rb'),
                       caption=open("main_page/Repetitor/comb_kurs.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)


    if call.data == "h1":
        bot.send_photo(call.message.chat.id,
                       photo=open("main_page/Holidays/h1_photo.jpg", 'rb'),
                       caption=open("main_page/Creativity/tv_masterskaya.txt",
                                    mode='r',
                                    encoding='utf-8').read(),
                       reply_markup=resp_mrk)

    if call.data == 'zap':
        bot.send_photo(call.message.chat.id,
                        photo=open("main_page/admin_photo.jpg", 'rb'),
                        caption="Связаться с администрацией академии и записаться на выбранный курс можно номеру телефона: \n\n[+7-920-769-48-82]\n(нажмите на номер с мобильнного телефона чтобы позвонить)",
                        parse_mode='Markdown',
                       reply_markup=resp_mrk)
    if call.data == 'main_screen':
        main(call.message)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        name, age, number = message.text.split("\n")
        text_message = f'Номер записан!'
        bot.send_message(message.chat.id, text_message)
        sh = gc.open('CA_numbers_bot')
        wks.append_row([name, age, number])
    except:
        bot.send_message(message.chat.id, 'ОШИБКА! Неправильный формат данных!')




if __name__ == '__main__':
    bot.polling(none_stop=True)
