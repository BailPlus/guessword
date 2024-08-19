#Copyright Bail 2024
#guessword 猜单词 v1.0_1
#2024.8.19

FILENAME = 'words.csv'
import sys,random

def readfile()->dict:
    '''读取文件
返回值:包含文件内所有单词的列表(dict)'''
    words = {}
    with open(FILENAME) as file:
        for i in file.readlines():
            word,trans = i.split()
            words[word] = trans
    return words
def askwordlen()->int:
    '''询问单词长度
返回值:用户输入的单词长度(int)'''
    return int(input('请输入单词长度 >'))
def filterword(words:dict,wordlen:str)->str:
    '''筛选单词
words(dict):单词列表
wordlen(int):单词长度
返回值: 选出的单词(str)'''
    lst = []    # 符合长度的单词
    for i in words:
        if len(i) == wordlen:
            lst.append(i)
    return random.choice(lst) if lst else None
def draw(word:str,user:str):
    '''回显评判结果(需要控制台支持)
word(str):正确的单词
user(str):用户输入的单词'''
    for i in range(len(word)):
        if user[i] == word[i]:
            print(f'\033[32m{user[i]}\033[0m',end='')
        elif user[i] in word:
            print(f'\033[33m{user[i]}\033[0m',end='')
        else:
            print(user[i],end='')
    print()
def play(word:str)->bool:
    '''开始游戏
word(str):要猜的单词
返回值:游戏成功性(bool)'''
    length = len(word)
    chance = length+1
    while True:
        print(f'你还有{chance}次机会')
        try:
            user_input = input('请输入你的猜测 >')
        except KeyboardInterrupt:
            return False
        if len(user_input) != length:
            print(f'单词长度错误。你选择的单词长度是{length}。')
            continue
        else:
            draw(word,user_input)
            if user_input == word:
                return True
        chance -= 1
        if chance==0:
            return False
def explain(word:str,trans:str):
    '''解释词义
word(str):单词
trans(str):词义'''
    print(f'【单词】{word}')
    print(f'【词义】{trans}')
def main():
    words = readfile()
    wordlen = askwordlen()
    word = filterword(words,wordlen)
    if not word:
        print('E: 当前长度暂无单词')
        return 1
    if play(word):
        print('恭喜，猜测正确！')
    else:
        print('很遗憾，猜测错误')
    explain(word,words[word])
    return 0

if __name__ == '__main__':
    sys.exit(main())