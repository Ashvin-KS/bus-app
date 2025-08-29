#importing all the modules and libaraies required for the game
import os
import tkinter as t
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import customtkinter as u
import mysql.connector
from datetime import datetime, timedelta
from tkcalendar import DateEntry
import shutil
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database="busapp1"
)
window = u.CTk()

#taking the path of the folder
parentDirectory='F:\\'
#assigning title ,icon, resolution
window.title("BUSBOOK")
window.geometry('1200x840')
window.resizable(width=False, height=False)
#assigning input variables to get from the entry box and check for the user name an password
user = StringVar()
passw= StringVar()
# Create a cursor to interact with the database
cursor = db.cursor()
window.iconbitmap(os.path.join(parentDirectory, 'images\\_6a51b688-a9a1-4255-9e3b-408d8d855b9a.ico') )
place1=StringVar()
place2=StringVar()
seats=[]
a1,b1=StringVar(),StringVar()
def create_tables():# Function to create the tables (users and bookings)
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
        cost_per_km float NOT NULL,
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
    window.configure(bg='black')
    for widget in window.winfo_children():
        widget.destroy()
def create_user():#add an user
    n,b=user.get(),passw.get();a=(n,b)
    #checking existence and validity
    
    sql="SELECT * FROM users WHERE username =%s"
    cursor.execute(sql,(a[0],))

    
    if cursor.fetchall():
        Label(text='Username already exist',bg='#fcc65a').place(x=256,y=540)
    else:
      if a[0]=='' or a[1]=='' or a[1].isspace() or a[0].isspace():
        Label(text='!!!invalid crendential!!!',bg='#fcc65a').place(x=258,y=540)
      else:
        query = "SELECT COUNT(*) FROM users"
        cursor.execute(query)
        row_count = cursor.fetchone()[0]
        sql = "INSERT INTO users (user_id, username, password,default_image) VALUES (%s,%s, %s,%s)"    
        tp=(row_count+1,)+a+(0,)
        cursor.execute(sql,tp )
        db.commit()
        login_page()       
def admin():
    clfr()
    window.geometry('1050x450')
    # Create a label to display status messages
    status_label = Label( text="", fg="red")
    status_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    Button(text='back',command=jsp).place(x=990,y=10)
    # Create a function to fetch and display user bookings from the database
    def show_user_bookings():
        user_id = user_id_entry.get()
        if user_id:
            cursor.execute("SELECT * FROM bookings WHERE user_id = %s", (user_id,))
            rows = cursor.fetchall()
            user_tree.delete(*user_tree.get_children())  # Clear the existing data in the treeview
            for row in rows:
                user_tree.insert("", "end", values=row)
        else:
            status_label.config(text="Please enter a User ID")

    # Create labels and entry fields for checking user bookings
    user_id_label = Label( text="User ID:")
    user_id_label.grid(row=0, column=3, padx=10, pady=5)
    user_id_entry = Entry()
    user_id_entry.grid(row=0, column=4, padx=10, pady=5)

    check_button =Button( text="Check Bookings", command=show_user_bookings)
    check_button.grid(row=0, column=5, padx=10, pady=5)

    # Create a treeview to display user bookings
    user_tree = ttk.Treeview( columns=("Booking ID", "Bus Name", "Seat Number", "Booking Date"), show="headings")
    user_tree.heading("Booking ID", text="Booking ID")
    user_tree.heading("Bus Name", text="Bus Name")
    user_tree.heading("Seat Number", text="Seat Number")
    user_tree.heading("Booking Date", text="Booking Date")
    user_tree.grid(row=1, column=3, columnspan=3, padx=10, pady=5)

    show_user_bookings()
def jsp():
    window.geometry('1200x840')
    login_page()
