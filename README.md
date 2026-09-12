# MinPro1_004_Firdaus-Ramadhani
Nama     : Firdaus Ramadhani

NIM      : 2609116004

Kelas    : A 

## Mini Project 1 

### Sistem Pelayanan Pengaduan Mahasiswa

Sistem ini merupakan program sederhana yang berfungsi untuk melaporkan masalah yang dialami mahasiswa. Dalam program ini terdapat 2 akun yaitu akun **Mahasiswa** dan **Admin**. **Mahasiswa** dapat melaporkan keluhannya terkait kampus dan keluhan itu dapat dilihat dan diakses dengan akun **Admin**. 

#### Yang ada di dalam program ini

`List` ==> `list` khususnya list kosong digunakan untuk menjadi tempat menyimpan data yang akan diinput oleh user seperti keluhan/pengaduan dan status dari pengaduan tersebut

`Tuple` ==> `tuple` saya gunakan untuk dijadikan isi data status yang tidak bisa di ubah tetapi bisa di munculkan sebagai output

`if-else` ==> `if-else` saya gunakan untuk menentukan pilihan contohnya seperti di program user akan menggunakan akun Mahasiswa atau Admin. Selain itu `if-else` digunakan sebagai validasi jika user menginput pilihan yang tidak tersedia maka output menolak dan kembali ke pilihan sebelumnya (loop) 

`while` ==> `while` adalah dasar dari program ini agar program dapat dijalankan terus-terusan secara berulang sampai user menginginkan berhenti. disini `while` digunakan untuk sistem login, menu mahasiswa, dan menu admin.

`for` ==> `for` digunakan untuk menunjukkan output hasil dari yang telah diinput mahasiswa atau yang telah diubah admin

#### Penjelasan Flowchart dan Outputnya

<img width="2187" height="1769" alt="MINPRO1fix drawio" src="https://github.com/user-attachments/assets/ad819cbb-ea87-4d00-8918-5dfa28aede0f" />

Dimulai dari start kemudian user ditanya ingin login atau keluar, jika keluar program langsung selesai, jika login maka user memasuki laman login.

<img width="346" height="114" alt="OUTPUT START" src="https://github.com/user-attachments/assets/712c75fc-59ad-4faa-afe0-a6473a3d051c" />

##### Role Mahasiswa

Jika login sebagai mahasiswa maka outputnya sebagai berikut.

<img width="344" height="296" alt="LOGIN MAHASISWA" src="https://github.com/user-attachments/assets/2a6fa2f9-b431-4856-b3f4-aeb935e50277" />

dengan role mahasiswa fitur yang bisa diakses hanya **Membuat pengaduan, melihat status pengaduan, dan logout**.

Berikut adalah output ketika mahasiswa membuat pengaduan:

<img width="394" height="580" alt="PENGADUAN MAHASISWA" src="https://github.com/user-attachments/assets/f1dafb7f-5fb6-4027-8b53-2b92131bf5fa" />

Untuk melihat pengaduan yang telah dibuat sekaligus statusnya pilih opsi kedua dan berikut outputnya:

<img width="311" height="348" alt="LIHAT STATUS MAHASISWA" src="https://github.com/user-attachments/assets/3a33998e-42ed-4d20-b97a-9018723d131c" />

Jika user memilih opsi yang tidak tersedia maka:

<img width="333" height="142" alt="PILIHAN TIDAK VALID 2" src="https://github.com/user-attachments/assets/c3570e0a-8352-4800-ba31-1238373e09de" />

Dan ketika mahasiswa logout, Program kembali ke laman login:

<img width="370" height="239" alt="LOGOUT MAHASISWA" src="https://github.com/user-attachments/assets/ee531c71-9f9d-433b-a2a5-9c56b6194e10" />

##### Role Admin

Sebelum lanjut ke role mahasiswa, saya akan menunjukkan bagaimana jadinya jika saat login username atau password salah,:

<img width="412" height="281" alt="LOGIN GAGAL" src="https://github.com/user-attachments/assets/0c0e4bb7-15f9-49b8-b765-73a6e4c344b8" />

user akan diminta memasukkan username dan password lagi hingga benar. disini fungsi dari `while` bekerja.

Jika login sebagai admin maka outputnya sebagai berikut:

<img width="289" height="195" alt="LOGIN ADMIN" src="https://github.com/user-attachments/assets/bfd598e5-5bf4-4190-9c40-32ad831aa7ad" />

Ketika user login sebagai admin fiturnya berbeda dengan mahasiswa. Admin bisa melihat pengaduan, menghapus pengaduan jika sudah selesai, mengubah status pengaduan, dan logout.

Berikut adalah output dari opsi pertama yaitu Lihat Pengaduan:

<img width="320" height="381" alt="LIHAT PENGADUAN AS ADMIN" src="https://github.com/user-attachments/assets/974b3c89-db8c-406b-9682-a7875b456a4b" />

Admin bisa melihat semua pengaduan yang telah dibuat oleh mahasiswa sekaligus status awalnya yang diprogram otomatis seerti itu.

Kemudian admin bisa mengubah status dari pengaduan yang ada di daftar:

<img width="429" height="667" alt="ADMIN UBAH STATUS" src="https://github.com/user-attachments/assets/7c9fccd2-00eb-4b73-8ca8-fa3afc7cb2dd" />

Ini output daftar kekita status telah diubah

<img width="350" height="430" alt="ADMIN UBAH STATUS 2" src="https://github.com/user-attachments/assets/5e28cd72-eeb8-49d5-acb8-823ea9a2bf81" />

Dan admin juga bisa menghapus pengaduan:

<img width="379" height="242" alt="ADMIN HAPUS PENGADUAN " src="https://github.com/user-attachments/assets/9c1a34e3-d87e-4ff6-9196-a5e589bb96a7" />

Berikut output ketika user memasukkan opsi yang tidak tersedai di pilihan:

<img width="467" height="651" alt="PILIHAN TIDAK VALID" src="https://github.com/user-attachments/assets/8a662d9e-506c-49cf-8e10-e5cc6d47d12f" />

Untuk mengakhiri program, dalam role mahasiswa atau admin user cukup logout untuk kembali ke loop awal sebelum sistem login dan memilih opsi keluar:

<img width="368" height="260" alt="LOGOUT ADMIN" src="https://github.com/user-attachments/assets/ce453cd0-b5f1-4ab2-95e8-138b10baf6f4" />

<img width="445" height="136" alt="END" src="https://github.com/user-attachments/assets/a740d57d-757d-4893-a9c4-9433470f96d5" />









