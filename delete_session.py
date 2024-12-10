from connect import connect_database

conn = connect_database()

def delete_workout_session(session_id):
    query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
    cursor.execute(query, session_id)

if conn is not None:
    try:
        cursor = conn.cursor()
        session_id = (3, )

        query_check = "SELECT * FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(query_check, session_id)
        workout_session = cursor.fetchall()

        if workout_session:
            print("That session does not exist.")
        else:
            delete_workout_session(session_id)
            conn.commit()
            print("session has been deleted.")

    except Exception as e:
        print(e)
        
    finally:
        cursor.close()
        conn.close()
