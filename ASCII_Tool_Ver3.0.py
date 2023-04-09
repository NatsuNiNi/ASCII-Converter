from PIL import Image, ImageDraw, ImageFont
import webbrowser
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import CENTER
from tkinter import *
import datetime
import os
import urllib.request

# 定義字符集
char_set = '&@MW%$#84+*~_=-?>()/.,:  '

# 建立資料夾儲存圖片
path = 'ASCII_output_picture'
if not os.path.isdir(path):
    os.makedirs(path, mode=0o777)

# question_image = "https://i.pximg.net/img-master/img/2019/11/27/00/15/13/78011055_p0_master1200.jpg"
# title_image = "question.jpg"
# urllib.request.urlretrieve(question_image, title_image)

question1 = tk.Tk()
question1.title('ASCII')
question1.configure(background='#5E5E5E')
question1.geometry('600x300')
question1.resizable(False, False)
# question.iconbitmap(question_image)


title4 = tk.Label(text="ASCII 字符圖片轉換", pady=20, background='#5E5E5E', foreground='#FFFFFF', font='bold')
title4.pack(side='top',fill="x")

title1 = tk.Label(text="請輸入 RGB 值", pady=0, background='#5E5E5E', foreground='#FFFFFF')
title1.pack(side='top',fill="x")

title2 = tk.Label(text="按住 Ctrl 可以選擇多個檔案", pady=20, background='#5E5E5E', foreground='#FFFFFF')
title2.pack(side='bottom',fill="y")

title3 = tk.Label(text="請選擇轉換圖片的方式", pady=50, background='#5E5E5E', foreground='#FFFFFF')
title3.pack(side='top',fill="x")


red = tk.StringVar()
green = tk.StringVar()
blue = tk.StringVar()

def g(red_value, green_value, blue_value, image_color, path_name):
    
    with open('ascii' + path_name + '.html', 'w') as f:
            f.write('''
                    <html>
                        <body>
                            <pre>{}</pre>
                        </body>
                    </html>'''
                    )
            
    file_pathment = filedialog.askopenfilenames()
        
    for file_path in file_pathment: 
        # 清除檔案副檔名
        base_name = os.path.basename(file_path)
        file_name = os.path.splitext(base_name)[0]

        # 讀取圖片並調整大小
        image = Image.open(file_path)
        image = image.resize(((int(image.size[0]/3)), (int(image.size[1]/7))))

        # 將圖片轉換為 RGB 模式
        image = image.convert('RGB')

        # 取得圖片的像素數據
        pixels = image.load()

        # 掃描像素數據，根據像素的 RGB 值選擇相應的字符
        ascii_art = ''
        for i in range(image.size[1]):
            for j in range(image.size[0]):
                r, g, b = pixels[j, i]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                char_index = int((gray/255) * (len(char_set)-1))
                ascii_art += char_set[char_index]
            ascii_art += '\n'

        # 計算圖片大小
        char_width, char_height = ImageFont.truetype('arial.ttf', size=10).getsize(char_set[0])

        height = int(len(ascii_art.split('\n')) * char_height)
        width = int(len(ascii_art.split('\n')[0]) * char_width*0.7)

        art_image = Image.new('RGB', (width, height), color=image_color)

        # 創建繪圖檔案
        draw = ImageDraw.Draw(art_image)

        # 設置字體
        font = ImageFont.truetype('arial.ttf', size=int(char_height))

        # 掃描ASCII字符，繪製對應的矩形
        for i, line in enumerate(ascii_art.split('\n')):
            for j, char in enumerate(line):
                x = j * char_width*0.7
                y = i * char_height
                draw.text((x, y), char, font=font, fill=(red_value, green_value, blue_value))

        # 取得當前日期和時間
        now = datetime.datetime.now()

        # 將日期和時間轉換為字符串格式
        date_time_str = now.strftime('%Y%m%d%H%M%S')

        # 創建檔案名稱
        file_name_new = date_time_str + '_' + file_name +  '_ASCII_picture' + path_name + '.png'

         # 將資料夾和圖片的路徑合成
        save_path = os.path.join(path, file_name_new)
        
        # 將圖片儲存到指定的路徑
        art_image.save(save_path)

        # 將字符圖片輸出成文本文件
        with open('ascii' + path_name + '.html', 'a') as f:
            f.write('''
                    <html>
                        <body>
                            <pre>{}</pre>
                        </body>
                    </html>'''
                    .format(ascii_art))
        webbrowser.open('file://' + os.path.realpath(save_path))
    # 使用預設瀏覽器打開字符圖片
    # webbrowser.open('ascii' + path_name + '.html')
    
def ask_event():
    if red.get() != '':
        red_value = int(red.get())

    if green.get() != '':
        green_value = int(green.get())

    if blue.get() != '':
        blue_value = int(blue.get())

    image_color = 'white'
    path_name = ''

    g(red_value, green_value, blue_value, image_color, path_name)
    
def ask2_event():
    if red.get() != '':
        red_value = int(red.get())

    if green.get() != '':
        green_value = int(green.get())

    if blue.get() != '':
        blue_value = int(blue.get())

    image_color = 'black'
    path_name = '_inv'
    
    g(red_value, green_value, blue_value, image_color, path_name)

def ask6_event():

    red_value, green_value, blue_value = 0, 0, 0
    image_color = 'white'
    path_name = ''

    g(red_value, green_value, blue_value, image_color, path_name)

def ask7_event():

    image_color = 'black'
    red_value, green_value, blue_value = 255, 255, 255
    path_name = '_inv'
    
    g(red_value, green_value, blue_value, image_color, path_name)

ask3 = tk.Entry(question1, textvariable=red,)
ask3.place(x=150,y=100,anchor="center")

ask4 = tk.Entry(question1, textvariable=green)
ask4.place(x=300,y=100,anchor="center")

ask5 = tk.Entry(question1, textvariable=blue)
ask5.place(x=450,y=100,anchor="center")

ask = tk.Button(question1, text="白底彩字",command=ask_event, background="white", foreground="darkcyan")
ask.place(x=225,y=175,anchor='center')

ask2 = tk.Button(question1, text="黑底彩字",command=ask2_event, background="gray", foreground="lightcyan")
ask2.place(x=375,y=175,anchor='center')

ask6 = tk.Button(question1, text="白底黑字", command=ask6_event, background="white", foreground="black")
ask6.place(x=225,y=225,anchor='center')

ask7 = tk.Button(question1, text="黑底白字",command=ask7_event, background="gray", foreground="white")
ask7.place(x=375,y=225,anchor='center')

#ask6 = tk.Button(question1, text="確認",command=ask6_event)
#ask6.place(x=300,y=200,anchor='center')

question1.mainloop()


