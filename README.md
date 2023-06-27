# FINAL PROJECT DESIGN AND ANALYSIS ALGORITHM
# PERANCANGAN DAN ANALISIS ALGORITMA II
# NAMA  : BUDI AGUNG FAJARIYANTO
# NIM   : F55121064

A.	Bubble sort dan Insertion 

1.	Worst Case (Kasus Terburuk)
Pada kasus terburuk, kita akan melihat seberapa buruk performa kedua algoritma saat list input terurut secara terbalik atau terurut secara menurun. Dalam hal ini, kita akan mengurutkan list sebagai berikut: [99, 97, 95, ..., 3, 2, 1].
•	Bubble Sort
Pada kasus terburuk, bubble sort akan melakukan perbandingan dan penukaran elemen secara berulang untuk setiap pasang elemen, sehingga total jumlah operasi yang dilakukan adalah sekitar (n * n), dengan n adalah jumlah elemen dalam list. Jadi, jika kita memiliki 80 elemen, maka bubble sort akan melakukan sekitar 6.400 operasi perbandingan dan penukaran.
•	Insertion Sort
Pada kasus terburuk, insertion sort juga akan melakukan perbandingan dan penukaran elemen untuk setiap pasang elemen, namun dalam jumlah yang lebih sedikit daripada bubble sort. Total jumlah operasi yang dilakukan oleh insertion sort pada kasus terburuk adalah sekitar (n * n), sehingga jika kita memiliki 100 elemen, insertion sort akan melakukan sekitar 10.000 operasi perbandingan dan penukaran.
2.	Best Case (Kasus Terbaik)
Pada kasus terbaik, kita akan melihat seberapa efisien kedua algoritma saat list input sudah terurut secara membesar. Dalam hal ini, kita akan menggunakan list input yang sama seperti sebelumnya, tetapi kali ini kita akan mengurutkannya secara membesar: [1, 1, 1, ..., 99].
•	Bubble Sort
Pada kasus terbaik, bubble sort akan melakukan perbandingan untuk setiap pasang elemen, namun tidak akan ada penukaran elemen yang dilakukan karena list sudah terurut secara membesar. Jadi, total jumlah operasi yang dilakukan oleh bubble sort pada kasus terbaik adalah sekitar (n * n), tetapi jumlah operasi pertukaran elemen adalah 0.
•	Insertion Sort
Pada kasus terbaik, insertion sort juga akan melakukan perbandingan untuk setiap pasang elemen, dan karena list sudah terurut secara membesar, tidak ada penukaran elemen yang diperlukan. Jumlah operasi perbandingan yang dilakukan oleh insertion sort pada kasus terbaik adalah sekitar (n * n), tetapi jumlah operasi pertukaran elemen adalah 0.
3.	Average Case (Kasus Rata-rata):
Kasus rata-rata dapat bervariasi tergantung pada distribusi data dan algoritma yang digunakan. Untuk kasus ini, kita menggunakan list input yang sama seperti sebelumnya dan mengurutkannya dalam urutan acak.
•	Bubble Sort
Pada kasus rata-rata, bubble sort akan melakukan perbandingan dan penukaran elemen untuk setiap pasang elemen yang tidak terurut secara benar. Total jumlah operasi yang dilakukan oleh bubble sort pada kasus rata-rata adalah sekitar (n * n), dengan jumlah operasi penukaran yang lebih sedikit dibandingkan kasus terburuk.
•	Insertion Sort
Pada kasus rata-rata, insertion sort juga akan melakukan perbandingan dan penukaran elemen untuk setiap pasang elemen yang tidak terurut secara benar. Total jumlah operasi yang dilakukan oleh insertion sort pada kasus rata-rata adalah sekitar (n * n), dengan jumlah operasi penukaran yang lebih sedikit dibandingkan kasus terburuk.

