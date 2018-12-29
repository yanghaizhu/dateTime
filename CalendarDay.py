from DateInfo import DateInfo
from Festival import Festival
from ChineseWord import ChineseWord
import datetime

def CalendarDay(now):    
    g=DateInfo(now)
    festival = ""
    luFestival = ""
    if Festival.getFestival(g, "24JQ"):
        festival = festival + "节气：" + Festival.getFestival(g, "24JQ")
    if Festival.getFestival(g, "solar"):
        festival = festival + "公历节日：" + Festival.getFestival(g, "solar")
    if Festival.getFestival(g, "week"):
        festival = festival + "周节日：" + Festival.getFestival(g, "week")
    if Festival.getFestival(g, "lunar"):
        luFestival = luFestival + "农历：" + Festival.getFestival(g, "lunar")


    twitter = \
    "今天是" + str(g.year) + "年" + str(g.month) + "月" + str(g.day) + "日" + " " \
    + ChineseWord.weekday_str(g.weekday)+"\n" + "农历" + ChineseWord.year_lunar(g.luYear) \
    + ChineseWord.month_lunar(g.luIsleap,g.luMonth) \
    + ChineseWord.day_lunar(g.luDay)+"\n" + festival+luFestival
    print(twitter)

def AddCalendarDay(now,"solar",string):    
    nowDateInfo=DateInfo(now)
    Festival.addFestival(nowDateInfo,"solar",string)

if __name__ == '__main__':
    now = datetime.datetime.now()

    CalendarDay(now)
