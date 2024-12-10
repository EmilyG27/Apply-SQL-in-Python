from connect import connect_database

conn = connect_database()
def update_member_age(member_id, new_age):
    query = "UPDATE Members SET age = %s WHERE id = %s"
    cursor.execute(query, (member_id, new_age))

if conn is not None:
    try:
        cursor = conn.cursor()
        member_id = (3, )
        query_check = "SELECT * FROM Members WHERE id = %s"
        cursor.execute(query_check, member_id)
        member_check = cursor.fetchall()

        if member_check:
            print("That member does not exist.")
        else:
            update_member_age(28, 3)
            conn.commit()
            print("info has been updated.")
    finally:
        cursor.close()
        conn.close()