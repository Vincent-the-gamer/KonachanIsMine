# Developed by 诡锋
# bilibili/网易云音乐：诡锋丶The_Joker
# Youtube : SmokingSexyStyle
# Github : https://github.com/vincent-the-gamer
# Version 1.0


import tkinter as tk
from tkinter import Toplevel
from PIL import Image,ImageTk
import os,base64,sys
from tkinter.messagebox import showinfo,askokcancel
import Download as dl
from tkinter.filedialog import askdirectory
import bkimage as bk

# 获取路径
def getPath(fileName):
	path = os.path.join(os.path.dirname(sys.argv[0]), fileName)
	return path

def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()
get_pic(bk.background_png, getPath('background.png'))
url = ""


def selectPath():
  path_ = askdirectory()
  path.set(path_)

def selectPath2():
  path2_ = askdirectory()
  path2.set(path2_)


# 实例化object，建立窗口window
window = tk.Tk()
path = tk.StringVar()
path2 = tk.StringVar()
#操作系统
system = "macOS"

if system == "macOS":
    path2.set('/Applications/image_urls')
    path.set('/Applications/images')
elif system == "Windows":
    path2.set('D:\\image_urls')
    path.set('D:\\images')
# 给窗口的可视化起名字
window.title('KonachanIsMine Version 1.0')

#让窗口初始化在最中间
sw = window.winfo_screenwidth() # 得到屏幕宽度
sh = window.winfo_screenheight() # 得到屏幕高度
ww = 800
wh = 600

x = (sw - ww) / 2
y = (sh - wh) / 2
# 设定窗口的大小(长 * 宽)
window.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
#window.geometry('600x400')  # 这里的乘是小x
#增加背景图片

image = Image.open(getPath('background.png'))
img = image.resize((800, 600),Image.ANTIALIAS) #resize image with high-quality
photo = ImageTk.PhotoImage(img)
background_label =tk.Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#设定标签
label = tk.Label(window,text='直接批量下载图片,选择你要保存的路径：（不是很推荐，图片很大，速度慢）',     #text为显示的文本内容
                 bg='black',fg='white',			#bg为背景色，fg为前景色
                 width=35,height=2,         	#width为标签的宽，height为高
                 wraplength=300,				#设置多少单位后开始换行
                 anchor='w').pack()

entry = tk.Entry(window, textvariable = path,width=50).pack()
              # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容
              # %v(小写大写不一样的)，当前validate的值
              # %W表示该组件的名字).pack()
button = tk.Button(window, text = "浏览", command = selectPath,width=35).pack()
page_label = tk.Label(window,text='输入你要下载的页数：（至少1页，小于1都根据1处理）',     #text为显示的文本内容
                 bg='black',fg='white',			#bg为背景色，fg为前景色
                 width=35,height=2,         	#width为标签的宽，height为高
                 wraplength=300,				#设置多少单位后开始换行
                 anchor='w').pack()
page = tk.StringVar()
page.set(1)
page_entry = tk.Entry(window,textvariable = page).pack()



def Download():
    directory = path.get()
    pages = int(page.get())
    if pages < 1: pages = 1
    if(pages is not None and pages != "") and (directory is not None and directory != ""):
       if askokcancel('即将开始下载图片', '确定要开始下载吗？\n注意，下载过程中不会有GUI展示（因为我懒！）'):
           showinfo("正在下载中", "正在下载中，请不要关闭程序！！！")
           dl.executeImages(pages,directory)
           top = Toplevel()
           top.title('图片下载完毕！')

       # 让窗口初始化在最中间
       sw = top.winfo_screenwidth()  # 得到屏幕宽度
       sh = top.winfo_screenheight()  # 得到屏幕高度
       ww = 600
       wh = 300
       x = (sw - ww) / 2
       y = (sh - wh) / 2
       # 设定窗口的大小(长 * 宽)
       top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
       # window.geometry('600x400')  # 这里的乘是小x
       label = tk.Label(top, text="下载完毕！")
       label.pack()
       label2 = tk.Label(top, text="文件路径：" + directory)
       label2.pack()
       button = tk.Button(top, text="打开文件夹", command=lambda: open_dir('macOS', directory))
       button.pack()

    else:
        showinfo('路径为空或页数不正确！', '路径为空或页数不正确！')

