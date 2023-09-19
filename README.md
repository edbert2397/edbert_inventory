[link adaptable](https://edbertinventory.adaptable.app/main/)
# Cara Implementasi
## Setup Library yang dibutuhkan
Pertama-tama, membuat file `requirements.txt` yang berisi
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Kita ingin mendownload hal-hal dalam requirements.txt tersebut dalam virtual environment.
Installasi saya lakukan dalam windows powershell dengan cara:

```sh
python -m venv env # Buat virtual env
./venv/Scripts/activate # pada windows atau
pip install -r requirements.txt
```

## 1. Membuat sebuah proyek Django baru

Saya membuat project baru dengan nama `INVENTORY` dengan cara `django-admin createproject INVENTORY`, akan membuat direktori baru dengan nama `INVENTORY`. Direktori akan berisi `manage.py` dan folder `INVENTORY` yang berisi terkait setting dan routing dari proyek. `manage.py` adalah script python yang akan kita gunakan untuk memantain dan mengatur proyek kita. `python manage.py runserver` adalah command untuk menjalankan proyek kita.

## 2. Membuat aplikasi dengan nama main

Kemudian saya membuat app baru bernama main dengan cara `python manage.py createapp main`. Applikasi dalam bentuk folder baru dengan nama `main`. Setelah membuat aplikasi, saya mendaftarkannya pada `settings.py` yang terletak di folder `INVENTORY`. Tambahkan `main` pada `INSTALLED_APPS` sehingaa berbentuk seperti
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]
```
## 3. Melakukan routing proyek agar dapat menjalankan aplikasi
Konfigurasi link `main` pada proyek dengan cara menambahkan `path('main/', include('main.urls'))` pada `urls.py` yang terletak di direktori `INVENTORY`. `urls.py` pada `INVENTORY` nantinya akan terlihat seperti ini:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls'))
]

```
Kemudian buat `urls.py` pada folder `main` dengan kode seperti ini:
```python
from django.urls import path
from . import views

urlpatterns = [
	path('',show_main,name = 'show_main'),
]
```
Dengan begini ketika kita menuju `http://localhost:8000/main` pada browser, kita akan dihadapkan dengan apa yang direturn fungsi `show_main` pada `views.py` 

## 4.Membuat fungsi render pada views.py dan membuat main.html dalam folder templates

buat direktori `templates` pada `main` dan buat file html yang akan dirender dengan nama `main.html`. 
`main.html` yang saya buat sebagai berikut

```python
<h1>{{name_app}}</h1>
<h5>Name: </h5>
<p>{{name}}</p>
<h5>Class: </h5>
<p>{{class}}</p>
```
pada `views.py` kita dapat membuat fungsi untuk mengembalikan `main.html` dengan cara

```python
from django.shortcuts import render

def show_main(request):
    context={
        'name_app' : 'inventory',
        'name' : 'Edbert',
        'class' : 'PBP D'
    }
    return render(request,"main.html",context)
```

variabel `name_app`, `name`, `class` pada main.html didapat dari context saat fungsi `show_main` memanggil main.html 

## 5. Membuat model sebagai Database
Model adalah penghubung python dengan database kita. membuat model dalam file `models.py` pada aplikasi `main` dengan nama `Item`
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length = 255)
    amount = models.IntegerField()
    description = models.TextField()
