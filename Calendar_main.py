import tkinter as tk
from tkinter import *
from Festival import Festival
from CalendarDay import CalendarDay
import datetime
from dateutil.relativedelta import relativedelta

class APP:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.hi_there3 = tk.Button(frame, text="昨天", bg="black", fg="white", command=lambda:self.say_hi(datetime.datetime.now()+relativedelta(days = -1)))
        self.hi_there3.pack()


        self.hi_there = tk.Button(frame, text="今天", bg="gray", fg="red", command=lambda:self.say_hi(datetime.datetime.now()+relativedelta(days = 0)))
        self.hi_there.pack()

        self.hi_there2 = tk.Button(frame, text="明天", bg="black", fg="white", command=lambda:self.say_hi(datetime.datetime.now()+relativedelta(days = 1)))
        self.hi_there2.pack()

        t=tk.Text(frame,height=1,width=20)     #这里设置文本框高，可以容纳两行
        t.pack()
        
        self.e = tk.Entry(master)
        self.e.pack()
        
        self.enter = tk.Button(frame, text="确定", bg="black", fg="white", command=self.saveFile)
        self.enter.pack()
    def say_hi(self,now):
        #now = datetime.datetime.now()+relativedelta(days = 1)
        CalendarDay(now)
    def saveFile(self):
        var=self.e.get()
        AddCalendarDay(datetime.datetime.now(),"solar",var)
        print(var)

root = tk.Tk()
app = APP(root)


li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(root)          #  创建两个列表组件
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
 
listb.pack()                    # 将小部件放置到主窗口中

root.mainloop()                 # 进入消息循环
