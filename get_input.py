# coding=utf-8
# -*- coding: utf-8 -*-


# import getpass
# a = getpass.getpass("please input password:")
# print a


# python2 for windows
import msvcrt,sys
def getpass_for_windows(cue_words="Please input your password:"):    
    print cue_words
    chars = []   
    while True:  
        try:  
            newChar = msvcrt.getwch().decode(encoding="utf-8")  
        except:  
            print u"您输入有误,或者您很可能不是在cmd命令行下运行，请重新输入非汉字字符："  
            continue
        if newChar in '\r\n': # 如果是换行，则输入结束               
             break   
        elif newChar == '\b': # 如果是退格，则删除密码末尾一位并且删除一个星号   
             if chars:    
                 del chars[-1]   
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 光标回退一格  
                 msvcrt.putch( ' '.encode(encoding='utf-8')) # 输出一个空格覆盖原来的星号  
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 光标回退一格准备接受新的输入                   
        else:  
            chars.append(newChar)  
            msvcrt.putch('*'.encode(encoding='utf-8')) # 显示为星号  
    return (''.join(chars))  



# python3 for linux
# import sys, tty, termios
def getch():  
    fd = sys.stdin.fileno() 
    old_settings = termios.tcgetattr(fd) 
    try: 
        tty.setraw(sys.stdin.fileno()) 
        ch = sys.stdin.read(1) 
    finally: 
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
    return ch 
def getpass_for_linux(cue_words="Please input your password:",maskchar = "*"):
    print (cue_words)
    password = "" 
    while True: 
        ch = getch() 
    if ch == "\r" or ch == "\n":
        return password 
    elif ch == "\b" or ord(ch) == 127: 
        if len(password) > 0: 
            sys.stdout.write("\b \b") 
            password = password[:-1] 
    else: 
        if maskchar != None: 
            sys.stdout.write(maskchar) 
        password += ch 



if __name__ == "__main__":
    password = getpass_for_windows()
    print "your password is: %s" %password