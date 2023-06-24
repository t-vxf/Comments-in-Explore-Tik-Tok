import requests,os,json
hit=0
bad=0
from time import sleep
from colorama import Fore
os.system("cls")
os.system("clear")
import random

words = ['سبحان الله', 'استغفرالله', 'صلو على النبي يخوان', 'صليت على النبي اليوم؟', 'كَلِمَتانِ خَفِيفَتانِ علَى اللِّسانِ، ثَقِيلَتانِ في المِيزانِ، حَبِيبَتانِ إلى الرَّحْمَنِ، سُبْحانَ اللَّهِ وبِحَمْدِهِ، سُبْحانَ اللَّهِ العَظِيمِ', 'إنَّ أَحَبَّ الكَلَامِ إلى اللهِ: سُبْحَانَ اللهِ وَبِحَمْدِهِ']


banner="""by: @bbzzs on telegram
    ███        ▄█    █▄       ▄████████         ▄██████▄   ▄██████▄     ▄████████     ███     
▀█████████▄   ███    ███     ███    ███        ███    ███ ███    ███   ███    ███ ▀█████████▄ 
   ▀███▀▀██   ███    ███     ███    █▀         ███    █▀  ███    ███   ███    ███    ▀███▀▀██ 
    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄           ▄███        ███    ███   ███    ███     ███   ▀ 
    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ▀▀███ ████▄  ███    ███ ▀███████████     ███     
    ███       ███    ███     ███    █▄         ███    ███ ███    ███   ███    ███     ███     
    ███       ███    ███     ███    ███        ███    ███ ███    ███   ███    ███     ███     
   ▄████▀     ███    █▀      ██████████        ████████▀   ▀██████▀    ███    █▀     ▄████▀   by: @bbzzs on telegram
                                                                                              
⣟⣿⣿⣿⢠⣇⢾⣿⣿⣿⣿⡟⣹⣮⠻⢿⣿⣿⣿⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡻⠿⠿⣋⣭⠮⠁⣴⠟⣅⣷⣿⣶⣶⣤⡈⢻⣿⣿⣿⣷⡌⠸⣿⠏⡠⢤⣦⢶⣻⣹
⠺⣽⣿⣿⣐⡪⢮⣝⣛⣭⣭⣾⣿⣿⡧⣕⡩⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏⣻⡿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣵⣾⣿⣿⣿⠟⣨⠲⣋⠜⣻⣾⣿⣿⣿⣿⣿⣶⣾⣿⡟⠉⠁⣒⣉⡐⠷⣬⣴⣾⣯⡉
⣆⢩⡿⢿⣦⣽⣳⢮⣞⡿⣿⣿⣿⣿⢇⣿⣿⣾⣟⡿⣿⣿⣿⡸⣿⣿⣿⣿⣿⣿⣿⠟⣥⣸⣇⣿⣿⣿⣿⣿⣿⣟⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣋⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡹⠿⠿⣛⣥⣾⡋⣴⣯⣷⣹⣿⣿⣿⣿⣿⣭⣛⡿⠯⠤⣶⣿⣿⡑⠦⠶⣒⣿⣿⣿⣷
⣌⢀⠐⢪⡛⣿⣷⡏⢰⣶⣌⣍⢛⡫⡺⢿⣿⣿⣿⣿⣾⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⢸⣿⣇⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⢋⣵⣶⣦⡝⢻⣿⣿⣿⣿⣿⣿⣿⡿⠋⣰⣿⣿⣿⣟⡿⢭⣋⠖⡰⠂⡁⠉⡑⠊⠷⣶⣾⣭⣝⡲⢶⣶⣦⣭⡛
⣿⣿⣇⠀⠙⢳⣟⣿⢸⣿⣿⡎⣳⣩⠖⡧⣏⠿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⡟⣸⣿⣿⣿⣿⣿⣿⡏⢴⣟⢦⠹⣿⣿⡿⣭⠳⡌⠚⠀⠁⠤⠑⢀⠐⠠⠀⠩⠍⢴⣾⣟⣯⣿⢿⣿
⣿⣿⣿⡆⢐⣂⣤⣴⣾⣿⣿⡇⡵⡹⣿⣶⣥⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣽⣛⡿⠿⢟⣛⣡⣾⣿⣿⣿⣿⣿⣿⣛⣙⣒⣠⣼⢠⣿⣿⣟⠧⠁⠀⠀⠀⠀⠀⠈⠀⠈⠀⠠⠐⡈⠆⠒⣈⣹⠾⣿⣿
⣿⣿⣿⡯⠠⣿⣿⣿⣿⣿⣿⡇⣽⢴⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⡿⢸⣿⣿⣿⣿⡞⣿⣿⣿⡇⣮⠻⣿⣿⣿⣿⣿⣿⣿⣦⠻⣿⣿⠟⣛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⣾⠿⠟⢁⠠⣐⠢⢍⡐⠀⠀⠀⣀⡀⠤⠤⠒⠒⠉⠙⡠⢠⠘⣯⢿
⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⣧⠙⣛⠷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣟⣵⣿⣿⣿⣿⣿⠇⠘⣿⣿⣷⢹⡇⢦⢭⣍⣙⣛⡛⠻⠿⣷⣬⣛⣇⣸⡗⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⢛⣛⣻⣭⣶⣶⣶⣶⡾⣭⢳⡌⠇⠂⠀⠀⡌⠁⠀⠀⠀⠀⠀⠀⡬⠀⠑⢂⣸⢧⡿
⣫⢿⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⢸⡷⣶⢯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣿⣯⣟⠿⠀⡀⠈⠛⠿⣧⠃⣾⡷⣹⣭⠖⢋⢽⣦⣊⠻⠿⢿⠿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣾⡿⡸⣿⡿⠿⢿⣿⣿⠿⠻⠑⠒⠈⢌⠡⠀⠀⠁⠀⠀⠀⠀⠐⠀⢐⡜⢫⣶⢰⣫⠾⣽
⠿⣿⢿⣷⣝⡻⣿⣿⣿⣿⣿⣿⡞⣽⣳⣟⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣝⣛⢿⣿⣿⣧⠀⡇⠈⢸⣄⠈⠰⠉⠛⢉⣤⣶⣷⣎⢻⣿⡶⢸⣶⣟⣯⠹⣿⣿⣷⣾⣷⣿⣿⣿⣿⡔⢶⢶⡗⢱⣾⣿⣦⣉⣉⠶⣂⠤⣐⠢⡌⠂⠁⠄⡠⠀⡀⠀⠀⠀⠀⡔⣲⣿⣿⣮⣱⣚⣙
⣛⣿⣜⣿⣿⣿⡊⢿⣿⣿⣿⣿⣷⢻⡶⣯⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⠎⣿⣿⡏⠀⠑⠀⠀⣿⣾⣧⠀⢠⣿⢡⠀⠌⣿⠈⢹⠁⣼⠹⣿⣿⣷⠎⣒⠂⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⣿⣿⣿⣿⣿⣡⠾⣜⢣⢇⢣⡔⠃⢈⠀⡐⣹⠄⠀⠤⠠⠤⢀⣿⣿⣿⣷⣶⣿⣟
⠻⢿⣿⣿⣻⣿⡇⣼⣿⣿⣿⣿⣿⡎⡿⣷⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡹⢿⡿⠧⠀⠡⢾⣿⣿⣿⣿⣷⡘⢿⣶⣶⡾⠃⡀⣄⠘⠃⠀⢩⠋⠁⠚⢿⡒⣿⣿⡿⠟⠿⠿⠿⢟⠡⣾⣅⢦⡙⣿⠿⣡⣟⣭⢋⣎⢧⡘⡀⠘⠂⠀⠁⠀⠀⢀⡱⢈⣾⣿⣿⠿⣿⣿⠿⠛
⣦⠁⣻⣿⣴⣶⣷⡙⢿⣿⣿⣿⣿⣷⡸⣯⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⡿⣋⣭⡙⢿⢟⡙⢋⣵⣶⣾⣤⠀⠀⡀⠨⣿⣿⣿⣿⣿⣶⣶⣶⣶⣯⡾⠎⢀⣤⢠⡟⠁⠈⣁⡾⣸⣿⣏⣶⣭⢋⣾⣿⣿⣷⣬⣯⣾⣿⣶⠟⠇⣻⢼⢫⠜⢆⠣⠑⠂⢀⠄⢒⣨⣭⣴⣾⣿⡿⠉⠀⠀⠉⢀⣤⣶
⣿⡀⣷⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⣿⣧⢻⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⠇⢿⣿⠿⠶⡋⣴⣿⣿⡿⣿⣟⣆⠀⢿⣴⡆⣭⣭⢩⣿⢻⣭⡍⣭⣶⠸⣱⣿⡟⠈⠴⠒⠛⠯⣾⢛⣉⣙⠯⠵⣛⠿⠿⣿⣿⣿⣿⡿⠏⣣⠀⠎⠓⣉⣤⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⠀⠀⣀⣴⣾⣿⣿⣿
⣿⣿⣭⣛⡻⠿⠿⣿⡧⢸⣿⣿⣿⣿⣿⣧⢻⣟⣿⣿⣿⣿⡿⢡⣬⠤⠖⣠⣿⡰⢮⠅⡜⠻⢿⣿⡸⢃⣸⣆⠀⢾⡇⣿⡗⣾⣿⢸⣿⡇⡿⣣⣾⡿⠋⢀⣴⣿⣝⢿⣷⡄⢞⣩⣶⣿⣿⣿⣿⣷⣦⣍⣉⣉⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢽⡤⠤⠄⠚⠻⠿⠿⣟⣻
⣿⣿⣿⣿⣿⣿⣷⣎⠫⠸⣿⣿⣿⣿⣿⣿⣧⡻⣾⣽⣟⣿⠁⣿⠁⠄⠨⣶⠊⠤⠃⡰⠁⢃⣨⠾⣿⣿⣟⣯⡷⡀⠁⠻⠇⠿⠟⣚⣫⣵⣾⠿⠋⠀⠀⣼⣿⢟⡻⢺⡟⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠍⠫⠽⣿⣖⣶⠂⠠⠴⠶⠶
⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⢻⣿⣿⣿⣿⣿⣿⣷⡙⣾⡽⣯⣀⣁⣀⣰⣦⠓⠀⡶⢋⣴⣾⣿⣿⣶⣯⢺⣟⡇⠐⠁⠀⠀⠐⠒⠛⠋⠉⠁⠀⠀⠀⢀⡜⣸⡏⢎⢁⣾⣇⣀⣿⣿⣿⣿⣽⣾⣽⣿⣿⣿⣿⣿⣯⠏⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⢄⠂⠡⢂⣿⣿⠏⠀⠙⢲⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣎⣌⣿⣿⣿⣿⣿⣿⣿⣿⣎⢿⡑⢻⢾⡽⣿⡽⣧⠀⣴⣿⣿⣿⡿⣻⠟⣵⡛⠉⠁⠀⠀⠀⠀⠀⢀⣤⠖⠋⠀⠀⡀⣤⢃⣾⢟⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠑⠛⠻⢿⣳⡹⣭⣶⣾⡽⣿⡟⠁⢀⣀⠄⠀⠀⡘⠘⣼⠟⠁⠀⠀⠀⠀⣸⡞
⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⣿⡛⣿⣿⣿⣿⣿⣿⣿⣿⣷⡁⠀⠙⢞⡳⠽⣳⠘⠿⢿⣿⣻⣷⢯⣾⠿⠁⠀⠀⠀⠀⢠⠆⠼⠛⠃⠀⠀⣄⠲⣉⡴⢟⣵⣭⣶⣿⡿⠿⠿⠿⠿⣿⣿⣿⡿⠟⠋⣘⠻⠟⢀⣤⣤⣀⠀⠈⢻⣇⢿⠿⣣⡆⡿⠀⢠⢚⠀⠙⠀⠀⠀⠀⣀⠀⠊⣝⡳⠂⠰⠶⢷
⣽⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⡆⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠰⣄⣲⣆⡁⣰⠃⠀⣿⡷⢣⠟⣊⠤⠊⠀⠀⣠⠐⢁⣴⢢⣓⢦⢃⣫⣴⢪⣷⣿⡿⠟⠋⠉⠀⠀⠀⠀⣀⣤⣔⡀⣴⣾⣷⣶⣄⡐⠾⣽⣾⣿⣳⠂⠀⣣⠛⠾⢛⠡⠒⠁⢠⢯⡷⣅⡢⡲⢜⡲⡓⢆⡞⣬⣐⠡⠄⠀⢘⢒
⠀⢟⣿⣿⡿⣻⣿⣿⣿⣿⣿⣿⣂⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡉⠀⣼⢃⣠⣴⣟⣽⡶⢋⡼⠋⠀⠀⠀⠄⠋⢠⣛⡎⠉⠺⣡⣾⢟⣱⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠁⣠⣽⣿⣿⣿⣿⣿⣶⣄⡙⠯⡟⠀⠨⢳⢏⠏⠁⠁⣀⢄⢿⡻⣜⠧⡝⢢⣑⢌⡹⡜⣢⠵⣘⠟⣶⡖⠀⠬
⣿⣿⠻⢫⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⣾⢁⡬⢻⣿⣾⡿⢃⠎⠀⠀⢀⠆⠀⠀⠀⠀⢻⡼⢡⡞⣵⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠈⠁⣈⣀⠔⢶⡿⣷⣄⠙⠮⡝⣜⠣⠪⡱⢨⠢⠕⠊⠙⠚⠃⠉⠙⠀
⡯⠝⠃⠉⠛⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠻⠿⣫⣏⢻⣽⠟⣡⠋⠀⠀⢠⡟⠀⠀⠀⠀⠀⣴⡃⣿⢧⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⢟⣿⣿⣿⣿⣿⣿⣿⣯⠻⣿⣿⣿⣦⣀⠈⠳⢿⣾⡣⡛⢿⣞⠷⣥⠘⠎⠈⠆⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⣴⡞⣡⣦⡀⢘⠻⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣶⣶⣿⣜⡊⢋⡼⠁⠀⠀⠠⠋⠀⠀⠀⣴⣻⢾⣣⢠⡶⢫⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠻⣿⣿⣿⣷⣤⡀⠀⠉⠈⠂⠈⣁⣀⣀⣠⣤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠏⣢⣿⣿⣿⣮⣷⣤⡙⠿⣫⣵⣿⣿⣿⠟⣋⣡⣤⣤⣬⣭⣍⣉⣙⣉⣭⡥⠖⠋⠀⠀⠀⠀⠀⢀⠀⠀⣎⡷⣻⣼⡗⣿⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠄⠉⠛⠿⣿⣿⣷⣴⣤⡛⠿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡙⠿⣏⡁⠚⠿⠿⠟⠋⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⢲⡏⡎⠀⠘⣼⢳⡇⢿⣷⡻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠠⠀⠀⠉⠙⠛⠿⠿⠖⠃⠉⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠠
⠀⠸⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣢⢈⠙⠿⣶⣤⡀⠀⠀⠐⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠛⢰⠀⠀⠈⠐⠯⠽⡎⡻⣿⡷⢹⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠂⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣆⢿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠁⠛⠿⣷⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠀⠀⠀⠀⡀⠈⠐⠀⡑⢹⡌⡟⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⢰⣿⣶⣅⣐⢄⠐⢭⡻⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⡀⠈⠀⠄⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⣿⡘⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣶⣤⣀⠉⠙⠳⢆⡄⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⣰⠁⢀⠀⠀⡝⡦⠆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠰⢸⣿⣿⣿⣿⣿⣿⣶⣿⡼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠈⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀by: @bbzzs on telegram"""
print(Fore.LIGHTMAGENTA_EX+banner)
session=input(Fore.LIGHTCYAN_EX+"sessionid?: ")
print("1;  auto comment\n2: ur comment\nby: @bbzzs on telegram")
mod=input("Choose mode:  ")
r = 'https://www.tiktok.com/@_sra'
hc =  {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

r = requests.get(url=r,headers=hc)
csrf=r.cookies['tt_csrf_token']
uid = 'https://www.tiktok.com/api/recommend/item_list/?aid=1988&app_language=ar&app_name=tiktok_web&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36&channel=tiktok_web&clientABVersions=70508271%2C71065281%2C71163923%2C71214365%2C71231942%2C71264214%2C71272203%2C71273551%2C71273554%2C71273556%2C71274427%2C71283664%2C71287275%2C71288368%2C71290655%2C71314410%2C71325543%2C70405643%2C71057832%2C71200802&cookie_enabled=true&count=30&device_id=7248221636050126342&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=3&is_fullscreen=false&is_page_visible=true&language=ar&os=windows&priority_region=&pullType=2&referer=&region=SA&screen_height=1080&screen_width=1920&tz_name=Asia%2FRiyadh&verifyFp=verify_lj9ybfnn_kTE2YoHr_iYoV_42rn_B7db_LAjmU3JLSezV&webcast_language=ar&msToken=hj5t0-YP5CgQMOarNcVVj2d8-cUWO6vxgzx_N4A7XKcXh5SkjQfZcO5dkGAU4w9uhyzq_7pXSwA5qMCrZtbuNDXElGJ2l1Y8jAw4cgyacQcDVj_bnZ9GYen44ICZmfizSLURmjW-Mhq-&X-Bogus=DFSzxwVuzYXANHqFtnKlMQYklT1Y&_signature=_02B4Z6wo00001jCKH8QAAIDD7vxHY4eugdYwihtAAOjC18'

headers = {
           'tt-csrf-token': csrf,
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'x-kl-kfa-ajax-request': 'Ajax_Request',
'x-secsdk-csrf-token': '000100000001abcd2b31ccc40b3ead61a23743ab9d722a45cf0c8221941d7cf7fa0d5cf5d3a7176b675996cd2780',
           'cookie': '_ttp=2LZ9p0uHcrBOIt07JdVrL4wBexm; ttwid=1%7C5MlWCBGC8JoKOa3YunjpyKMo9N5SZAiZizHRcFvwWKc%7C1681231591%7C1edfc4151e8abb3040e3d3ea6caa740b6a3bd8029351e64f3fe7765284890022; tiktok_webapp_theme=dark; tt_chain_token=d29dlYwwUDXg0msrYy35qw==; living_user_id=793228223583; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227220834648023729665%22%2C%22timestamp%22:1681231593848}; passport_csrf_token=f3395b16d7ddfe035c450bd236952577; passport_csrf_token_default=f3395b16d7ddfe035c450bd236952577; cmpl_token=AgQQAPO_F-RO0rIUVTOxMZ04_lQX6X7Wv4M0YM6KDA; sid_guard='+session+'%7C1687188001%7C15552000%7CSat%2C+16-Dec-2023+15%3A20%3A01+GMT; uid_tt=576098b1be7e1008ab312231f995a717d36ab5b03f38e8d064e153cc5f022a4e; uid_tt_ss=576098b1be7e1008ab312231f995a717d36ab5b03f38e8d064e153cc5f022a4e; sid_tt='+session+'; sessionid='+session+'; sessionid_ss='+session+'; sid_ucp_v1=1.0.0-KDkyYjM0MmNiMGViMGY3ODUwYjNhZDQ2OTM0YzI5MzI4ZGJlMjNhMTMKIAiBiI3Iw_KulWIQoeTBpAYYswsgDDC096qRBjgEQOoHEAMaBm1hbGl2YSIgOTc2ZDE0NjRmNjA2NGFlYzE0NTg5YTQwNTRiMjIwNDI; ssid_ucp_v1=1.0.0-KDkyYjM0MmNiMGViMGY3ODUwYjNhZDQ2OTM0YzI5MzI4ZGJlMjNhMTMKIAiBiI3Iw_KulWIQoeTBpAYYswsgDDC096qRBjgEQOoHEAMaBm1hbGl2YSIgOTc2ZDE0NjRmNjA2NGFlYzE0NTg5YTQwNTRiMjIwNDI; store-idc=alisg; store-country-code=sa; store-country-code-src=uid; tt-target-idc=alisg; tt-target-idc-sign=oVyXmWBuhThH5AanDr2s4ifPFLqVbXA__2Y-_noynXhnZcC2KUC2SvURG2IPVQjGsBdfp_l0cxCnjKPZiHgvAq_Q5rPi-HvgU3FnTJ8FxYdqoRtwCzFLUgh5zoXMA2Oa0DBkRCvSP3tnOV0mU8ssiOzhX_FicDeyH8b8wU6jaXnxrAGdyUwVdrd-etCah1w8NHEuK5cNHOpjCdjacvq7x2D-MwsjB2gb-xnwhWaFB6MVgBQD2nHkIty_ydjgHk5IjOrqmR8uSXYld9ru7w-FAypohnsJQstuezJpyD8PuXB41QguQTWXc_6zrXB_uS0sdPBPBaGHZNWOUM3ZT7LYFn9xRNkUM-vJmS0dN0ncjtBAfPKdy-WoIRd-8cdearyJ5HreE9KJDrrrryfNjmFOgTn8efuZklqqNJ-xCeCbDN02TZpXUtADQCuAGHC728ooFUtKT9MGxeYUGTtiaPh8tfnD82CnvHf3-lcOLwmOo3NNLCyzc9Q_2OIulvHKkiuL; tt_csrf_token='+csrf+'; passport_fe_beating_status=true; csrf_session_id=9811f85acfe738d341b65ba95478a236; odin_tt=b6c00912e1a4a34a11e0a0cd899bca20468f42ba9752468057c09cd26700564fcbac8c4073947ced875c2b6bd7fd3f63343987ccce3be6ebe3eb8431c5e2862ff521bb3b9538862a6d8c49bf6e6da95a; ttwid=1%7C5MlWCBGC8JoKOa3YunjpyKMo9N5SZAiZizHRcFvwWKc%7C1687556106%7C35c9b03998613b4ebf39b09355191ce09f698bb1156d4b27dff7e0fb19678220; msToken=xGwLm3J4MoiRHKMHbnXzqGVLxdRX-EEFSa4jPp_tnrUR4cUZcTReV4otxbwLSgicYRG8RZ-dYPMlGjoJZEQtCxlgOWml5i1qwuKv-09zS2xlAaEQoiLdZDFHd4UIJ6YWFVrxhER7KDj_wg==; msToken=xGwLm3J4MoiRHKMHbnXzqGVLxdRX-EEFSa4jPp_tnrUR4cUZcTReV4otxbwLSgicYRG8RZ-dYPMlGjoJZEQtCxlgOWml5i1qwuKv-09zS2xlAaEQoiLdZDFHd4UIJ6YWFVrxhER7KDj_wg=='
           }
if mod=="1":
      while True:
            text = random.choice(words)
            sleep(5)
            rid = requests.get(url=uid, headers=hc).text
            dataa = json.loads(rid)
            id = dataa['itemList'][0]['id']
            url = f'https://www.tiktok.com/api/comment/publish/?aid=1988&app_language=ar&app_name=tiktok_web&aweme_id={id}&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7220834648023729665&device_platform=web_pc&focus_state=true&from_page=video&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=SA&referer=&region=SA&screen_height=1080&screen_width=1920&text=%D8%A7%D8%B3%D8%AA%D8%BA%D9%81%D8%B1%D8%A7%D9%84%D9%84%D9%87&text_extra=%5B%5D&tz_name=Asia%2FRiyadh&webcast_language=ar&msToken=y7SN__Ui7P0qpM0Jfru7aM9c5FDjiE1JFrLOkTTDQPaW_E3uEvSC4YrUHO-DiX8uN4qeWDOUnAQF0xnSlo4EGfDTt4aeRV78WYLKV3nZizGq3LxfFJHYYJhVuwotKpgMqxkD&X-Bogus=DFSzxwVLvkhANtUztnBs7cYklT1B&_signature=_02B4Z6wo00001iGcQ6wAAIDD.-obChl-FNYhnEcAAOz.58'
            data =f'aid=1988&app_language=ar&app_name=tiktok_web&aweme_id={id}&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7220834648023729665&device_platform=web_pc&focus_state=true&from_page=video&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=SA&referer=&region=SA&screen_height=1080&screen_width=1920&text='+text+'&text_extra=%5B%5D&tz_name=Asia%2FRiyadh&webcast_language=ar&msToken=y7SN__Ui7P0qpM0Jfru7aM9c5FDjiE1JFrLOkTTDQPaW_E3uEvSC4YrUHO-DiX8uN4qeWDOUnAQF0xnSlo4EGfDTt4aeRV78WYLKV3nZizGq3LxfFJHYYJhVuwotKpgMqxkD&X-Bogus=DFSzxwVLvkhANtUztnBs7cYklT1B&_signature=_02B4Z6wo00001iGcQ6wAAIDD.-obChl-FNYhnEcAAOz.58'  
            send = requests.post(url,headers=headers,data=data).text
            if '"status_msg":"تم إرسال التعليق بنجاح"' in send:
                  hit+=1      
            else:
                  bad+=1
            print(Fore.LIGHTCYAN_EX+f"comment:{text}\ndone:[{hit}]    bad:[{bad}]\n",end="\r")
            
elif mod=="2":
      text = input("set ur comment:")
      while True:
            if  len(text) < 151:

                  sleep(20)
                  rid = requests.get(url=uid, headers=hc).text
                  dataa = json.loads(rid)
                  id = dataa['itemList'][0]['id']
                  url = f'https://www.tiktok.com/api/comment/publish/?aid=1988&app_language=ar&app_name=tiktok_web&aweme_id={id}&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7220834648023729665&device_platform=web_pc&focus_state=true&from_page=video&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=SA&referer=&region=SA&screen_height=1080&screen_width=1920&text=%D8%A7%D8%B3%D8%AA%D8%BA%D9%81%D8%B1%D8%A7%D9%84%D9%84%D9%87&text_extra=%5B%5D&tz_name=Asia%2FRiyadh&webcast_language=ar&msToken=y7SN__Ui7P0qpM0Jfru7aM9c5FDjiE1JFrLOkTTDQPaW_E3uEvSC4YrUHO-DiX8uN4qeWDOUnAQF0xnSlo4EGfDTt4aeRV78WYLKV3nZizGq3LxfFJHYYJhVuwotKpgMqxkD&X-Bogus=DFSzxwVLvkhANtUztnBs7cYklT1B&_signature=_02B4Z6wo00001iGcQ6wAAIDD.-obChl-FNYhnEcAAOz.58'
                  data =f'aid=1988&app_language=ar&app_name=tiktok_web&aweme_id={id}&browser_language=ar&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7220834648023729665&device_platform=web_pc&focus_state=true&from_page=video&history_len=3&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=SA&referer=&region=SA&screen_height=1080&screen_width=1920&text='+text+'&text_extra=%5B%5D&tz_name=Asia%2FRiyadh&webcast_language=ar&msToken=y7SN__Ui7P0qpM0Jfru7aM9c5FDjiE1JFrLOkTTDQPaW_E3uEvSC4YrUHO-DiX8uN4qeWDOUnAQF0xnSlo4EGfDTt4aeRV78WYLKV3nZizGq3LxfFJHYYJhVuwotKpgMqxkD&X-Bogus=DFSzxwVLvkhANtUztnBs7cYklT1B&_signature=_02B4Z6wo00001iGcQ6wAAIDD.-obChl-FNYhnEcAAOz.58'

                  
                  
                  send = requests.post(url,headers=headers,data=data).text
                  if '"status_msg":"تم إرسال التعليق بنجاح"' in send:
                        hit+=1
                        
                  else:
                        bad+=1
                  print(Fore.LIGHTCYAN_EX+f"comment:{text}\ndone:[{hit}]    bad:[{bad}]\n",end="\r",flush=True)
            else:
                  print(Fore.LIGHTMAGENTA_EX+f"{banner}Characters must be less than 150")
                  exit()