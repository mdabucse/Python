import mysql.connector

#CONNECT TO DATABASE
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="presidio"
    )


# CREATE (Insert message)
def save_message(room, username, message):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO messages (room, username, message)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (room, username, message))
    conn.commit()

    cursor.close()
    conn.close()


#READ (Get messages by room)
def get_messages(room):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT id, username, message
    FROM messages
    WHERE room = %s
    ORDER BY id ASC
    """

    cursor.execute(query, (room,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results


# UPDATE (Edit message)
def update_message(message_id, new_message):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE messages
    SET message = %s
    WHERE id = %s
    """

    cursor.execute(query, (new_message, message_id))
    conn.commit()

    cursor.close()
    conn.close()


# DELETE (Delete message)
def delete_message(message_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM messages
    WHERE id = %s
    """

    cursor.execute(query, (message_id,))
    conn.commit()

    cursor.close()
    conn.close()