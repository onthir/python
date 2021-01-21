# import modules
from tkinter import *
import sqlite3
import tkinter.messagebox
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()

# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        root.title('hospital_reservation_system')

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='aliceblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='lightsteelblue')
        self.right.pack(side=RIGHT)

        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y-%m-%d     %H시%M분')

        # labels for the window
        self.heading = Label(self.left, text="군밤 병원 예약관리시스템", font=('나눔스퀘어_ac 40'), fg='black', bg='aliceblue')
        self.heading.place(x=130, y=50)

        # labels for now_datetime
        self.nowdatetime = Text(self.left, font=('나눔스퀘어_ac 13'), bg = 'aliceblue', fg = 'gray', width = 19, height=1)
        self.nowdatetime.place(x = 610, y = 0)
        self.nowdatetime.insert(END, nowDatetime)
        self.nowdatetime.configure(state = 'disabled')
        
        # patients name
        self.name = Label(self.left, text="이       름", font=('나눔스퀘어_ac 17 bold'), fg='black', bg='aliceblue')
        self.name.place(x=200, y=150)

        # age
        self.age = Label(self.left, text="나       이", font=('나눔스퀘어_ac 17 bold'), fg='black', bg='aliceblue')
        self.age.place(x=200, y=190)

        # gender
        self.gender = Label(self.left, text="성       별", font=('나눔스퀘어_ac 17 bold'), fg='black', bg='aliceblue')
        self.gender.place(x=200, y=230)

        # location
        self.location = Label(self.left, text="주       소", font=('나눔스퀘어_ac 17 bold'), fg='black', bg='aliceblue')
        self.location.place(x=200, y=270)

        # appointment time
        self.time = Label(self.left, text="예약 시간", font=('나눔스퀘어_ac 17 bold'), fg='black', bg='aliceblue')
        self.time.place(x=200, y=310)

        # phone
        self.phone = Label(self.left, text="전화 번호", font=('나눔스퀘어_ac 17 bold'), fg='black', bg='aliceblue')
        self.phone.place(x=200, y=350)

        # 안내사항1
        self.info1 = Label(self.left, text = "☞ 예약 완료 전 꼭 읽어보세요 ☜", font = ('굴림 15 bold'),  fg = 'black', bg = 'aliceblue')
        self.info1.place(x=250, y=560)

        # 안내사항2
        self.info = Label(self.left, text = "예약 당일 반드시 원무팀 접수창구에서 예약확인 후 진료과로 가십시오.\n예약 후 내원하신 경우에도 진료실 사정에 따라 진료시간이 늦어질 수 있습니다.\n ",
                          justify = 'left', font = ('굴림 13 '), fg = 'black', bg = 'aliceblue')
        self.info.place(x=120, y=600)

        # Entries for all labels============================================================
        self.name_ent = Entry(self.left, width=25)
        self.name_ent.place(x=350, y=155)

        self.age_ent = Entry(self.left, width=25)
        self.age_ent.place(x=350, y=195)
    
        self.gender_ent = Entry(self.left, width=25)
        self.gender_ent.place(x=350, y=235)

        self.location_ent = Entry(self.left, width=25)
        self.location_ent.place(x=350, y=275)

        self.time_ent = Entry(self.left, width=25)
        self.time_ent.place(x=350, y=315)

        self.phone_ent = Entry(self.left, width=25)
        self.phone_ent.place(x=350, y=355)

        # button to perform a command
        self.submit = Button(self.left, text="예약", width=6, height=1, bg='lightsteelblue', fg='white', font=('나눔스퀘어_ac 13 bold'), command=self.add_appointment)
        self.submit.place(x=360, y=420)
    
        
        # displaying the logs in our right frame
        self.logs = Label(self.right, text="예약 현황", font=('나눔스퀘어_ac 30 bold'), fg='white', bg='lightsteelblue')
        self.logs.place(x=125, y=60)

        self.box = Text(self.right, width=50, height=30)
        self.box.place(x=25, y=140)
        #self.box.configure(state='disabled')

        self.update = Button(self.right, text = '새로고침', width = 6, height = 1, bg = 'lightsteelblue', fg = 'black', font = ('나눔스퀘어_ac 13'), command = self.data_update)
        self.update.place(x = 170, y = 570)
    
    def data_update(self):
        global id_num
        self.box.delete('1.0', END)
        # sql2 = "SELECT ID FROM appointments "
        # self.result = c.execute(sql2)
        # for self.row in self.result:
        #     self.id = self.row[0]
        #     ids.append(self.id)        
        # self.new = sorted(ids)
        # self.final_id = self.new[len(ids)-1]
        # self.box.insert(END, "마지막 ID는 " + str(self.final_id)+ "입니다.\n\n")
        datas = c.execute("SELECT DISTINCT name, scheduled_time FROM appointments")
        #datas = c.execute("SELECT name FROM appointments")
        for data in datas:
            info1 = list(data)
            self.box.insert(END, str(info1[0]) + '님 \t' + str(info1[1]) + '\n' )
            
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )
            

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()