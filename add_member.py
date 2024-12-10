from connect import connect_database

conn = connect_database()
def add_member(id, name, age):
    query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, age))

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (member_id, date, duration_minutes, calories_burned))

if conn is not None:
    try:
        cursor = conn.cursor()
        add_member(3, "Max", 20)
        add_workout_session(cursor.lastrowid, "12-05-2024", 60, 100)
        
        conn.commit()
        print(f"info has been added.")

    finally:
        cursor.close()
        conn.close()