def check_user():#login checker
    #gets username and password from the entry boxes
    a=user.get()
    b=passw.get()
    l=a,b
    if a==b and a=='admin':
        admin()
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
def register_page():#gui page for creating an account
    clfr()
    #gets new username and passwrod and creates it in the xl file
    img2=Image.open(os.path.join(parentDirectory, 'images\\bussignin.png'))
    test2 = ImageTk.PhotoImage(img2)
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    Label(window,text='username ',bg= 'white',font=("Arial Bold",12)).place(x=100,y=320)
    Entry(window,textvariable=user,width=60).place(x=130,y=370)
    Label(window,text='password ',bg= 'white',font=("Arial Bold",12)).place(x=100,y=430)
    Entry(window,textvariable=passw,show='•',width=60).place(x=130,y=480)
    u.CTkButton(window,text='SIGN UP',command=create_user,hover_color='grey',
                fg_color='#022a46',corner_radius=7,bg_color='#fbc458'
                ,font=("Arial Bold",18),width=197,height=65).place(x=200,y=758)
    u.CTkButton(window,text='LOGIN',command=login_page,hover_color='grey',fg_color='#022a46',corner_radius=5,bg_color='white'
                ,font=("Arial Bold",12),width=90,height=39).place(x=472,y=35)
def login_page():#gui page for login
    clfr()
    img2=Image.open(os.path.join(parentDirectory, 'images\\buslogin.jpg'))
    test2 = ImageTk.PhotoImage(img2)
    #adding it as a label
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    Label(window,text='username',bg= 'white',font=("Arial Bold",12)).place(x=680,y=320)
    #to get username
    Entry(window,textvariable=user,width=60).place(x=700,y=370)
    Label(window,text='password',bg= 'white',font=("Arial Bold",12)).place(x=680,y=430)
    #To get password
    Entry(window,textvariable=passw,show='•',width=60).place(x=700,y=480)
    #buttons 
    #calls inp which allows login of the username if present 
    u.CTkButton(window,text='LOGIN',command=check_user,hover_color='grey',
                fg_color='#022a46',corner_radius=7,bg_color='#fbc458'
                ,font=("Arial Bold",18),width=197,height=65).place(x=1000,y=758)
    u.CTkButton(window,text='SIGNUP',command=register_page
                ,hover_color='grey',fg_color='#022a46',corner_radius=5,bg_color='white'
                ,font=("Arial Bold",12),width=90,height=39).place(x=642,y=35)
def show_buses(user_id,time):#it is the main processing of wut buses to be displayed acc to time and places

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
    
    temp=list(busid)
    busid=[]
    for i in range(0,len(temp),2):
        busid.append(temp[i])
    b=list(busid)
    for i in b:
        sql=f"SELECT sequence FROM bus_routes WHERE place = '{place11}' and bus_id='{i}';"
        cursor.execute(sql)
        seq=[]
        for j in cursor.fetchone():seq.append(j)
        sql=f"SELECT sequence FROM bus_routes WHERE place = '{place22}' and bus_id='{i}';"
        cursor.execute(sql)
        for j in cursor.fetchone():seq.append(j)
        if seq[0]>seq[1]:
            busid.remove(i)
    
    
    timeadist={}
    
    
    for i in list(busid):
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
            busid.remove(i)
            continue
       
        query=f'''SELECT departure_time from bus WHERE bus_id="{i}"'''
        cursor.execute(query)
        time2=str(cursor.fetchone()[0])
        time2= datetime.strptime(time2, '%H:%M:%S').time()
        time = datetime.combine(time, time2)
        
        timeadist[i]=[time]#departure of first stop
        d=0
        query=f'''SELECT speed_km_per_h from bus WHERE bus_id="{i}"'''
        cursor.execute(query)
        s=cursor.fetchone()[0]#speed
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
        
        timeadist[i].append(timeadist[i][0]+timedelta(hours=d/s) )#the stop where the user gets in
        
        if  str(datetime.now()+timedelta(hours=4))<=str(timeadist[i][1] )and str(giventime)[:10]==str(timeadist[i][1])[0:10]:
            pass
        else:
            del timeadist[i];busid.remove(i)
        time=giventime
    
    if busid:
        for i in busid:
            query=f'''SELECT sequence from bus_routes WHERE bus_id="{i}"and place="{place11}"'''
            cursor.execute(query)
            seq1=cursor.fetchone()[0]
            query=f'''SELECT sequence from bus_routes WHERE bus_id="{i}"and place="{place22}"'''
            cursor.execute(query)
            seq2=cursor.fetchone()[0]
            d=0
            print(seq1,seq2)
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
                print(distances)
                for distance in distances:
                    d+=distance[0]
                    break
            
            timeadist[i].append(timeadist[i][1]+timedelta(hours=d/s))#i2 -->arrival time
            timeadist[i].append(d)#i3 -->distance
            timeadist[i].append(s)#i4 -->speed
    if busid:
        
        show_bus_selection(user_id,timeadist,places)
    else:Label(text='no buses found for the location').place(x=700,y=600)
