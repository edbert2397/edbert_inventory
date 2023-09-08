[link adaptable]()
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

Kemudian saya membuat app baru bernama main dengan cara `python manage.py createapp main`. Applikasi dalam bentuk folder baru dengan nama `APP`. Setelah membuat aplikasi, saya mendaftarkannya pada `settings.py` yang terletak di folder `INVENTORY`. Tambahkan `main` pada `INSTALLED_APPS` sehingaa berbentuk seperti
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
