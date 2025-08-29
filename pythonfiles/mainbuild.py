#importing all the modules and libaraies required for the game
import os
import tkinter as t
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as u
import mysql.connector
from datetime import datetime, timedelta
from tkcalendar import DateEntry
# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database="busapp1"
)
window = u.CTk()
#taking the path of the folder
parentDirectory='d:\\desk\\codes\\Python\\resources\\'
#assigning title ,icon, resolution
window.title("WATERSORT")
window.geometry('700x900')
window.iconbitmap(os.path.join(parentDirectory, 'ico.ico') )
window.resizable(width=False, height=False)
#assigning input variables to get from the entry box and chreck for the user name an password
user = StringVar()
passw= StringVar()
# Create a cursor to interact with the database
cursor = db.cursor()
place1=StringVar()
place2=StringVar()
seats=[]
# Function to create the tables (users and bookings)
def create_tables():
    user='''CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
        );'''
    bus='''CREATE TABLE IF NOT EXISTS bus (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bus_id INT,
        bus_name VARCHAR(255) NOT NULL,
        cost_per_km INT NOT NULL,
        speed_km_per_h INT NOT NULL,
        days_column VARCHAR(255),
        date_column VARCHAR(255),
        departure_time VARCHAR(255),
        no_of_columns INT NOT NULL,
        no_of_rows INT NOT NULL
        );'''
    bookings='''CREATE TABLE IF NOT EXISTS bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        bus_name VARCHAR(255) NOT NULL,
        seat_number VARCHAR(255) NOT NULL,
        bus_id INT,
        busdate_id_date VARCHAR(255),
        booking_date VARCHAR(255)
        );'''
    places='''CREATE TABLE IF NOT EXISTS places (
        id INT AUTO_INCREMENT PRIMARY KEY,
        place1 VARCHAR(255) NOT NULL,
        place2 VARCHAR(255) NOT NULL,
        distance INT
        );'''
    routes='''CREATE TABLE IF NOT EXISTS bus_routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    bus_id INT,
    place VARCHAR(255) NOT NULL,
    sequence INT NOT NULL
    );'''
    cursor.execute(user)
    cursor.execute(bus)
    cursor.execute(bookings)
    cursor.execute(places)
    cursor.execute(routes)
    cursor.execute(user)
    cursor.execute(bus)
    cursor.execute(bookings)
    cursor.execute(places)
    cursor.execute(routes)
def clfr():#clears widgets
    for widget in window.winfo_children():
        widget.destroy()
def create_user():
    n,b=user.get(),passw.get();a=(n,b)
    #checking existence and validity
    
    sql="SELECT * FROM users WHERE username =%s"
    cursor.execute(sql,(a[0],))

    
    if cursor.fetchall():
        Label(text='Username already exist',bg='#fcc65a').place(x=276,y=700)
    else:
      if a[0]=='' or a[1]=='' or a[1].isspace() or a[0].isspace():
        Label(text='!!!invalid crendential!!!',bg='#fcc65a').place(x=278,y=700)
      else:
        query = "SELECT COUNT(*) FROM users"
        cursor.execute(query)
        row_count = cursor.fetchone()[0]
        sql = "INSERT INTO users (user_id, username, password) VALUES (%s,%s, %s)"    
        tp=(row_count+1,)+a
        cursor.execute(sql,tp )
        db.commit()
        print('saved')
def check_user():
    #gets username and password from the entry boxes
    a=user.get()
    b=passw.get()
    l='meow','meow'#a,b
    sql = "SELECT * FROM users WHERE username = %s and password= %s "
    cursor.execute(sql,(l[0],l[1]))
    cond=cursor.fetchall()
    if cond:
        sql = "SELECT * FROM users WHERE username = %s "
        cursor.execute(sql,(l[0],))
        user_id= cursor.fetchall()
        places_select(user_id)
    else:
        sql = "SELECT * FROM users WHERE username = %s "
        cursor.execute(sql,(l[0],))
        if cursor.fetchall():
          Label(text='!!!Password incorrect!!!',bg='#fcc65a').place(x=278,y=690)
        else:Label(text='!User name not found!',bg='#fcc65a').place(x=278,y=690)
