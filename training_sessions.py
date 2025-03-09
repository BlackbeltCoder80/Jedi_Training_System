# This is where Im handling all the Jedi training sessions. 
# The modules are the best and most useful thing I've learned. I may use them more than others but 
# I suggest newbies like me to do it because it easier to understadn whats happending. 
#Notes Are key to all the coding I may have done to many notes and slowded me down a lot but it was worth it.
from holocron_connection import connect_db
from datetime import date

# Defining training sessions 
def add_training_session(jedi_id, session_time, activity, duration_minutes, force_ability): # Differnt trianing session allowed for jedis of all ranks.
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
        INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity, duration_minutes, force_power_used)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    session_date = date.today().strftime('%Y-%m-%d')
    values = (jedi_id, session_date, session_time, activity, duration_minutes, force_ability)
#The try coding still gets me I copy paste it mostly when it look similar to other programs.
    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"Training session for Jedi ID {jedi_id} recorded successfully in the Jedi Archives!")
    except Exception as e: # the fast way to know you have an error but identifying the error long term would be better in a larger program.
        print("Error logging training session:", e)

    conn.close()

def remove_training_session(session_id):
    conn = connect_db()
    cursor = conn.cursor()

    sql = "DELETE FROM WorkoutSessions WHERE session_id = %s"
    values = (session_id,)

    cursor.execute(sql, values)
    if cursor.rowcount == 0:
        print("No training session found with that ID in the Jedi Archives.")
    else:
        conn.commit()
        print(f"Training session {session_id} has been erased from the Jedi Archives.")

    conn.close()