# Aliyah Nahisa Sugiana | 2306275405 | PBP B

## TUGAS INDIVIDU 2:

### Tautan Aplikasi PWS
Aplikasi Django saya dapat diakses melalui link berikut:  
[Link Aplikasi PWS masih belum ada karena server down]

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



## TUGAS INDIVIDU 3:

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah cara kita memastikan aplikasi tetap sinkron dengan server, terutama untuk aplikasi yang interaktif. Tanpa data delivery, semua data di halaman aplikasi akan statis dan tidak bisa memperbarui informasi sesuai kebutuhan pengguna. Data delivery membuat semuanya terasa nyata dan langsung—ketika pengguna menambah barang di keranjang belanja, contohnya, itu harus langsung diproses dan dikirim ke server, bukan hanya sekadar aksi visual.

### 2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Secara pribadi, saya lebih memilih JSON. XML terasa terlalu berat dan cenderung ribet. Sedangkan JSON, lebih simpel dan to the point, cocok untuk pengiriman data yang cepat dan ringan. Alasan utamanya JSON lebih populer karena lebih sedikit syntax dan lebih mudah dibaca, baik oleh manusia maupun mesin. XML mungkin punya tempat di beberapa aplikasi yang sangat spesifik, tapi dalam pengembangan modern, JSON lebih bagus dalam hal kepraktisan.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` pada form Django itu penting untuk ngecek apakah input dari pengguna sesuai aturan yang sudah kita tentukan di form atau model. Tanpa itu, kita bisa aja dapat input yang asal-asalan, misalnya harga produk yang berupa teks atau field kosong yang seharusnya wajib diisi. Kita butuh ini supaya form bisa memfilter data yang tidak valid sebelum masuk ke database atau diproses lebih lanjut.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita butuh `csrf_token` karena itu cara paling gampang Django untuk memastikan bahwa data yang dikirimkan oleh pengguna benar-benar datang dari form di website kita, bukan dari sumber luar yang berbahaya. Kalau kita nggak pakai `csrf_token`, form kita bisa dipakai penyerang untuk mengirimkan permintaan yang tidak kita inginkan atas nama pengguna yang sedang aktif di situs kita—misalnya transaksi ilegal atau mengubah data penting.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Saya mulai dengan bikin direktori proyek dan setup Django. Setelah itu, deployment ke PWS, tapi sempat terhenti karena server down. Lanjut, saya buat model yang sesuai dengan kebutuhan aplikasi (nama, harga, deskripsi). Setelah itu, saya setup views dan URLs untuk menampilkan data di frontend. Terakhir, saya rapikan template HTML dan pastikan semuanya bisa bekerja dengan baik secara fungsional dan visual.

