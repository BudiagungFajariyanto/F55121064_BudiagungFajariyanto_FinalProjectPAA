# FINAL PROJECT DESIGN AND ANALYSIS ALGORITHM
# PERANCANGAN DAN ANALISIS ALGORITMA II
# NAMA  : BUDI AGUNG FAJARIYANTO
# NIM   : F55121064

=========================================================================

# A.	Bubble sort dan Insertion 

# 1.	Worst Case (Kasus Terburuk)

Pada kasus terburuk, kita akan melihat seberapa buruk performa kedua algoritma saat list input terurut secara terbalik atau terurut secara menurun. Dalam hal ini, kita akan mengurutkan list sebagai berikut: [99, 97, 95, ..., 3, 2, 1].

• Bubble Sort 

Pada kasus terburuk, bubble sort akan melakukan perbandingan dan penukaran elemen secara berulang untuk setiap pasang elemen, sehingga total jumlah operasi yang dilakukan adalah sekitar (n * n), dengan n adalah jumlah elemen dalam list. Jadi, jika kita memiliki 80 elemen, maka bubble sort akan melakukan sekitar 6.400 operasi perbandingan dan penukaran.

• Insertion Sort

Pada kasus terburuk, insertion sort juga akan melakukan perbandingan dan penukaran elemen untuk setiap pasang elemen, namun dalam jumlah yang lebih sedikit daripada bubble sort. Total jumlah operasi yang dilakukan oleh insertion sort pada kasus terburuk adalah sekitar (n * n), sehingga jika kita memiliki 100 elemen, insertion sort akan melakukan sekitar 10.000 operasi perbandingan dan penukaran.

# 2.	Best Case (Kasus Terbaik)
   
Pada kasus terbaik, kita akan melihat seberapa efisien kedua algoritma saat list input sudah terurut secara membesar. Dalam hal ini, kita akan menggunakan list input yang sama seperti sebelumnya, tetapi kali ini kita akan mengurutkannya secara membesar: [1, 1, 1, ..., 99].

•	Bubble Sort

Pada kasus terbaik, bubble sort akan melakukan perbandingan untuk setiap pasang elemen, namun tidak akan ada penukaran elemen yang dilakukan karena list sudah terurut secara membesar. Jadi, total jumlah operasi yang dilakukan oleh bubble sort pada kasus terbaik adalah sekitar (n * n), tetapi jumlah operasi pertukaran elemen adalah 0.

•	Insertion Sort

Pada kasus terbaik, insertion sort juga akan melakukan perbandingan untuk setiap pasang elemen, dan karena list sudah terurut secara membesar, tidak ada penukaran elemen yang diperlukan. Jumlah operasi perbandingan yang dilakukan oleh insertion sort pada kasus terbaik adalah sekitar (n * n), tetapi jumlah operasi pertukaran elemen adalah 0.

# 3.	Average Case (Kasus Rata-rata):
   
Kasus rata-rata dapat bervariasi tergantung pada distribusi data dan algoritma yang digunakan. Untuk kasus ini, kita menggunakan list input yang sama seperti sebelumnya dan mengurutkannya dalam urutan acak.

•	Bubble Sort

Pada kasus rata-rata, bubble sort akan melakukan perbandingan dan penukaran elemen untuk setiap pasang elemen yang tidak terurut secara benar. Total jumlah operasi yang dilakukan oleh bubble sort pada kasus rata-rata adalah sekitar (n * n), dengan jumlah operasi penukaran yang lebih sedikit dibandingkan kasus terburuk.

•	Insertion Sort

Pada kasus rata-rata, insertion sort juga akan melakukan perbandingan dan penukaran elemen untuk setiap pasang elemen yang tidak terurut secara benar. Total jumlah operasi yang dilakukan oleh insertion sort pada kasus rata-rata adalah sekitar (n * n), dengan jumlah operasi penukaran yang lebih sedikit dibandingkan kasus terburuk.

=========================================================================

# B.	Algoritma TSP (Travelling Salesman Problem) dan Dijkstra 

