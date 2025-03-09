from holocron_connection import connect_db

def add_jedi(name, age, jedi_rank):
    conn = connect_db()
    cursor = conn.cursor()

    sql = "INSERT INTO Members (name, age, jedu_rank) VALUES (%s, %s, %s)"
    values = (name, age, jedi_rank)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print(F"Jedi Knight {name} has been added to the archives!")
    except Exception as e:
        print("Error adding Jedi:", {e})

        conn.close()
def update_jedi_rank(jedi_id, new_rank):
    conn = connect_db()
    cursor = conn.cursor()

    sql = "UPDATED Members SET jedi_rank = %s WHERE id =%s"
    values =(new_rank, jedi_id)
    cursor.execute(sql, values)
    if cursor.rowcount == 0:
        print("No Jedi found with that ID in the Jedi Archives.")
    else:
        conn.commit()
        print(f"Jedi ID {jedi_id} has ascended to {new_rank}!")

        conn.close()