### POSTMAN
![image](https://github.com/user-attachments/assets/613ae02f-68fe-4cb9-a1a6-8a87ef20f1ab)
![image](https://github.com/user-attachments/assets/4778dfd7-ed97-4e21-bfb6-2ea4ac05ec5d)
![image](https://github.com/user-attachments/assets/9e55582b-fd77-444f-9d4b-821463b01e46)
![image](https://github.com/user-attachments/assets/e8b469de-79a1-458c-8c97-66f0a76a3ae1)


## TUGAS INDIVIDU 4:

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
   - `HttpResponseRedirect()` adalah kelas bawaan Django yang mengembalikan respon HTTP yang mengarahkan ulang ke URL tertentu. Ini membutuhkan argumen berupa URL sebagai string.
   
   - `redirect()` adalah shortcut bawaan Django yang memudahkan proses pengalihan. `redirect()` dapat menerima URL sebagai string, nama tampilan (view), atau bahkan model object yang memiliki method `get_absolute_url()`. Ini lebih fleksibel dibandingkan `HttpResponseRedirect()` karena bisa otomatis mengonversi berbagai tipe argumen menjadi URL.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model `Product` dengan `User`, biasanya digunakan ForeignKey. Misalnya, model `Product` mungkin memiliki atribut `owner` yang mengacu pada model `User`, yang berarti setiap produk dikaitkan dengan pengguna tertentu. Setiap `Product` memiliki `owner` yang merupakan pengguna yang membuat atau memiliki produk tersebut. Berarti jika pengguna dihapus, semua produk yang dimiliki oleh pengguna tersebut juga akan dihapus.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
   - **Authentication** adalah proses memverifikasi identitas pengguna, memastikan bahwa pengguna adalah siapa yang mereka klaim. Dalam Django, proses ini dilakukan saat pengguna memasukkan username dan password. Jika informasi tersebut cocok dengan yang ada di database, pengguna dianggap **terotentikasi**.

   - **Authorization** adalah proses memeriksa hak akses pengguna terhadap sumber daya tertentu. Setelah pengguna terotentikasi, Django akan memeriksa apakah pengguna tersebut memiliki izin (permission) untuk melakukan tindakan tertentu atau mengakses halaman tertentu.
   
   Saat pengguna login, Django melakukan **authentication** dengan mencocokkan kredensial pengguna. Jika berhasil, session akan dibuat untuk mengingat pengguna. Django juga memeriksa izin pengguna (authorization) saat mereka mencoba mengakses fitur tertentu.

   **Implementasi di Django**:
   - Django menyediakan `User` model dan `authenticate()` function untuk proses autentikasi.
   - Django juga memiliki framework permission untuk menangani otorisasi. 

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang login melalui **session** yang disimpan di cookies. Saat pengguna berhasil login, Django membuat session ID yang unik dan mengirimkannya sebagai cookie ke browser pengguna. Pada setiap request selanjutnya, session ID tersebut dikirim kembali ke server untuk mengidentifikasi pengguna yang sedang login.

   **Cookies** digunakan untuk berbagai hal, termasuk:
   - Menyimpan preferensi pengguna (misalnya tema atau pengaturan bahasa).
   - Menyimpan data keranjang belanja di aplikasi e-commerce.
   - Melacak perilaku pengguna untuk analisis atau iklan.

   **Keamanan cookies**:
   Tidak semua cookies aman digunakan. Cookie bisa saja rentan terhadap serangan seperti session hijacking atau cross-site scripting (XSS). Oleh karena itu, Django menyediakan fitur keamanan seperti:
   - `HttpOnly`: Cookie hanya dapat diakses melalui HTTP, tidak dapat diakses oleh JavaScript.
   - `Secure`: Cookie hanya akan dikirim melalui koneksi HTTPS.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk mengimplementasikan sistem login, register, logout, autentikasi, dan penghubungan model secara bertahap tanpa hanya sekadar mengikuti tutorial, saya

1. Membuat fungsi registrasi: Saya memulai dengan menambahkan form pendaftaran menggunakan UserCreationForm. Setelah form di-submit dan validasi berhasil, saya menggunakan form.save() untuk menyimpan data pengguna baru ke database, serta menampilkan pesan sukses menggunakan messages dan redirect ke halaman login. Saya juga memastikan template HTML untuk form registrasi dirancang dengan baik.

2. Membuat fungsi login: Saya menambahkan autentikasi pengguna dengan menggunakan AuthenticationForm. Saat pengguna memasukkan kredensial, saya memvalidasi form dan, jika sukses, melakukan login dengan login(request, user), yang menciptakan sesi untuk pengguna tersebut. Setelah login, pengguna akan diarahkan ke halaman utama.

3. Membuat fungsi logout: Saya mengimpor fungsi logout dan menambahkan mekanisme logout untuk menghapus sesi yang sedang aktif, kemudian redirect ke halaman login.

4. Menggunakan cookies: Saya menambahkan cookie last_login ketika pengguna berhasil login, yang menyimpan waktu terakhir login. Cookie ini kemudian ditampilkan di halaman utama.

5. Menghubungkan model dengan pengguna: Saya menambahkan relasi ForeignKey antara model MoodEntry dan model User. Ketika pengguna membuat mood entry, saya memastikan data yang disimpan dikaitkan dengan akun pengguna yang sedang login, dan hanya menampilkan mood entry yang sesuai dengan pengguna tersebut di halaman utama.

6. Migrasi model: Setelah menghubungkan model dengan User, saya menjalankan migrasi untuk memperbarui struktur database, memastikan data lama ditetapkan ke pengguna yang ada, jika ada entri sebelumnya di database.