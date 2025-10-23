import psycopg2
import os

# Ganti dengan IP Publik, user, pass, dan nama DB Anda
DB_HOST = "YOUR_CLOUDSQL_PUBLIC_IP"
DB_USER = "postgres"
DB_PASSWORD = "YOUR_POSTGRES_PASSWORD"
DB_NAME = "elearning_db"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# --- CREATE (Insert) ---
def create_quiz(course_id, title):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO quizzes (course_id, title) VALUES (%s, %s) RETURNING quiz_id",
                (course_id, title))
    quiz_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    print(f"Quiz baru dibuat dengan ID: {quiz_id}")
    return quiz_id

# --- READ (Select) ---
def get_quiz(quiz_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM quizzes WHERE quiz_id = %s", (quiz_id,))
    quiz = cur.fetchone()
    cur.close()
    conn.close()
    print(f"Data Quiz: {quiz}")
    return quiz

# --- UPDATE ---
def update_quiz_title(quiz_id, new_title):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE quizzes SET title = %s WHERE quiz_id = %s",
                (new_title, quiz_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Quiz ID {quiz_id} diupdate.")

# --- DELETE ---
def delete_quiz(quiz_id):
    conn = get_db_connection()
    cur = conn.cursor()
    # Hapus dulu data terkait (jika ada)
    cur.execute("DELETE FROM quiz_attempts WHERE quiz_id = %s", (quiz_id,))
    # Hapus quiz utama
    cur.execute("DELETE FROM quizzes WHERE quiz_id = %s", (quiz_id,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Quiz ID {quiz_id} dan attempt terkait dihapus.")


# --- Contoh Eksekusi ---
if __name__ == "__main__":
    # Create
    new_id = create_quiz(102, "Kuis 2: Pengenalan Cloud SQL")

    # Read
    get_quiz(new_id)

    # Update
    update_quiz_title(new_id, "Kuis 2: Update Judul")

    # Read Lagi
    get_quiz(new_id)

    # Delete
    delete_quiz(new_id)
