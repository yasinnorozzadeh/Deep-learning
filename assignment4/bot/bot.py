import telebot
from animal_detector import Detector

detector = Detector
mybot = telebot.TeleBot("5569565731:AAFXKqQM-EowGXyvIEOCG4RgMzrCgUO2ZiI")

def img_detect(img):
    try:
        fileid = img.photo[-1].file_id
        fileinfo = mybot.get_file(fileid)
        downloaded_file = mybot.download_file(fileinfo.file_path)

        image_path = fileid + '.jpg'
        with open(f"botimage/{image_path}", 'wb') as new_file:
            new_file.write(downloaded_file)

        pred = detector(f"botimage/{image_path}")
        print(pred.pred_animal)
        mybot.reply_to(img, pred.pred_animal)
    except:
        mybot.send_message(img.chat.id, "There is a problem, try again")
@mybot.message_handler(commands=["start"])
def Welcom(message):
    mybot.reply_to(message, "hi " + str(message.from_user.first_name))
    mybot.send_message(message.chat.id, "click /help for commands bot")

@mybot.message_handler(commands=["help"])
def Help(message):
    mybot.reply_to(message, "/detect for detect animals")

@mybot.message_handler(commands=["detect"])
def Detect(message):
    ms = mybot.send_message(message.chat.id, "animals category : 1.🦜 2.🦏 3.🐍 4.🐢\nsend photo jpg fomat:")
    mybot.register_next_step_handler(ms, img_detect)

mybot.polling()
