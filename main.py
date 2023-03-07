# This is a sample Python script.
import openpyxl
import pandas
import xlrd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import random
import string
# NAME = 'Resource/23_02_22.xls'
# NAME = 'Resource/english_word.xls'
NAME = 'Resource/23_03_07.xls'

def recite_jp(NAME):

    worksheet = xlrd.open_workbook(NAME)
    sheet_names = worksheet.sheet_names()
    print(sheet_names)
    for sheet_name in sheet_names:
        sheet = worksheet.sheet_by_name(sheet_name)


        cols_kanji = sheet.col_values(1)  # 获取第二列内容， 数据格式为此数据的原有格式（原：字符串，读取：字符串；  原：浮点数， 读取：浮点数）
        # print(cols_kanji)
        # print(cols_kanji[2])

        cols_hirakana = sheet.col_values(0)

        allWords = 40
        count = 0
        batu = []
        list_n = random.sample(range(1, 167), allWords)

        for n in range(len(list_n)):

            if cols_kanji[list_n[n]] != '':
                print("请输入 "+str(cols_kanji[list_n[n]])+" 对应的假名：")
                a = input()
                if a == cols_hirakana[list_n[n]]:
                    print("正确")
                    count = count+1
                else:
                    print("错误, 正确答案为 "+str(cols_hirakana[list_n[n]]))
                    batu.append(list_n[n])

        print("您的总得分为：" + str(count/allWords * 100))

        while len(batu) != 0:
            print("错题循环")
            n=0
            for i in range(len(batu)-n):

                print("请输入 " + str(cols_kanji[batu[i-n]]) + " 对应的假名：")
                a = input()
                if a == cols_hirakana[batu[i-n]]:
                    print("正确")
                    batu.pop(i-n)
                    n = n+1
                else:
                    print("错误, 正确答案为 " + str(cols_hirakana[batu[i-n]]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    recite_jp(NAME)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