def places_select(user_id):#gui to select places
    clfr()
    
    def get_selected_date(user_id):
        selected_date = str(cal.get_date())  
        
        current_datetime = datetime.now()
        if str(selected_date)>=str(current_datetime)[0:10]:
            selected_date =datetime.strptime(selected_date, f'%Y-%m-%d')
            show_buses(user_id,selected_date)
        
    
    window.title("Bus Search")
    img2=Image.open(os.path.join(parentDirectory, 'images\\placeselectbg.jpg'))
    test2 = ImageTk.PhotoImage(img2)
    #adding it as a label
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    u.CTkFrame(window,height=600,width=900,bg_color='#1E1F33',corner_radius=50,fg_color='white').place(x=190,y=100)
    img3=Image.open(os.path.join(parentDirectory, 'images\\placeselect.png'))
    test3 = ImageTk.PhotoImage(img3)
    #adding it as a label
    label1 = t.Label(image=test3,borderwidth=0)
    label1.image = test3
    label1.place(x=280, y=150)
    u.CTkButton(window,text='🡸',width=1,corner_radius=100,
                    fg_color='black',bg_color='#272933',text_color='white',font=("Arial Bold",20),command=login_page).place(x=1140,y=10)
    Entry(textvariable=place1,width=30).place(x=365,y=320)
    Entry(textvariable=place2,width=30).place(x=367,y=430)
    style = t.ttk.Style(window)
    style.theme_use('clam')
    style.configure("TEntry", fieldbackground='white', foreground='black')
    cal = DateEntry(window ,width=12, background='lightblue', foreground='black', borderwidth=2,
                    date_pattern='dd/MM/yyyy', font=('Arial', 12, 'bold'))
    cal.place(x=710,y=320)
    u.CTkButton(window,text='submit',width=1,corner_radius=100,
                    fg_color='black',bg_color='white',text_color='white'
                    ,font=("Arial Bold",20), command=lambda: get_selected_date(user_id)).place(x=600,y=500)   
    def toggle_win():
        f1=Frame(window,width=300,height=840,bg='#12c4c0')
        f1.place(x=0,y=0)

        def dele():
            f1.destroy()
        
        Button(f1,
            text='X',
            border=0,
            command=dele,
            bg='#12c4c0',
            activebackground='#12c4c0').place(x=5,y=10)     
        u.CTkButton(f1,text='profile',width=300,font=("Arial Bold",16),fg_color='#12c4c0',hover_color='lightblue',command=
                    lambda:profile(user_id)).place(x=0,y=100)
    Button(window,text='=',
        command=toggle_win,
        border=0,
        bg='#12c4c0', font=("Arial Bold",20),
        activebackground='#262626').place(x=5,y=10)
def select_image(user_id,profile_canvas):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.ico *.webp")])

    if file_path:
        # Define the destination folder where you want to store the image
        destination_folder = parentDirectory+'Pic\\'
        
    
        shutil.copy(file_path, os.path.join(destination_folder,f'{user_id[0][1]}'+'.jpg'))
        cursor.execute(f'update users set default_image={user_id[0][1]} where user_id ="{user_id[0][1]}";')
        db.commit()
        profile_image = Image.open(file_path)
        profile_image.thumbnail((150, 150))  # Resize the image to a smaller size
        mask = Image.new('L', profile_image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, profile_image.width, profile_image.height), fill=255)
        profile_image.putalpha(mask)
        profile_photo = ImageTk.PhotoImage(profile_image)
        profile_canvas.create_image(0, 0, anchor=NW, image=profile_photo)
        profile_canvas.image = profile_photo
