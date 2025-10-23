import redis

# Ganti dengan IP Privat instance Memorystore Anda
REDIS_HOST = "YOUR_MEMORSTORE_PRIVATE_IP"
REDIS_PORT = 6379

try:
    # Inisialisasi Klien
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r.ping()
    print("Berhasil terhubung ke Memorystore (Redis)!")

    # --- CREATE / UPDATE (SET) ---
    # Gunakan untuk cache profil user atau session 
    print("\n--- CREATE / UPDATE ---")
    # Set dengan expiry (3600 detik = 1 jam) - cocok untuk session
    r.setex("session:user123", 3600, "{'username': 'andi', 'role': 'student'}")
    print("Data session:user123 disimpan.")

    # Set data cache kursus
    r.set("course:101:details", "{'title': 'Kuis 1', 'instructor': 'Budi'}")
    print("Data course:101:details disimpan.")


    # --- READ (GET) ---
    print("\n--- READ ---")
    session_data = r.get("session:user123")
    print(f"Membaca session:user123: {session_data}")

    course_data = r.get("course:101:details")
    print(f"Membaca course:101:details: {course_data}")


    # --- DELETE (DEL) ---
    print("\n--- DELETE ---")
    r.delete("course:101:details")
    print("Data course:101:details dihapus.")

    # Cek apakah sudah hilang
    course_data_deleted = r.get("course:101:details")
    print(f"Membaca course:101:details setelah dihapus: {course_data_deleted}")


except Exception as e:
    print(f"Gagal terhubung atau operasi gagal: {e}")