def register_page():
    clfr()
    #gets new username and passwrod and creates it in the xl file
    img2=Image.open(os.path.join(parentDirectory, 'create page image.jpg'))
    test2 = ImageTk.PhotoImage(img2)
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    Label(window,text='username :',bg= '#96b35f',font=("Arial Bold",12)).place(x=176,y=420)
    Entry(window,textvariable=user,width=18).place(x=275,y=420)
    Label(window,text='password :',bg= '#96b35f',font=("Arial Bold",12)).place(x=176,y=450)
    Entry(window,textvariable=passw,show='•',width=18).place(x=275,y=450)
    u.CTkButton(window,text='Create',command=create_user,hover_color='grey',fg_color='black',corner_radius=20,bg_color='#fbc458'
                ,font=("Arial Bold",16)).place(x=280,y=500)
    u.CTkButton(window,text='Back',command=login_page,hover_color='grey',fg_color='black',corner_radius=20,bg_color='#fbc458'
                ,font=("Arial Bold",16)).place(x=280,y=570)
def login_page():
    clfr()
    #clearing widgets in previous windows
    #making the background from the img sources
    img2=Image.open(os.path.join(parentDirectory, 'login page image.jpg'))
    test2 = ImageTk.PhotoImage(img2)
    #adding it as a label
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    Label(window,text='username :',bg= '#96b35f',font=("Arial Bold",12)).place(x=176,y=400)
    #to get username
    Entry(window,textvariable=user,width=18).place(x=275,y=400)
    Label(window,text='password :',bg= '#96b35f',font=("Arial Bold",12)).place(x=176,y=430)
    #To get password
    Entry(window,textvariable=passw,show='•',width=18).place(x=275,y=430)
    #buttons 
    #calls inp which allows login of the username if present 
    u.CTkButton(window,text='LOGIN',command=check_user,hover_color='grey',
                fg_color='black',corner_radius=20,bg_color='#fbc458'
                ,font=("Arial Bold",16)).place(x=280,y=480)
    Label(text='New to water sort ?',bg='#fcc65a').place(x=290,y=540)
    #or click this to create an account
    u.CTkButton(window,text='Create Account',command=register_page
                ,hover_color='grey',fg_color='black',corner_radius=20,bg_color='#fbc458'
                ,font=("Arial Bold",16)).place(x=280,y=580)