```

## 6. Melakukan deployment ke Adaptable

## Bagan Aplikasi berbasis django
<img src=bagan.jpg width = 500 height=300/>

## Mengapa virtual environment

Virtual environment digunakan dalam pengembangan software untuk mengisolasi dan mengelola dependensi proyek secara efisien. Hal ini membantu dalam mencegah konflik dependensi, memastikan kompatibilitas dengan versi Python yang benar. Saat mengembangkan aplikasi web berbasis Django atau proyek software lainnya, sangat disarankan untuk selalu menggunakan virtual environment agar dapat menjalankan proyek dengan lebih lancar dan menghindari masalah yang mungkin timbul akibat konflik dependensi dan versi.

kita masih dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi ini tidak disarankan dan dapat mengakibatkan sejumlah masalah. Tanpa virtual environment, proyek Django menggunakan lingkungan Python dan dependensi sistem secara global. Ini dapat menyebabkan konflik dependensi, karena proyek mungkin memerlukan versi paket yang berbeda dengan proyek lain.

# Apa itu MVC, MVT, MVVM
1. **MVC** (Model View Controller) adalah pattern desain framework yang memisahkan applikasi menjadi 3 komponen, yaitu model, view, dan controller. MVC adalah komponen yang sering digunakan industri untuk membuat applikasi yang scalable dan extensible.
<img src=https://miro.medium.com/v2/resize:fit:1400/1*hTlpGXMh9EFefBIT9NrTDQ.png width=500 height=250/>

2. **MVT** (Model View Template) adalah pattern desain yang mirip dengan MVC. Perbedaannya adalah controller diimplementasikan oleh framework sendiri sehingga kita hanya perlu membuat template. Memungkinkan untuk pengembangan yang lebih scalable, cepat, namun terdapat ketergantungan terhadap framework yang digunakan.
<img src=https://miro.medium.com/v2/resize:fit:1400/0*8ZFh-CsrMi7bQG0O.jpg width=500 height=250/>

3. **MVVM** (Model View ViewModel) adalah pattern desain yang fokus pada membedakan user interface (UI) dengan logic dari applikasi kita. Controller pada MVVM berada pada ViewModel. Memungkinkan untuk pemisahan kerja yang lebih baik antara UI dan logic sesuai dengan kelebihan pengembang. ViewModel dapat terlihat sangat kompleks dan susah didebug jika sudah terdapat banyak logic dan binding. 
<img src=https://media.geeksforgeeks.org/wp-content/uploads/20201002215007/MVVMSchema.png width=500 height=250/>

--------------------

# Perbedaan antara POST dan GET pada Django?

POST: Menggunakan metode HTTP POST. Data form dikirim dalam badan permintaan HTTP, yang biasanya tidak terlihat oleh pengguna.POST Lebih aman daripada GET karena data dikirimkan secara tersembunyi dalam badan permintaan HTTP. Ini cocok untuk mengirim data yang sensitif, seperti kata sandi atau informasi pribadi.
GET: Menggunakan metode HTTP GET. Data form disertakan dalam URL sebagai parameter query string, yang terlihat oleh pengguna. GET juga Kurang aman karena data form terlihat dalam URL, sehingga dapat dengan mudah diakses oleh siapa saja yang melihat URL. 

# Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

1.XML (eXtensible Markup Language): XML adalah bahasa markup yang digunakan untuk menggambarkan data dalam bentuk dokumen berhierarki. Sistem XML mirip seperti tree yang memiliki 1 root.
2.JSON (JavaScript Object Notation): data nya disimpan dalam bentuk key-value seperti dictionary dalam python. JSON seringkali digunakan dalam pengiriman data antar web API.
3.HTML (Hypertext Markup Language): HTML adalah bahasa markup khusus yang digunakan untuk membuat halaman web dengan tujuan utamanya adalah mengatur tampilan dan konten halaman web dan tidak efisien untuk menstrafer data secara murni.

# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena kesederhanaan, keringanan, dan kompatibilitasnya. JSON yang berbentuk key-value sperti dictionary tersebut juga cukup human readable. 

# Cara Implementasi

## Membuat Form (`forms.py`)

`APP/forms.py` akan mengimplementasikan library `django.forms` yang akan mempermudah pembuatan form kita karena seluruh html sudah dihandle oleh library form tersebut. Contoh isi `APP/forms.py` adalah.
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name","amount","description"]
```
dimana `name`, `amount`, dan `description` adalah field yang ada pada model `Item` yang sudah didefinisikan.

## Merender form yang dibuat

Untuk merender form yang sudah kita buat, kita dapat menggunakan kemudahan library django. Pada `create_item.html`, kita tinggal menulis code sebagai berikut

```html
<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>
```
`csrf_token` token wajib didefinisikan setiap definisi form, hal ini terkait dengan keamanan. `form.as_table` akan merender form secara keseluruhan kecuali button submit yang perlu kita tulis sendiri.

## Menambahkan masing-masing function pada views.py untuk serializer json dan xml

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml",data),content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type = "application/json")

def show_xml_by_id(request,id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml",data),content_type = "application/xml")

def show_json_by_id(request,id):
    data = Item.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json",data),content_type = "application/json")
```

## Menambahkan routing pada dalam urls.py

```python
from django.urls import path
from main.views import show_main,create_item,show_xml,show_json,show_xml_by_id,show_json_by_id
app_name = 'main'

urlpatterns=[
    path('',show_main,name = 'show_main'),
    path('create-item',create_item,name = 'create_item'),
    path('xml/',show_xml,name = 'show_xml'),
    path('json/',show_json,name='show_json'),
    path('xml/<int:id>/',show_xml_by_id,name="show_xml_by_id"),
    path('json/<int:id>/',show_json_by_id,name = "show_json_by_id"),
]
```
`<int:id>` merupakan contoh dynamic routing yang mana nilai `id` berupa sebuah angka

## SS hasil Postman

1.HTML
<img src = "html.png" width = 400 height = 400/>

2.JSON
<img src = "json.png"/>

3.XML
<img src = "xml.png"/>

4.JSON (by id)
<img src = "json1.png"/>

5.XML (by id)
<img src = "xml1.png"/>



