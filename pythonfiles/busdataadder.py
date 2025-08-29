import mysql.connector
import random
# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database='busapp1'
)
# Create a cursor object to execute SQL statements
cursor = conn.cursor()

def create_tables():
    user='''CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        default_image int 
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
        user_id int NOT NULL,
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
    print('sucees creating')
create_tables()

data=[  ('Chennai', 'Coimbatore', 500), ('Chennai', 'Madurai', 450),
  ('Chennai', 'Tiruchirappalli', 350),('Chennai', 'Salem', 350),
  ('Chennai', 'Tirunelveli', 600),('Chennai', 'Vellore', 150),
  ('Chennai', 'Erode', 400),('Chennai', 'Thanjavur', 350),
  ('Chennai', 'Tiruppur', 450), ('Chennai', 'Kanyakumari', 700),
  ('Chennai', 'Virudhunagar', 500),('Chennai', 'Karur', 300),('Chennai', 'Nagercoil', 650),
  ('Chennai', 'Kanchipuram', 75),  ('Chennai', 'Tambaram', 20),
  ('Chennai', 'Cuddalore', 200),  ('Chennai', 'Tiruvannamalai', 200),
  ('Chennai', 'Villupuram', 160),  ('Chennai', 'Kumbakonam', 290),
  ('Chennai', 'Pollachi', 550),  ('Chennai', 'Neyveli', 250),
  ('Chennai', 'Dindigul', 430),  ('Coimbatore', 'Madurai', 250),
  ('Coimbatore', 'Tiruchirappalli', 200),
  ('Coimbatore', 'Salem', 250),  ('Coimbatore', 'Tirunelveli', 500),  ('Coimbatore', 'Vellore', 350),
        ('Coimbatore', 'Erode', 150), ('Coimbatore', 'Thanjavur', 300),
  ('Coimbatore', 'Tiruppur', 50),  ('Coimbatore', 'Kanyakumari', 600),
  ('Coimbatore', 'Karur', 200),
  ('Coimbatore', 'Nagercoil', 550),  ('Coimbatore', 'Kanchipuram', 425),
  ('Coimbatore', 'Tambaram', 400),  ('Coimbatore', 'Cuddalore', 400),
  ('Coimbatore', 'Tiruvannamalai', 450),  ('Coimbatore', 'Villupuram', 410),
  ('Coimbatore', 'Kumbakonam', 390),  ('Coimbatore', 'Pollachi', 50),
  ('Coimbatore', 'Neyveli', 400),  ('Coimbatore', 'Dindigul', 280),
  ('Madurai', 'Tiruchirappalli', 150),
  ('Madurai', 'Salem', 300),  ('Madurai', 'Tirunelveli', 300),
  ('Madurai', 'Vellore', 400),  ('Madurai', 'Erode', 300),
  ('Madurai', 'Thanjavur', 200),
  ('Madurai', 'Tiruppur', 400),  ('Madurai', 'Kanyakumari', 650),
  ('Madurai', 'Karur', 200),  ('Madurai', 'Nagercoil', 550),
  ('Madurai', 'Kanchipuram', 450),  ('Madurai', 'Tambaram', 425),
  ('Madurai', 'Cuddalore', 425), ('Madurai', 'Tiruvannamalai', 475),
  ('Madurai', 'Villupuram', 435), ('Madurai', 'Kumbakonam', 415),
  ('Madurai', 'Pollachi', 350),
  ('Madurai', 'Neyveli', 425),
  ('Madurai', 'Dindigul', 200),
  ('Tiruchirappalli', 'Salem', 200),
  ('Tiruchirappalli', 'Tirunelveli', 250),
  ('Tiruchirappalli', 'Vellore', 250),  ('Tiruchirappalli', 'Erode', 250),
  ('Tiruchirappalli', 'Thanjavur', 100),  ('Tiruchirappalli', 'Tiruppur', 350),
  ('Tiruchirappalli', 'Kanyakumari', 550),  ('Tiruchirappalli', 'Karur', 100),
  ('Tiruchirappalli', 'Nagercoil', 500),  ('Tiruchirappalli', 'Kanchipuram', 375),
  ('Tiruchirappalli', 'Tambaram', 350),  ('Tiruchirappalli', 'Cuddalore', 350),
  ('Tiruchirappalli', 'Tiruvannamalai', 400),('Tiruchirappalli', 'Villupuram', 360),
  ('Tiruchirappalli', 'Kumbakonam', 340),  ('Tiruchirappalli', 'Pollachi', 450),
  ('Tiruchirappalli', 'Neyveli', 350),  ('Tiruchirappalli', 'Dindigul', 230),
  ('Tiruchirappalli', 'Madurai', 140),  ('Salem', 'Tirunelveli', 400),
  ('Salem', 'Vellore', 200),  ('Salem', 'Erode', 100),
  ('Salem', 'Thanjavur', 250),
  ('Salem', 'Tiruppur', 250),
  ('Salem', 'Kanyakumari', 650),
  ('Salem', 'Karur', 250),  ('Salem', 'Nagercoil', 600),
  ('Salem', 'Kanchipuram', 475),
  ('Salem', 'Tambaram', 450),  ('Salem', 'Cuddalore', 450),
  ('Salem', 'Tiruvannamalai', 500),  ('Salem', 'Villupuram', 460),
  ('Salem', 'Kumbakonam', 440),
  ('Salem', 'Pollachi', 350),  ('Salem', 'Neyveli', 450),
  ('Salem', 'Dindigul', 330),  ('Virudhunagar', 'Chennai', 500),
    ('Virudhunagar', 'Madurai', 50),
    ('Virudhunagar', 'Tiruchirappalli', 175),    ('Virudhunagar', 'Coimbatore', 275),
    ('Virudhunagar', 'Tirunelveli', 75),
    ('Virudhunagar', 'Vellore', 400),    ('Virudhunagar', 'Erode', 300),
    ('Virudhunagar', 'Thanjavur', 225),    ('Virudhunagar', 'Tiruppur', 250),
    ('Virudhunagar', 'Kanyakumari', 300),
    ('Tirunelveli', 'Vellore', 450),    ('Tirunelveli', 'Erode', 500),
    ('Tirunelveli', 'Thanjavur', 400),    ('Tirunelveli', 'Tiruppur', 550),
    ('Tirunelveli', 'Kanyakumari', 100),    ('Tirunelveli', 'Karur', 400),
    ('Tirunelveli', 'Nagercoil', 50),
    ('Tirunelveli', 'Kanchipuram', 475),    ('Tirunelveli', 'Tambaram', 450),
    ('Tirunelveli', 'Cuddalore', 450),
    ('Tirunelveli', 'Tiruvannamalai', 500),
    ('Tirunelveli', 'Kumbakonam', 440),
    ('Tirunelveli', 'Pollachi', 350),    ('Tirunelveli', 'Neyveli', 450),
    ('Tirunelveli', 'Dindigul', 330),    ('Vellore', 'Tiruppur', 270),
    ('Vellore', 'Salem', 240),
    ('Vellore', 'Erode', 300),
    ('Vellore', 'Thanjavur', 300),
    ('Vellore', 'Tiruppur', 350),
    ('Vellore', 'Kanyakumari', 550),    ('Vellore', 'Karur', 250),    ('Vellore', 'Nagercoil', 500),
    ('Vellore', 'Kanchipuram', 375),
    ('Vellore', 'Tambaram', 350),    ('Vellore', 'Cuddalore', 350),
    ('Vellore', 'Tiruchirappalli', 275),    ('Vellore', 'Tiruvannamalai', 400),
    ('Vellore', 'Villupuram', 360),    ('Vellore', 'Kumbakonam', 340),
    ('Vellore', 'Pollachi', 450),
    ('Vellore', 'Neyveli', 350),    ('Vellore', 'Dindigul', 230),
    ('Erode', 'Thanjavur', 300),    ('Erode', 'Tiruppur', 50),
    ('Erode', 'Kanyakumari', 600),
    ('Erode', 'Karur', 150),    ('Erode', 'Nagercoil', 550),
    ('Erode', 'Kanchipuram', 425),
    ('Erode', 'Tambaram', 400),    ('Erode', 'Cuddalore', 400),
    ('Erode', 'Tiruvannamalai', 450),    ('Erode', 'Villupuram', 410),
    ('Erode', 'Kumbakonam', 390),    ('Erode', 'Pollachi', 50),
    ('Erode', 'Neyveli', 400),    ('Erode', 'Dindigul', 280),
    ('Thanjavur', 'Tiruppur', 350),    ('Thanjavur', 'Kanyakumari', 700),
    ('Thanjavur', 'Karur', 250),    ('Thanjavur', 'Nagercoil', 650),
    ('Thanjavur', 'Kanchipuram', 525),
    ('Thanjavur', 'Tambaram', 500),    ('Thanjavur', 'Cuddalore', 500),
    ('Thanjavur', 'Tiruvannamalai', 550),    ('Thanjavur', 'Villupuram', 510),
    ('Thanjavur', 'Kumbakonam', 490),
    ('Thanjavur', 'Pollachi', 400),    ('Thanjavur', 'Neyveli', 500),
    ('Thanjavur', 'Dindigul', 380),    ('Tiruppur', 'Kanyakumari', 650),
    ('Tiruppur', 'Karur', 100),    ('Tiruppur', 'Nagercoil', 600),
    ('Tiruppur', 'Kanchipuram', 475),    ('Tiruppur', 'Tambaram', 450),
    ('Tiruppur', 'Cuddalore', 450),
    ('Tiruppur', 'Tiruvannamalai', 500),    ('Tiruppur', 'Villupuram', 460),
    ('Tiruppur', 'Kumbakonam', 440),    ('Tiruppur', 'Pollachi', 350),
    ('Tiruppur', 'Neyveli', 450),
    ('Tiruppur', 'Dindigul', 330),    ('Kanyakumari', 'Karur', 550),
    ('Kanyakumari', 'Nagercoil', 50),    ('Kanyakumari', 'Kanchipuram', 525),
    ('Kanyakumari', 'Tambaram', 500),
    ('Kanyakumari', 'Cuddalore', 500),    ('Kanyakumari', 'Tiruvannamalai', 550),
    ('Kanyakumari', 'Villupuram', 510),    ('Kanyakumari', 'Kumbakonam', 490),
    ('Kanyakumari', 'Pollachi', 400),
    ('Kanyakumari', 'Neyveli', 500),    ('Kanyakumari', 'Dindigul', 380),
    ('Kanchipuram', 'Chennai', 75),    ('Kanchipuram', 'Madurai', 450),
    ('Kanchipuram', 'Vellore', 125),
    ('Kanchipuram', 'Tirupati', 120),
    ('Kanchipuram', 'Mahabalipuram', 70),
    ('Kanchipuram', 'Pondicherry', 120),
    ('Kanchipuram', 'Bengaluru', 280),    ('Kanchipuram', 'Madurai', 450),
    ('Kanchipuram', 'Coimbatore', 425),    ('Kanchipuram', 'Tiruchirappalli', 375),
    ('Kanchipuram', 'Salem', 475),
    ('Kanchipuram', 'Tirunelveli', 475),
    ('Cuddalore', 'Dindigul', 280),    ('Cuddalore', 'Chennai', 200),
    ('Cuddalore', 'Vellore', 350),    ('Cuddalore', 'Tirupati', 250),
    ('Cuddalore', 'Mahabalipuram', 180),    ('Cuddalore', 'Pondicherry', 25),
    ('Cuddalore', 'Bengaluru', 380),
    ('Cuddalore', 'Madurai', 450),    ('Cuddalore', 'Coimbatore', 400),
    ('Cuddalore', 'Tiruchirappalli', 350),
    ('Cuddalore', 'Salem', 330),    ('Cuddalore', 'Tirunelveli', 500),    ('Nagercoil', 'Chennai', 650),
    ('Nagercoil', 'Coimbatore', 550),    ('Nagercoil', 'Madurai', 550),
    ('Nagercoil', 'Tiruchirappalli', 500),    ('Nagercoil', 'Salem', 600),    ('Nagercoil', 'Tirunelveli', 50),
    ('Nagercoil', 'Vellore', 650),
    ('Nagercoil', 'Erode', 550),    ('Nagercoil', 'Thanjavur', 650),
    ('Nagercoil', 'Tiruppur', 600),    ('Nagercoil', 'Kanyakumari', 50),
    ('Namakkal', 'Chennai', 360),    ('Namakkal', 'Coimbatore', 110),
    ('Namakkal', 'Madurai', 140),    ('Namakkal', 'Tiruchirappalli', 75),
    ('Namakkal', 'Salem', 45),    ('Nagercoil', 'Dindigul', 300),
    ('Namakkal', 'Tirunelveli', 380),   ('Namakkal', 'Vellore', 220),
    ('Nagercoil', 'Kanchipuram', 525),    ('Namakkal', 'Erode', 60),
    ('Namakkal', 'Thanjavur', 130),    ('Namakkal', 'Tiruppur', 90),
    ('Namakkal', 'Kanyakumari', 460),    ('Namakkal', 'Kanchipuram', 300),
]
sql_insert = """
    INSERT INTO places (place1, place2, distance) VALUES (%s, %s, %s)
"""
for row in data:
    cursor.execute(sql_insert, row)
# Commit the changes to the database
insert_query = '''
INSERT INTO bus_routes (bus_id, place, sequence)
VALUES (%s, %s, %s)
'''
cities = [
    "Chennai",
    "Coimbatore",
    "Madurai",
    "Tiruchirappalli",
    "Salem",
    "Tiruppur",
    "Erode",
    "Vellore",
    "Thanjavur",
    "Dindigul",
    "Virudhunagar",
    "Nagercoil",
    "Cuddalore",
    "Kanchipuram",
    "Tirunelveli",
    "Namakkal"
]
# Populate the "bus_routes" table for each bus
for bus_id in range(1, 12):  # Assuming 11 buses with IDs from 1 to 11
    lis=[]
    for i in range(1,random.randint(6,10)):
        while True:
            place =random.choice(cities)
            if place not in lis:
                break
        lis.append(place)
        cursor.execute(insert_query, (bus_id, place, i))

bus_data = [
    (1,"Rockfort Express", 4, 100,"MondayTuesday","no","09:00:00", 4, 10),
    (2,"Sunshine Travels", 6, 103,"no","2023-08-09","10:30:00", 5, 12),
    (3,"Silver Arrow", 6, 103, "no","2023-08-09","12:00:00", 3, 8),
    (4,"Rajdhani Express", 2, 70,"MondayTuesday","no", "10:30:00", 5, 12),
    (5,"Shatabdi Deluxe", 8, 110, "no","2023-08-12","12:00:00", 3, 8),
    (6,"Vrindavan Express", 9, 113,"no", "2023-08-13","09:00:00", 4, 10),
    (7,"Himalayan Queen", 7, 109,"MondayTuesday","no","10:30:00", 5, 12),
    (8,"Deccan Odyssey", 15, 130,"no", "2023-08-15","04:00:00", 3, 8),
    (9,"Ganga Sagar", 24, 200, "MondayTuesday","no","09:00:00", 4, 10),
    (10,"Konkan Kanya", 9, 113,"no", "2023-08-12","1:30:00", 5, 12),
    (11,"Malabar Express", 15, 130,"no", "2023-08-20","12:00:00", 3, 8)
]
insert_query = '''INSERT INTO bus (bus_id,bus_name,cost_per_km,
speed_km_per_h,days_column,date_column,departure_time, no_of_columns,
no_of_rows) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s)'''
# Execute the insert query for each bus
cursor.executemany(insert_query, bus_data)
print('data added')
conn.commit()
cursor.close()
conn.close()
