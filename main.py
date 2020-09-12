#import bs4 = bautifulSoup ==> hanya berfungsi sebagai parsing, memecah string menjadi bagian2 kecil/elemen
#import requests = untuk menembus url
import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=233' #variabel berisi url target
content = requests.get(url) #variabel yg memanfaatkan package request untuk mengambil 'url'

response = bs4.BeautifulSoup(content.text, 'html.parser') #variabel yang memanfaatkan bs4 untuk mengambil isi variabel content, html.parser untuk menerjemahkan html ke teks biasa

#menggunakan fungsi dari bs4 = .find_all, memfilter tag tertentu dari var response
#kenapa kok tag 'table_highlight', karena pada jadwal sholat hari ini menggunakan tag tersebut dan itu target kita.
data = response.find_all('tr', 'table_highlight')
data = data[0] #mengambil data array dari tag 'table_highlight'=>berisi 5 waktu sholat, ada 5 data

sholat = {} #membuat dict kosong, nantinya akan menampung data dari proses perulangan
i = 0

#perulangan: mendapatkan 5 data dalam bentuk teks dan memasukkannya kedalam sholat{}
for d in data:
    i = i + 1
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()


print(sholat)

