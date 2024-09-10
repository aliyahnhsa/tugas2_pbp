# Tugas 2 PBP
# Aliyah Nahisa Sugiana
# 2306275405
# PBP B

## Tautan Aplikasi PWS
Aplikasi Django saya dapat diakses melalui link berikut:  
[Link Aplikasi PWS masih belum ada karena server down]

## Jawaban Pertanyaan

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step?

Pertama-tama saya buat direktori dan repositori baru yang bernama `tugas2_pbp`, kemudian saya instalasi Django di direktori tersebut dan menginisiasi proyek Django. Setelah itu, saya mencoba untuk melakukan deployment di PWS, tetapi server masih down. Selanjutnya, saya membuat `urls.py`, `views.py`, `models.py`, dan berkas HTML `main.html` untuk halaman web yang kemudian saya rapihkan sesuai kemampuan.

### 2. Bagan request client ke web aplikasi berbasis Django

- Client mengirim request ke server.
- `urls.py` menangkap request dan mencocokkannya dengan pola URL yang ada.
- `views.py` menangani logika request, memproses data dengan menggunakan `models.py` (jika diperlukan), lalu merender template HTML.
- `models.py` berfungsi sebagai ORM yang menghubungkan logika aplikasi dengan database.
- Setelah semua diproses, HTML dikirim kembali sebagai respon ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git berfungsi sebagai sistem kontrol versi yang memungkinkan developer untuk melacak perubahan kode, berkolaborasi dengan tim, serta mengelola berbagai versi dari suatu proyek secara terorganisir. Ini penting dalam menjaga integritas dan riwayat pengembangan.

### 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dipilih karena memiliki struktur yang jelas dan lengkap, sehingga memudahkan pemula untuk memahami cara kerja pengembangan web secara menyeluruh. Django juga memiliki banyak fitur bawaan yang mengurangi kebutuhan untuk menulis kode dari nol.

### 5. Mengapa model pada Django disebut sebagai ORM?

Model di Django disebut ORM (Object-Relational Mapping) karena memungkinkan developer untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL secara langsung. ORM mengonversi data dari database menjadi objek Python dan sebaliknya.