def checnewpass(user_id):
    new,con=a1.get(),b1.get()
    if new!=con or new=='' or con=='' or con.isspace() or new.isspace():
        Label(text='invalid password',bg='yellow').place(x=500,y=370)
    else:
        cursor.execute(f'update users set password="{new}" where user_id={user_id[0][0]} ')
        db.commit()
        profile(user_id)
def changepasswd(user_id):
    clfr()
    img2=Image.open(os.path.join(parentDirectory, 'images\\changepwd.png'))
    test2 = ImageTk.PhotoImage(img2)
    #adding it as a label
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    window.configure(bg="white")
    u.CTkButton(window,bg_color='white',fg_color='black',text='back',command=lambda:profile(user_id)).place(x=1050,y=10)
    Entry(textvariable=a1,show='•',width=60).place(x=435,y=290)
    Entry(textvariable=b1,show='•',width=60).place(x=470,y=368)
    u.CTkButton(window,bg_color='white',fg_color='black',text='submit',command=lambda:checnewpass(user_id)).place(x=500,y=420)
def profile(user_id):
    img = Image.open(os.path.join(parentDirectory, 'images\\profile.png'))
    test2 = ImageTk.PhotoImage(img)
    label0 = Label(window, image=test2)
    label0.place(x=0, y=0)
    label0.image = test2
    profile_canvas = Canvas(window,width=150, height=150, bg='white', borderwidth=0,highlightthickness=0)
    profile_canvas.place(x=1050, y=260)
    profile_image = Image.open(parentDirectory+'Pic\\'+f'{user_id[0][4]}.jpg')
    profile_image.thumbnail((150, 150))  # Resize the image to a smaller size
    mask = Image.new('L', profile_image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, profile_image.width, profile_image.height), fill=255)
    profile_image.putalpha(mask)
    profile_photo = ImageTk.PhotoImage(profile_image)
    
    profile_canvas.create_image(0, 0, anchor=NW, image=profile_photo)
    profile_canvas.image = profile_photo
    Label(text=f'{user_id[0][2]}',font=("Bradley Hand ITC",40),bg='white').place(x=650,y=280)
    u.CTkButton(window,bg_color='white',fg_color='black',text='back',
                command=lambda:places_select(user_id)).place(x=1060,y=10)
    u.CTkButton(window,bg_color='white',fg_color='black',text='change image ',
                command=lambda:select_image(user_id,profile_canvas)).place(x=80,y=300)
    u.CTkButton(window,bg_color='white',fg_color='black',text='change password ',
                command=lambda:changepasswd(user_id)).place(x=80,y=350)
def show_bus_selection(user_id,b,places):#gui page to show all the available pages acc to the user requirements
    clfr()
    img2=Image.open(os.path.join(parentDirectory, 'images\\usenow.jpg'))
    test2 = ImageTk.PhotoImage(img2)
    #adding it as a label
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    u.CTkButton(window,text='🡸',width=1,corner_radius=100,fg_color='black',bg_color='#aad3cf',text_color='white',
                font=("Arial Bold",20),command=lambda : places_select(user_id)).place(x=1140,y=10)
    for i in b:
        
        query = f'''SELECT  bus_name,cost_per_km, no_of_rows, no_of_columns FROM bus WHERE bus_id='{i}';'''
        cursor.execute(query)
        bus_details = cursor.fetchall()      
        def select_bus(user_id,i,b,places,cost):
            show_seat_selection(user_id,i,b,places,cost)
        for j, bus in enumerate(bus_details):
            
            bus_name,cost_per_km,no_of_rows, no_of_columns = bus
            frame = t.Frame(width=600,height=300)
            frame.pack_propagate(False)
            frame.pack()
            img3=Image.open(os.path.join(parentDirectory, 'images\\bus.png'))
            test3 = ImageTk.PhotoImage(img3)
            #adding it as a label
            label1 = t.Label(frame,image=test3)
            label1.image = test3
            label1.place(x=0, y=0)
            label_name = t.Label(frame,bg='white', text=f"{bus_name}",font=("Segoe \\ Bold",16)).place(x=140,y=11)
            label_departure = t.Label(frame,bg='white', text=f"{str(b[i][1])[0:19]}",font=("Segoe \\ Bold",16)).place(x=30,y=130)
            Label(frame,bg='white', text=f'{places[0]}',font=("Segoe \\ Bold",16)).place(x=90,y=56)
            Label(frame,bg='white', text=f'{places[1]}',font=("Segoe \\ Bold",16)).place(x=430,y=56)
            label_arrival = t.Label(frame,bg='white', text=f"{str(b[i][2])[0:19]}",font=("Segoe \\ Bold",16)).place(x=320,y=130)
            
            label_dist = t.Label(frame,bg='white', text=f"{b[i][3]}",font=("Segoe \\ Bold",16)).place(x=140,y=180)
            
            label_cost = t.Label(frame,bg='white', text=f"{cost_per_km*b[i][3]}",font=("Segoe \\ Bold",16)).place(x=100,y=220)
           
            seats_left = no_of_rows * no_of_columns
            query = f"SELECT COUNT(*) FROM bookings WHERE bus_id = '{i}' and busdate_id_date='{b[i][0]}'"
            cursor.execute(query)
            label_seats_left = t.Button(frame,bg='white', text=f"Seats Left: {seats_left-cursor.fetchone()[0]}",font=("Segoe \\ Bold",16),
                                         command=lambda i=i: select_bus(user_id,i,b[i],places,cost)).place(x=245,y=250)
            cost=cost_per_km*(b[i][3]) 