def show_buses(user_id,time):
    giventime= time
    place11 = place1.get()
    place22= place2.get()
    places=(place11,place22)
    query = f"SELECT bus_id FROM bus_routes WHERE place = '{place11}' OR place = '{place22}';"
    cursor.execute(query)
    bus_ids = [row[0] for row in cursor.fetchall()]
    busid=[]
    for i in bus_ids:
        if bus_ids.count(i)==2:
            busid.append(i) 
    busids=[]
    for i in busid:
        if i not in  busids:
            busids+=[i]
    b=list(busids)
    for i in b:
        sql=f"SELECT sequence FROM bus_routes WHERE place = '{place11}' and bus_id='{i}';"
        cursor.execute(sql)
        seq=[]
        for j in cursor.fetchone():seq.append(j)
        sql=f"SELECT sequence FROM bus_routes WHERE place = '{place22}' and bus_id='{i}';"
        cursor.execute(sql)
        for j in cursor.fetchone():seq.append(j)
        if seq[0]>seq[1]:
            busids.remove(i)
    
    timeadist={}
    print('start',busids)
    for i in list(busids):
        print('present',busids)
        query=f'SELECT sequence FROM bus_routes WHERE bus_id="{i}" and place="{place11}"'
        cursor.execute(query)
        seqth=cursor.fetchone()[0]
        query=f'''SELECT days_column from bus WHERE bus_id="{i}"'''
        cursor.execute(query)
        y_n=cursor.fetchone()[0]
        if y_n=='no':
            query=f'''SELECT date_column from bus WHERE bus_id="{i}"'''
            cursor.execute(query)
            for j in cursor.fetchall():
                time=str(j[0])
                time= datetime.strptime(time,f'%Y-%m-%d')
        elif str(time.strftime('%A') )in y_n:
            pass
        else:
            busids.remove(i)
            continue
        print('after checking for date or days',busids)
        query=f'''SELECT departure_time from bus WHERE bus_id="{i}"'''
        cursor.execute(query)
        time2=str(cursor.fetchone()[0])
        time2= datetime.strptime(time2, '%H:%M:%S').time()
        time = datetime.combine(time, time2)
        print('its departure time',time)
        timeadist[i]=[time]
        d=0
        query=f'''SELECT speed_km_per_h from bus WHERE bus_id="{i}"'''
        cursor.execute(query)
        s=cursor.fetchone()[0]
        if 1 !=seqth:
            for k in range(1,seqth):
                query=f'''SELECT place from bus_routes WHERE bus_id="{i}"and sequence="{k}"'''
                cursor.execute(query)
                p1=cursor.fetchone()[0]
                query=f'''SELECT place from bus_routes WHERE bus_id="{i}"and sequence="{k+1}"'''
                cursor.execute(query)
                p2=cursor.fetchone()[0]
                query = '''SELECT distance from places WHERE (place1=%s AND place2=%s) OR (place1=%s AND place2=%s)'''
                cursor.execute(query, (p1, p2, p2, p1))
                distances = cursor.fetchall()
                for distance in distances:
                    d+=distance[0]
                    break
        print('distance is',d,'time is',timedelta(hours=d/s))
        timeadist[i].append(timeadist[i][0]+timedelta(hours=d/s) )
        print('get on time',timeadist[i][1])
        if  str(datetime.now()+timedelta(hours=4))<=str(timeadist[i][1] )and str(giventime)[:10]==str(timeadist[i][1])[0:10]:
            pass
        else:
            del timeadist[i];busids.remove(i)
    print('remaining',timeadist,busids)
    if busids:
        for i in busids:
            query=f'''SELECT sequence from bus_routes WHERE bus_id="{i}"and place="{place11}"'''
            cursor.execute(query)
            seq1=cursor.fetchone()[0]
            query=f'''SELECT sequence from bus_routes WHERE bus_id="{i}"and place="{place22}"'''
            cursor.execute(query)
            seq2=cursor.fetchone()[0]
            d=0
            for j in range(seq1,seq2):
                query=f'''SELECT place from bus_routes WHERE bus_id="{i}"and sequence="{j}"'''
                cursor.execute(query)
                p1=cursor.fetchone()[0]
                query=f'''SELECT place from bus_routes WHERE bus_id="{i}"and sequence="{j+1}"'''
                cursor.execute(query)
                p2=cursor.fetchone()[0]
                print(p1,p2)
                query = '''SELECT distance from places WHERE (place1=%s AND place2=%s) OR (place1=%s AND place2=%s)'''
                cursor.execute(query, (p1, p2, p2, p1))
                distances = cursor.fetchall()
                for distance in distances:
                    d+=distance[0]
                    break
            print('distance',d)
            timeadist[i].append(timeadist[i][1]+timedelta(hours=d/s))
            timeadist[i].append(d)
            timeadist[i].append(s)
    if busids:
        print(timeadist)
        show_bus_selection(user_id,timeadist,places)
    else:Label(text='no buses found for the location').pack()
def places_select(user_id):
    clfr()
    def get_selected_date(user_id):
        selected_date = str(cal.get_date())  
        
        current_datetime = datetime.now()
        if str(selected_date)>=str(current_datetime)[0:10]:
            selected_date =datetime.strptime(selected_date, f'%Y-%m-%d')
            show_buses(user_id,selected_date)
        else:print('naah')
    
    window.title("Bus Search")
    
    Button(text='back',command=login_page).pack()
    label_place1 = t.Label(window, text="Place 1:")
    label_place1.pack()
    Entry(window,textvariable=place1,width=18).pack()
    label_place2 = t.Label(window, text="Place 2:")
    label_place2.pack()
    Entry(window,textvariable=place2,width=18).pack()
    style = t.ttk.Style(window)
    style.theme_use('clam')
    style.configure("TEntry", fieldbackground='white', foreground='black')
    cal = DateEntry(window ,width=12, background='lightblue', foreground='black', borderwidth=2,
                    date_pattern='dd/MM/yyyy', font=('Arial', 12, 'bold'))
    cal.pack(padx=10, pady=10)
    button = t.Button( text="Get Date", command=get_selected_date, bg='lightblue', fg='black', font=('Arial', 12))
    button.pack(pady=5)

    submit_button = t.Button(window, text="Submit", command=lambda: get_selected_date(user_id))
    submit_button.pack()
