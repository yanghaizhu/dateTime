
class ChineseWord():
    def weekday_str(tm):
        a = '星期日 星期一 星期二 星期三 星期四 星期五 星期六'.split()
        return a[tm]

    def solarTerm(year, month, day):
        a = '小寒 大寒 立春 雨水 惊蛰 春分\
             清明 谷雨 立夏 小满 芒种 夏至\
             小暑 大暑 立秋 处暑 白露 秋分\
             寒露 霜降 立冬 小雪 大雪 冬至'.split()
        return

    def day_lunar(ld):
        a = '初一 初二 初三 初四 初五 初六 初七 初八 初九 初十\
             十一 十二 十三 十四 十五 十六 十七 十八 十九 廿十\
             廿一 廿二 廿三 廿四 廿五 廿六 廿七 廿八 廿九 三十'.split()
        return a[ld - 1]

    def month_lunar(le, lm):
        a = '正月 二月 三月 四月 五月 六月 七月 八月 九月 十月 十一月 十二月'.split()
        if le:
            return "闰" + a[lm - 1]
        else:
            return a[lm - 1]

    def year_lunar(ly):
        y = ly
        tg = '甲 乙 丙 丁 戊 己 庚 辛 壬 癸'.split()
        dz = '子 丑 寅 卯 辰 巳 午 未 申 酉 戌 亥'.split()
        sx = '鼠 牛 虎 兔 龙 蛇 马 羊 猴 鸡 狗 猪'.split()
        return tg[(y - 4) % 10] + dz[(y - 4) % 12] + '[' + sx[(y - 4) % 12] + ']' + '年'
