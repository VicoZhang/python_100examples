"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
import datetime
year = eval(input("年"))
month = eval(input("月"))
day = eval(input("日"))
date = datetime.date(year, month, day)
print(date.strftime('%j'))
