import re
import datetime
from DateInfo import DateInfo
class Festival():
    def addFestival(dateInfo,mode,string):
        if mode =="solar":
            fileName = "solar.dat"
            checkStr = "#"
            checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
            checkStr += str(dateInfo.day) if dateInfo.day > 9 else "0" + str(dateInfo.day)
            checkStr += "#"
        elif mode == "lunar":
            fileName = "lunar.dat"
            checkStr = "#"
            checkStr += str(dateInfo.luMonth) if dateInfo.luMonth > 9 else "0" + str(dateInfo.luMonth)
            checkStr += str(dateInfo.luDay) if dateInfo.luDay > 9 else "0" + str(dateInfo.luDay)
            checkStr += "#"
        elif mode == "week":
            fileName = "week.dat"
            checkStr = "#"
            checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
            checkStr += str(dateInfo.weekDayNum) + str(dateInfo.weekday)
            checkStr += "#"
            if dateInfo.lastweekDay == 1 and dateInfo.weekDayNum == 4:
                checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
                checkStr += str(dateInfo.weekDayNum+1) + str(dateInfo.weekday)
                checkStr += "#"                
        file = open(fileName,'a')
        file.write(',"'+checkStr+string+'",')
        file.close()


            
    def getFestival(dateInfo,mode):
        if mode =="solar":
            fileName = "solar.dat"
            checkStr = "#"
            checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
            checkStr += str(dateInfo.day) if dateInfo.day > 9 else "0" + str(dateInfo.day)
            checkStr += "#"
        elif mode == "lunar":
            fileName = "lunar.dat"
            checkStr = "#"
            checkStr += str(dateInfo.luMonth) if dateInfo.luMonth > 9 else "0" + str(dateInfo.luMonth)
            checkStr += str(dateInfo.luDay) if dateInfo.luDay > 9 else "0" + str(dateInfo.luDay)
            checkStr += "#"
        elif mode == "week":
            fileName = "week.dat"
            checkStr = "#"
            checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
            checkStr += str(dateInfo.weekDayNum) + str(dateInfo.weekday)
            checkStr += "#"
            if dateInfo.lastweekDay == 1 and dateInfo.weekDayNum == 4:
                checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
                checkStr += str(dateInfo.weekDayNum+1) + str(dateInfo.weekday)
                checkStr += "#"
        elif mode == "24JQ":
            fileName = "24JQ.dat"
            checkStr = "#"
            checkStr += str(dateInfo.month) if dateInfo.month > 9 else "0" + str(dateInfo.month)
            checkStr += str(dateInfo.day) if dateInfo.day > 9 else "0" + str(dateInfo.day)
            checkStr += "#"
            file = open(fileName,'w')
            arr = Festival.gen24JQFile(dateInfo.year%100)
            file.write(arr)
            file.close()
            
        file = open(fileName,'r')
        arrayTxt = file.read()
        file.close()
        pat = ',(.*?),'
        sFtv = re.compile(pat, re.S|re.M).findall(arrayTxt)

        patCheck = '#(.*?)#'
        checkStrArr = re.compile(patCheck, re.S|re.M).findall(checkStr)
        
        fstv = "#"

        for checkStrItem in checkStrArr:
            pattern = "(" + checkStrItem + ")([\w+?\#?\(?\)?\d+\s?·?]*)"
            for item in sFtv:
                result = re.search(pattern, item)
                if result is not None:
                    fstv = fstv + result.group(2) + "#"
            return fstv+"\n"
    @classmethod
    def gen24JQFile(cls,year):
        # 计算节气的C常量组
        C_Arr = [3.87, 18.73, 5.63, 20.646, 4.81, 20.1,
         5.52, 21.04, 5.678, 21.37, 7.108, 22.83,
         7.5, 23.13, 7.646, 23.042, 8.318, 23.438,
         7.438, 22.36, 7.18, 21.94, 5.4055, 20.12]
        # 节气名称组
        name_Arr = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
            "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
            "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
            "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"]
        #循环100年，计算节气日期，并创建文件
        list_arr = ""
        for i in range(0, 24):
            C = C_Arr[i]
            if i == 0 or 1 or 10 or 11:
                days = (year * 0.2422 + C) // 1 - ((year - 1) // 4)
            else:
                days = (year * 0.2422 + C) // 1 - (year // 4)
            days = int(days)
            days = '%02d' % days
            y = int(year // 1)
            m = i // 2 + 2
            if m == 13:
                m = 1
            m = '%02d' % m
            y = '%02d' % y
            strs = ",#{0}{1}#{2}#,".format(str(m), str(days), name_Arr[i])
            list_arr += strs
        return list_arr
            
if __name__ == '__main__':
    now = datetime.datetime.now()
    DateInfo(now).cout()
    print(Festival.getFestival(DateInfo(now),"24JQ"))