# 1.	Worst Case (Kasus Terburuk)
   
Disini dapat dilihat seberapa buruk performa algoritma TSP dan Dijkstra saat harus melalui semua simpul dan edge dalam graf yang diberikan. Dalam hal ini, graf yang diberikan memiliki 7 simpul (a, b, c, d, e, f, g) dan 23 edge yang menghubungkan simpul-simpul tersebut. Dalam kasus ini, kita harus mencari rute terpendek yang melalui semua simpul dan edge.

•	Algoritma TSP

Worst case untuk TSP adalah ketika jumlah simpul (nodes) yang ada dalam graf sangat besar. Dalam kasus ini, TSP memiliki kompleksitas waktu yang tinggi, sehingga mencari solusi optimal dapat menjadi sangat lambat dan mahal secara komputasional. Dalam contoh yang diberikan, terdapat 7 simpul (a, b, c, d, e, f, g), sehingga kompleksitas waktu TSP dapat menjadi eksponensial tergantung pada implementasinya.

•	Algoritma Dijkstra

Worst case untuk algoritma Dijkstra adalah ketika setiap simpul terhubung dengan semua simpul lainnya. Dalam hal ini, kompleksitas waktu Dijkstra adalah O(V^2), di mana V adalah jumlah simpul dalam graf. Dalam contoh yang diberikan, terdapat 7 simpul, sehingga kompleksitas waktu Dijkstra adalah O(7^2) = O(49).

# 2.	Best Case (Kasus Terbaik):
   
Pada kasus terbaik, kita akan melihat seberapa efisien algoritma TSP dan Dijkstra saat graf memiliki sifat khusus yang memudahkan pencarian jalur terpendek.

•	Algoritma TSP

Best case untuk TSP adalah ketika solusi optimal dapat ditemukan dengan cepat. Namun, TSP secara umum merupakan permasalahan NP-complete, yang berarti tidak ada algoritma efisien yang dapat menyelesaikan semua kasus dengan kompleksitas waktu konstan. Oleh karena itu, tidak ada "best case" yang pasti dalam konteks TSP.

•	Algoritma Dijkstra

Best case untuk algoritma Dijkstra adalah ketika simpul tujuan (destination node) terletak dekat dengan simpul asal (source node) dan tidak ada simpul yang perlu dikunjungi di antara keduanya. Dalam kasus ini, algoritma Dijkstra dapat menemukan jalur terpendek dengan cepat dan kompleksitas waktu yang rendah. Namun, dalam contoh yang diberikan, harus ada informasi spesifik mengenai simpul asal dan tujuan, sehingga dapat diketahui secara pasti best case-nya.

# 3.	Average Case (Kasus Rata-rata):
   
Kasus rata-rata dapat bervariasi tergantung pada distribusi data dan algoritma yang digunakan. Untuk kasus ini, kita menggunakan graf yang diberikan dan menghitung rata-rata kinerja algoritma TSP dan Dijkstra berdasarkan jumlah simpul dan edge yang ada.

•	Algoritma TSP

Average case untuk TSP dan Dijkstra dapat bervariasi tergantung pada struktur dan ukuran graf yang digunakan. Pada umumnya, kompleksitas waktu TSP cenderung tinggi karena mencari solusi optimal melibatkan pengujian semua kemungkinan kombinasi jalur, yang membuatnya lebih lambat saat jumlah simpul meningkat. Dalam hal ini, dengan 7 simpul, kompleksitas waktu TSP masih dapat dikendalikan.

•	Algoritma Dijkstra

Average case untuk Dijkstra tergantung pada jumlah simpul dan jumlah tepi (edges) dalam graf, serta distribusi bobot tepi. Dalam contoh yang diberikan, kompleksitas waktu Dijkstra akan bergantung pada jumlah simpul dan bobot tepi yang spesifik. Dalam hal ini, dengan 7 simpul dan 23 tepi, kompleksitas waktu Dijkstra tidak terlalu tinggi.

=========================================================================