download = tk.Button(window, text = "下载", command = Download ,width = 20).pack()


label2 = tk.Label(window,text='下载图片URL地址,选择你要保存的路径：(非常推荐，速度巨快！）',     #text为显示的文本内容
                 bg='black',fg='white',			#bg为背景色，fg为前景色
                 width=35,height=2,         	#width为标签的宽，height为高
                 wraplength=300,				#设置多少单位后开始换行
                 anchor='w').pack()

entry2 = tk.Entry(window, textvariable = path2,width = 50).pack()
              # %P表示 当输入框的值允许改变，该值有效。该值为当前文本框内容
              # %v(小写大写不一样的)，当前validate的值
              # %W表示该组件的名字).pack()
button2 = tk.Button(window, text = "浏览", command = selectPath2).pack()
page_label2 = tk.Label(window,text='输入你要下载的页数：（至少1页，小于1都根据1处理）',     #text为显示的文本内容
                 bg='black',fg='white',			#bg为背景色，fg为前景色
                 width=35,height=2,         	#width为标签的宽，height为高
                 wraplength=300,				#设置多少单位后开始换行
                 anchor='w').pack()
page2 = tk.StringVar()
page2.set(1)
page_entry2 = tk.Entry(window,textvariable = page2).pack()

def open_dir(system,path):
  if system == 'macOS':
    import subprocess
    subprocess.call(["open", path])
  elif system == 'Windows':
      import os
      os.startfile(path)



def getUrl():
    directory = path2.get()
    pages = int(page2.get())
    if pages < 1 : pages = 1
    if(pages is not None and pages != "") and (directory is not None and directory != ""):
        if askokcancel('即将开始获取URL！', '确定要开始获取吗？\n注意，获取过程中不会有GUI展示（因为我懒！）'):
            showinfo("正在获取中","正在获取中，请不要关闭程序！！！")
            dl.executeUrls(pages,directory)
            top = Toplevel()
            top.title('URL获取完毕！')

        # 让窗口初始化在最中间
        sw = top.winfo_screenwidth()  # 得到屏幕宽度
        sh = top.winfo_screenheight()  # 得到屏幕高度
        ww = 600
        wh = 300
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        # 设定窗口的大小(长 * 宽)
        top.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        # window.geometry('600x400')  # 这里的乘是小x
        label = tk.Label(top,text="获取完毕！")
        label.pack()
        label2 = tk.Label(top, text="文件路径："+directory)
        label2.pack()
        button = tk.Button(top,text="打开文件夹",command = lambda: open_dir(system,directory))
        button.pack()

    else:
        showinfo('路径为空或页数不正确！','路径为空或页数不正确！')




download = tk.Button(window, text = "下载", command = getUrl).pack()
# 第6步，主窗口循环显示
label3 = tk.Label(window,text='该软件的功能是批量下载Konachan.com的高清图片，\n或者获取图片url，很多是4K的，所以下载速度会较慢。\n'
                              '我比较懒，运行过程中没有进度条，运行完了会有提示，不要在意了2333\n'
                              '如果你嫌下载慢，可以获取URL以后用下载软件批量下载。\n'
                              'macOS默认在Applications文件夹生成文件夹，Windows端默认在D盘根目录生成文件夹存放文件。\n'
                                   '开发者：诡锋\n'
                                  'bilibili/网易云音乐：诡锋丶The_Joker\n'
                                   'Github: https://github.com/vincent-the-gamer\n'
                              '版本V1.0\n',     #text为显示的文本内容
                 bg='black',fg='white',			#bg为背景色，fg为前景色
                 width=40,height=12,         	#width为标签的宽，height为高
                 wraplength=350,				#设置多少单位后开始换行
                 anchor='w').pack()



window.mainloop()



# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。