def show_seat_selection(user_id,b,busdet,places,cost):#shows the seats selected by the user and allows him to select
    clfr()
    img2=Image.open(os.path.join(parentDirectory, 'images\\seatselect.png'))
    test2 = ImageTk.PhotoImage(img2)
    label0 = t.Label(image=test2)
    label0.image = test2
    label0.place(x=0, y=0)
    window.configure(bg="white")
    window.title("Seat Selection")  
    query=f"SELECT no_of_rows FROM bus WHERE bus_id = '{b}' "
    cursor.execute(query)
    rows =cursor.fetchone()[0]
    query=f"SELECT no_of_columns FROM bus WHERE bus_id = '{b}'"
    cursor.execute(query)
    columns = cursor.fetchone()[0]
    global seats
    seats=[]
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
    
    seat_buttons = []
    sf=Frame(window)
    sf.place(x=510,y=100)
    for row in range(0,rows):
        seat_buttons.append([])
        for column in range(0,columns):
            if [str(row),str(column) ] in sab:
                is_window_seat = column == 0 or column == columns -1
                button_text = f"{row}-{column}"
                button = t.Label(sf, text=button_text, width=5, height=2)
                button.grid(row=row, column=column, padx=5, pady=5)
                if is_window_seat:
                    button.config(bg="grey", fg="black")
                else:
                
                    button.config(bg="grey", fg="black")
                seat_buttons[row].append(button)
            else:
                is_window_seat = column == 0 or column == columns -1
                button_text = f"{row}-{column}"
                button = t.Button(sf, text=button_text, width=5, height=2)
                button.grid(row=row, column=column, padx=5, pady=5)
                if is_window_seat:
                    button.config(bg="lightblue", fg="black",
                            command=lambda row=row, column=column: seat_click(row, column))
                else:
                    button.config(bg="white", fg="black",
                            command=lambda row=row, column=column: seat_click(row, column))
                seat_buttons[row].append(button)
    u.CTkButton(window,text='select',command=lambda :bookingpage(user_id,b,busdet,places,cost)
                ,hover_color='grey',fg_color='black',corner_radius=20,bg_color='yellow'
                ,font=("Arial Bold",16)).place(x=560,y=800)
