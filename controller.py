from mysql.connector import connect, Error


connection = None

try:
    connection = connect(
        host="localhost",
        user="root",
        password="",
        database="hotel_reservation",
        port="3308"
    )
    
    cursor = connection.cursor()
    print("Connected to the database!")
    
    
    def checkUser(username, password=None):
        cmd = f"Select count(username) from user where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    
    
    
    def checkUser(username, password=None):
        cmd = f"Select count(username) from user where username='{username}' and BINARY password='{password}'"
        cursor.execute(cmd)
        cmd = None
        a = cursor.fetchone()[0] >= 1
        return a
    
    
      # Add a guest_info
    def add_guest(name, address, number, email):
        try:
            query = "INSERT INTO guest(name, address, number, email) VALUES (%s, %s, %s, %s)"
            values = (name, address, number, email)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def get_guest():
        try:
            cmd = "SELECT id, name, address, number, email FROM guest"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()
            print("data: ", result)

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []  # Return an empty list if there's an error or no results



     # update health
    def update_guest(id,name, address, number, email):
        cmd = f"update guest set name ='{name}',address='{address}', number ='{number}', email ='{email}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True
            
        
            # Delete a activity
    def delete_guest(id):
        cmd = f"delete from guest where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    
          # Add a guest_info
    def add_reservation(guestId, roomNo, typeRoom, checkIn, checkOut):
        try:
            query = "INSERT INTO reservation(guest_id, room_no, type_room, check_in, check_out) VALUES (%s, %s, %s, %s, %s)"
            values = (guestId, roomNo, typeRoom, checkIn, checkOut)
            cursor.execute(query, values)
            connection.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            print(values)
            return False
        
    def get_reservation():
        try:
            cmd = "SELECT id, guest_id, room_no, type_room, check_in, check_out FROM reservation"
            cursor.execute(cmd)

            # Fetch the results
            result = cursor.fetchall()
            print("data: ", result)

            # Return the results
            return result
            
        except Exception as e:
            print(f"Error: {e}")
            return []  
        
      # update health
    def update_reservation(id,guestId, roomNo, typeRoom, checkIn, checkOut):
        cmd = f"update reservation set guest_id ='{guestId}',room_no='{roomNo}', type_room ='{typeRoom}', check_in ='{checkIn}', check_out ='{checkOut}' where id = '{id}';"
        cursor.execute(cmd)
        connection.commit()
        if cursor.rowcount == 0:
            return False
        return True
        
            # Delete a activity
    def delete_guest(id):
        cmd = f"delete from reservation where id='{id}';"
        cursor.execute(cmd)
        connection.commit() 
        if cursor.rowcount == 0:
            return False
        return True
    
except Error as e:
    print(f"Error: {e}")
    