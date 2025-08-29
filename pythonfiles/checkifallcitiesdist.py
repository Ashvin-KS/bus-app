import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="test",
    database='busapp1'
)

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

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

for i in range(len(cities)-1):
    for j in range(i+1, len(cities)):
        p1 = cities[i]
        p2 = cities[j]
        query = '''SELECT distance from places WHERE (place1=%s AND
place2=%s) OR (place1=%s AND place2=%s)'''
        cursor.execute(query, (p1, p2, p2, p1))
        distances = cursor.fetchall()
        for distance in distances:
            print(f"The distance between {p1} and {p2} is {distance[0]} units.")

# Close the cursor and connection
print('data verified')
cursor.close()
conn.close()