def pdf_gen(user_id,bus_id,busdet,places,cost):
    name = user_id[0][2]
    cursor.execute(f'select bus_name from bus where bus_id={bus_id}')
    b=cursor.fetchone()[0]
    busname = str(b)
    source = str(places[0])
    destination =str( places[1])
    departure_time = str(busdet[1])[0:19]
    arrival_time =str( busdet[2])[0:19]
    fare = str(cost*len(seats))
    distance = str(busdet[3])
    seats_booked = str(seats)

    pdf = canvas.Canvas(f"{user_id[0][0]}.pdf", pagesize=letter)

    # Add an image from the specified file path
    image_path =  parentDirectory+'images//buslogo.png'
    image_x = 400
    image_y = 720
    image_width = 100
    image_height = 100

    pdf.drawImage(image_path, image_x, image_y, width=image_width, height=image_height)

    # Add the first horizontal line below the image
    pdf.line(50, image_y - 20, 550, image_y - 20)

    # Add text details below the first line, left-aligned
    text_x = 50  # Adjust the X-coordinate for left alignment
    pdf.drawString(text_x, image_y - 5, 'WanderHub')
    pdf.drawString(text_x, image_y - 40, "Name: " + name)
    pdf.drawString(text_x, image_y - 60, "Bus Name: " + busname)
    pdf.drawString(text_x, image_y - 80, "Source: " + source)
    pdf.drawString(text_x, image_y - 100, "Destination: " + destination)
    pdf.drawString(text_x, image_y - 120, "Departure Time: " + departure_time)
    pdf.drawString(text_x, image_y - 140, "Arrival Time: " + arrival_time)
    pdf.drawString(text_x, image_y - 160, "Distance: " + distance)
    pdf.drawString(text_x, image_y - 180, "Seats Booked: " + seats_booked)
    pdf.drawString(text_x, image_y - 200, "Total Cost: " + fare)

    # Add the second horizontal line below the text details
    pdf.line(50, image_y - 240, 550, image_y - 240)

    # Save the PDF
    pdf.save()
def bookingpage(user_id,bus_id,busdet,places,cost):#gui page to nook seats
    clfr()
   
    img3=Image.open(os.path.join(parentDirectory, 'images\\booking page.png'))
    test3 = ImageTk.PhotoImage(img3)
    #adding it as a label
    label1 = t.Label(window,image=test3)
    label1.image = test3
    label1.place(x=0, y=0)
    cursor.execute(f'select bus_name from bus where bus_id={bus_id}')
    b=cursor.fetchone()[0]
    u.CTkButton(window,text='EXIT',width=1,corner_radius=100,
                    fg_color='black',bg_color='white',text_color='white',font=("Arial Bold",20)
                    ,command=lambda:places_select(user_id)).place(x=10,y=10)    
    u.CTkButton(window,text='🡸',width=1,corner_radius=100,
                    fg_color='black',bg_color='white',text_color='white',font=("Arial Bold",20)
                    ,command=lambda:show_seat_selection(user_id,bus_id,busdet,places,cost)).place(x=1140,y=10)    
    Label(bg='white',font=("Comic Sans MS ",16),text=b).place(x=360,y=267)
    Label(bg='white',font=("Comic Sans MS ",16),text=places[0]).place(x=300,y=337)
    Label(bg='white',font=("Comic Sans MS ",16),text=places[1]).place(x=650,y=337)
    Label(bg='white',font=("Comic Sans MS ",15),text=str(busdet[1])[0:19]).place(x=407,y=398)
    Label(bg='white',font=("Comic Sans MS ",16),text=str(busdet[2])[0:19]).place(x=750,y=398)
    Label(bg='white',font=("Comic Sans MS ",16),text=busdet[3]).place(x=345,y=478)
    Label(bg='white',font=("Comic Sans MS ",16),text=f'{seats}').place(x=765,y=478)
    Label(bg='white',font=("Comic Sans MS ",16),text=cost*len(seats)).place(x=300,y=560)
    u.CTkButton(window,text='confirm',width=1,corner_radius=100,
                    fg_color='black',bg_color='white',text_color='white',font=("Arial Bold",20),
                    command=lambda:book(user_id,bus_id,busdet,places,cost)).place(x=700,y=600)
def book(user_id,bus_id,busdet,places,cost):#just process it
    import datetime
    current_datetime = datetime.datetime.now()
    global seats
    for i in seats:
        sql = '''INSERT INTO bookings (user_id, seat_number, bus_id, busdate_id_date,booking_date)
         VALUES (%s,%s,%s,%s,CURDATE())'''
        tup=(user_id[0][0],i,bus_id,busdet[0])
        cursor.execute(sql,tup)
        db.commit()
    pdf_gen(user_id,bus_id,busdet,places,cost)
    messagebox.showinfo("Booking status", "Booking Succesfull.")
    places_select(user_id)
login_page()
window.mainloop()

