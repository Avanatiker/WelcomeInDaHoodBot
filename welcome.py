import requests
import telegram
import urllib
import json
import time
import logging
from time import sleep
from ConfigParser import SafeConfigParser

bot = telegram.Bot('xxx')
chat_id = 0
lang = 'en'

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.info("WelcomeInDaHoodBot launched.")

try:
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
except IndexError:
    LAST_UPDATE_ID = None

def msg(msg):
    bot.sendMessage(chat_id=chat_id, text=msg)
    logging.info("Send message: " + msg)
    pass

def keyboard(status):
    if status == 1: #Questions 1
        custom_keyboard  = [
        [ 'How do I send photos with my bot?' ],
        [ 'How can I check if the message comes from a chat or a group?' ],
        [ 'Question 3' ],
        [ 'Exit', 'Next' ],
        ]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(chat_id=chat_id, text="Choose.", reply_markup=reply_markup)
        logging.info('Toggeled keyboard status for ' + str(chat_id) + ' to ' + str(status))
        pass
    if status == 2: #Questions 2
        custom_keyboard  = [
        [ 'Question 4' ],
        [ 'Question 5' ],
        [ 'Question 6' ],
        [ 'Exit', 'Settings' ],
        ]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(chat_id=chat_id, text="Choose.", reply_markup=reply_markup)
        logging.info('Toggeled keyboard status for ' + str(chat_id) + ' to ' + str(status))
        pass
    if status > 2: #Close
        reply_markup = telegram.ReplyKeyboardHide()
        bot.sendMessage(chat_id=chat_id, text="Keyboard deactivated", reply_markup=reply_markup)
        logging.info('Toggeled keyboard status for ' + str(chat_id) + ' to ' + str(status))
        pass
    pass

def echo():
    global LAST_UPDATE_ID
    global chat_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID):
        if LAST_UPDATE_ID < update.update_id:
            chat_id = update.message.chat_id
            is_group = update.message.chat_id != update.message.from_user.id
            usernamefrom = update.message.from_user.username
            try:
                if (is_group == False):
                    message = update.message.text.encode('utf-8')
                    logging.info('Got message from @' + update.message.from_user.username + ': ' + update.message.text)
                    if message == '/faq':
                        if lang == 'en':
                            keyboard(1)
                            pass
                        else:
                            msg('Not a valid language!')
                        pass
                    elif message == 'Next':
                        keyboard(2)
                        pass
                    elif message == 'Exit':
                        keyboard(3)
                        pass
                    elif message == 'How do I send photos with my bot?':
                        msg("bot.sendPhoto(chat_id=chat_id, photo=open('path/image.jpg', 'rb').read())")
                        pass
                    elif message == 'How can I check if the message comes from a chat or a group?':
                        msg('is_group = update.message.chat_id != update.message.from_user.id\nTrue = it is, False = it a personal chat.')
                        pass
                    elif message == 'Question 3':
                        msg('Answer 3')
                        pass
                    elif message == 'Question 4':
                        msg('Answer 4')
                        pass
                    elif message == 'Question 5':
                        msg('Answer 5')
                        pass
                    elif message == 'Question 6':
                        msg('Answer 6')
                        pass
                    pass
                pass
            except:
                pass

            user = update.message.new_chat_participant
            if (user):
                if lang == 'en':
                    try:
                        username = update.message.new_chat_participant.username
                        first_name = update.message.new_chat_participant.first_name
                        last_name = update.message.new_chat_participant.last_name
                        group = update.message.chat.title
                        msg('Welcome in the group ' + group + ', ' + first_name + ' ' + last_name + '! - @' + username + '\nJust ask a question.\nBut first check me out! @WelcomeInDaHoodBot for the FAQ')
                        pass
                    except:
                        try:
                            username = update.message.new_chat_participant.username
                            first_name = update.message.new_chat_participant.first_name
                            group = update.message.chat.title
                            msg('Welcome in the group ' + group + ', ' + first_name + '! - @' + username + '\nJust ask a question.\nBut first check me out! @WelcomeInDaHoodBot for the FAQ')
                            pass
                        except:
                            try:
                                username = update.message.new_chat_participant.username
                                last_name = update.message.new_chat_participant.first_name
                                group = update.message.chat.title
                                msg('Welcome in the group ' + group + ', ' + last_name + '! - @' + username + '\nJust ask a question.\nBut first check me out! @WelcomeInDaHoodBot for the FAQ')
                                pass
                            except:
                                try:
                                    first_name = update.message.new_chat_participant.first_name
                                    last_name = update.message.new_chat_participant.last_name
                                    group = update.message.chat.title
                                    msg('Welcome in the group ' + group + ', ' + first_name + ' ' + last_name + '!\nJust ask a question.\nBbut first check me out! @WelcomeInDaHoodBot for the FAQ')
                                    pass
                                except:
                                    try:
                                        first_name = update.message.new_chat_participant.first_name
                                        group = update.message.chat.title
                                        msg('Welcome in the group ' + group + ', ' + first_name + '!\nJust ask a question.\nBut first check me out! @WelcomeInDaHoodBot for the FAQ')
                                        pass
                                    except:
                                        username = update.message.new_chat_participant.username
                                        group = update.message.chat.title
                                        msg('Welcome in the group ' + group + ', ' + ' @' + username + '!\nJust ask a question.\nBut first check me out! @WelcomeInDaHoodBot for the FAQ')
                                        pass
                                    pass
                                pass
                            pass
                        pass
                else:
                    msg('Not a valid language!')
                pass
            else:
                pass

            LAST_UPDATE_ID = update.update_id

if __name__ == '__main__':
    while True:
        echo()
        time.sleep(0.5)