def show_bus_selection(user_id,b,places):
    clfr()
    Button(text='getback to place selection table',command=lambda : places_select(user_id)).pack()
    for i in b:
        print(i)
        query = f'''SELECT  bus_name,cost_per_km, no_of_rows, no_of_columns FROM bus WHERE bus_id='{i}';'''
        cursor.execute(query)
        bus_details = cursor.fetchall()      
        def select_bus(user_id,i,b,places,cost,n):
            show_seat_selection(user_id,i,b,places,cost,n)
        for j, bus in enumerate(bus_details):
            print()
            bus_name,cost_per_km,no_of_rows, no_of_columns = bus
            frame = t.Frame( bd=1, relief=t.RAISED)
            frame.pack(padx=10, pady=10)
            label_name = t.Label(frame, text=f"Bus Name: {bus_name}")
            label_name.pack()
            label_departure = t.Label(frame, text=f"Departure Time: {b[i][1]}")
            label_departure.pack()
            label_arrival = t.Label(frame, text=f"arrival Time: {b[i][2]}")
            label_arrival.pack()
            label_dist = t.Label(frame, text=f"distance: {b[i][3]}")
            label_dist.pack()
            label_cost = t.Label(frame, text=f"Cost: {cost_per_km*b[i][3]}")
            label_cost.pack()
            seats_left = no_of_rows * no_of_columns
            query = f"SELECT COUNT(*) FROM bookings WHERE bus_id = '{i}'"
            cursor.execute(query)
            label_seats_left = t.Label(frame, text=f"Seats Left: {seats_left-cursor.fetchone()[0]}")
            label_seats_left.pack()
            cost=cost_per_km*(b[i][3])
            button_select = t.Button(frame, text="Select", command=lambda i=i: select_bus(user_id,i,b[i],places,cost,n=b))
            button_select.pack()    
def show_seat_selection(user_id,b,busdet,places,cost,n):
    clfr()
    window.title("Seat Selection")
    
    query=f"SELECT no_of_rows FROM bus WHERE bus_id = '{b}' "
    cursor.execute(query)
    rows =cursor.fetchone()[0]
    query=f"SELECT no_of_columns FROM bus WHERE bus_id = '{b}'"
    cursor.execute(query)
    columns = cursor.fetchone()[0]
    def seat_click(row, column):
        global seats
        seat = f"{row}-{column}"
        curr = seat_buttons[row][column].cget("bg")
        
        if curr=='white' or curr=='lightblue':
            seats+=[seat]
        else:seats.remove(seat)
        new=''
        if curr=='white' or curr=='lightblue':
            new='red'
        elif curr=='red' and column==0 or column==columns-1:
            new ='lightblue'
        else:new='white'
        seat_buttons[row][column].config(bg=new)
    sql=f'''SELECT seat_number FROM bookings WHERE bus_id='{b}' and busdate_id_date='{busdet[0]}';'''
    cursor.execute(sql)
    allseatsraw=cursor.fetchall()
    sab=[]
    for i in allseatsraw:
        for j in i:
            sab.append(j.split('-'))
    print(sab)
    seat_buttons = []
    for row in range(0,rows):
        seat_buttons.append([])
        for column in range(0,columns):
            if [str(row),str(column) ] in sab:
                button_text = f"{row+1}-{column+1}"
                button = t.Label(window, text=button_text, width=5, height=2)
                button.grid(row=row, column=column, padx=5, pady=5)
                if is_window_seat:
                    button.config(bg="grey", fg="black")
                else:
                    print('hi')
                    button.config(bg="grey", fg="black")
                seat_buttons[row].append(button)
            else:
                is_window_seat = column == 0 or column == columns -1
                button_text = f"{row+1}-{column+1}"
                button = t.Button(window, text=button_text, width=5, height=2)
                button.grid(row=row, column=column, padx=5, pady=5)
                if is_window_seat:
                    button.config(bg="lightblue", fg="black",
                            command=lambda row=row, column=column: seat_click(row, column))
                else:
                    button.config(bg="white", fg="black",
                            command=lambda row=row, column=column: seat_click(row, column))
                seat_buttons[row].append(button)
    u.CTkButton(window,text='click me',command=lambda :book(user_id,b,busdet,places,cost)
                ,hover_color='grey',fg_color='black',corner_radius=20,bg_color='#fbc458'
                ,font=("Arial Bold",16)).place(x=280,y=580)
def book(user_id,bus_id,busdet,places,cost):
    import datetime
    current_datetime = datetime.datetime.now()
    global seats
    print(bus_id,places,cost)
    for i in seats :
        sql = '''INSERT INTO bookings (bus_name, seat_number, bus_id, busdate_id_date)
         VALUES (%s,%s,%s,%s)'''
        tup=('p1',i,bus_id,busdet[0])
        cursor.execute(sql,tup)
        db.commit()
create_tables()
login_page()
window.mainloop()