B.	Algoritma TSP (Travelling Salesman Problem) dan Dijkstra 
1.	Worst Case (Kasus Terburuk)
Disini dapat dilihat seberapa buruk performa algoritma TSP dan Dijkstra saat harus melalui semua simpul dan edge dalam graf yang diberikan. Dalam hal ini, graf yang diberikan memiliki 7 simpul (a, b, c, d, e, f, g) dan 23 edge yang menghubungkan simpul-simpul tersebut. Dalam kasus ini, kita harus mencari rute terpendek yang melalui semua simpul dan edge.
•	Algoritma TSP
Pada kasus terburuk, algoritma TSP akan mencoba semua kemungkinan rute yang melalui semua simpul dan edge. Karena jumlah simpul dalam graf ini adalah 7, maka jumlah kemungkinan permutasi adalah 7! (faktorial 7), yaitu sekitar 5040 kemungkinan permutasi. Oleh karena itu, jumlah operasi yang dilakukan oleh algoritma TSP pada kasus terburuk adalah sekitar O(7!).
•	Algoritma Dijkstra
Pada kasus terburuk, algoritma Dijkstra akan mencari rute terpendek dari satu simpul ke semua simpul lainnya. Dalam kasus ini, akan menjalankan algoritma Dijkstra dari setiap simpul dalam graf, sehingga total jumlah operasi yang dilakukan adalah sekitar O(V * E * log(V)), dengan V adalah jumlah simpul (7) dan E adalah jumlah edge (23). Jadi, pada kasus terburuk, algoritma Dijkstra pada graf ini akan melakukan sekitar O(7 * 23 * log(7)) operasi.
2.	Best Case (Kasus Terbaik):
Pada kasus terbaik, kita akan melihat seberapa efisien algoritma TSP dan Dijkstra saat graf memiliki sifat khusus yang memudahkan pencarian jalur terpendek.
•	Algoritma TSP
Pada kasus terbaik, algoritma TSP akan menemukan tur terpendek dengan jumlah simpul yang sedikit. Dalam graf yang diberikan, tidak dapat mengidentifikasi kasus terbaik tertentu karena semua simpul harus dikunjungi, dan tidak ada sifat khusus yang dapat mempercepat pencarian tur terpendek.
•	Algoritma Dijkstra
Pada kasus terbaik, algoritma Dijkstra akan menemukan jalur terpendek antara dua simpul tanpa harus menjelajahi seluruh graf. Dalam graf yang diberikan, tidak dapat mengidentifikasi kasus terbaik tertentu karena setiap simpul harus dihubungkan dengan setiap simpul lainnya, dan tidak ada sifat khusus yang dapat mempercepat pencarian jalur terpendek.
3.	Average Case (Kasus Rata-rata):
Kasus rata-rata dapat bervariasi tergantung pada distribusi data dan algoritma yang digunakan. Untuk kasus ini, kita menggunakan graf yang diberikan dan menghitung rata-rata kinerja algoritma TSP dan Dijkstra berdasarkan jumlah simpul dan edge yang ada.
•	Algoritma TSP
Pada kasus rata-rata, algoritma TSP akan mencoba beberapa kemungkinan permutasi tur yang melalui semua simpul dan edge. Jumlah permutasi yang harus diuji dapat bervariasi tergantung pada urutan simpul yang dikunjungi. Karena jumlah simpul dalam graf ini adalah 7, kompleksitas waktu rata-rata algoritma TSP pada kasus ini adalah sekitar O(7!).
•	Algoritma Dijkstra
Pada kasus rata-rata, algoritma Dijkstra akan mencari jalur terpendek dari satu simpul ke semua simpul lainnya. Dalam kasus ini, kita akan menjalankan algoritma Dijkstra dari setiap simpul dalam graf, sehingga total jumlah operasi yang dilakukan adalah sekitar O(V * E * log(V)), dengan V adalah jumlah simpul (7) dan E adalah jumlah edge (23). Jadi, pada kasus rata-rata, algoritma Dijkstra pada graf ini akan melakukan sekitar O(7 * 23 * log(7)) operasi.


