import random
import time
import sys
import datetime
import os.path
from tkinter import *
import tkinter.messagebox

class Security:
    def __init__(self, user):
       self.user = user
       
                   
    
        
    def run(self):

        root=Tk()
        root.title("거짓말탐지기")
        root.geometry("400x250")
        global cor_cnt
        global death_count
        death_count = 0
        words = []                                

        cor_cnt = 0

        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            word_path = os.path.join(BASE_DIR, 'word.txt')
            word_f=open(word_path, 'r')             
        except IOError:
            print("보안 문자 파일이 존재하지 않습니다.")
        else:
                for c in word_f:
                   words.append(c.strip())
        if words==[]:                              
            sys.exit()

        random.shuffle(words)                    # List shuffle!
        q = random.choice(words)                 # List -> words random extract!
        text=Text(root,bg="black",fg="white",width=60,height=10,font=('나눔스퀘어_ac 12'))
        text.pack(side='top')
        text.insert(END, q)
        e=Entry(root,width=60)
        e.insert(0, "위 문자를 입력해 주세요")
        e.pack()

        def btncmd():
            global cor_cnt
            global death_count
            #print(text.get("1.0",END)) # 0번째 컬럼부터 끝까지 텍스트값의 모든 내용을 가져온다는 의미
            #print(e.get()) # 엔트리 안의 모든 값을 가져온다는 의미
            if text.get("1.0",END).split()==e.get().split():
                cor_cnt+=1
                
                #label1=Label(root,text="정상 사용자입니다.")
                #label1.pack()
                root.destroy()
            else:
                text.delete("1.0",END)
                e.delete(0,END)

                random.shuffle(words)                  
                q = random.choice(words)

                text.insert(END, q)
                text.configure(state='disabled')

                if text.get("1.0",END).split()==e.get().split():     # 입력 확인(공백제거)
                    #label1=Label(root,text="정상 사용자입니다.")
                    #label1.pack()                    
                    root.destroy()
                    
                else:
                    label2=Label(root,text="불법 프로그램이 탐지되었습니니다.")
                    label2.pack()
                    death_count += 1
                    
            if death_count >= 2:
                
                tkinter.messagebox.showinfo("오류", "비 정상적인 사용입니다.\n프로그램을 종료합니다.") # 메세지박스 띄우기
                
                sys.exit()

                

        btn=Button(root,text="클릭",command=btncmd)
        btn.pack()
        word_f.close()
        
        root.mainloop()

