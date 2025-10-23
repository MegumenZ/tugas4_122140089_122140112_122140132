from google.cloud import storage
import os

# Ganti dengan nama bucket Anda
BUCKET_NAME = "platform-elearning-videos-prod-demo"

# Inisialisasi Klien
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

# --- CREATE (Upload) ---
# Ini untuk mengupload file seperti video, thumbnail, atau assignment [cite: 9, 14]
def upload_file(file_path, destination_blob_name):
    """Uploads a file to the bucket."""
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(file_path)
    print(f"File {file_path} diupload ke {destination_blob_name}.")

# --- READ (Download) ---
def download_file(source_blob_name, destination_file_path):
    """Downloads a blob from the bucket."""
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_path)
    print(f"File {source_blob_name} didownload ke {destination_file_path}.")

# --- DELETE ---
def delete_file(blob_name):
    """Deletes a blob from the bucket."""
    blob = bucket.blob(blob_name)
    blob.delete()
    print(f"File {blob_name} dihapus.")

# --- LIST (Bagian dari Read) ---
def list_files():
    """Lists all the blobs in the bucket."""
    blobs = storage_client.list_blobs(BUCKET_NAME)
    print("Files di bucket:")
    for blob in blobs:
        print(f"- {blob.name}")

# --- Contoh Eksekusi ---
if __name__ == "__main__":
    # Buat file dummy
    DUMMY_FILE = "demo_video.mp4"
    with open(DUMMY_FILE, "w") as f:
        f.write("ini adalah file video demo")

    # Upload
    upload_file(DUMMY_FILE, "courses/101/video_utama.mp4")

    # List
    list_files()

    # Download
    download_file("courses/101/video_utama.mp4", "downloaded_video.mp4")

    # Delete
    delete_file("courses/101/video_utama.mp4")

    # Hapus file lokal
    os.remove(DUMMY_FILE)
    os.remove("downloaded_video.mp4")
