import os
from pathlib import Path

# Mendefinisikan lokasi utama folder proyekmu
BASE_DIR = Path(__file__).resolve().parent

# Kunci rahasia untuk keamanan (wajib ada di Django)
SECRET_KEY = 'django-insecure-kunci-rahasia-clean-dong-laundry'

# Mode Debug dinyalakan agar kita bisa melihat error jika ada masalah
DEBUG = True

ALLOWED_HOSTS = ['*']

# ==========================================
# 1. APLIKASI YANG TERDAFTAR (Syarat 3i & 3j)
# ==========================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'laundry_app', # <--- Aplikasi buatanmu terdaftar di sini
]

# ==========================================
# 2. MESIN PENGHUBUNG (Middleware)
# ==========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Mengarahkan rute utama ke file urls.py milikmu
ROOT_URLCONF = 'urls'

# ==========================================
# 3. PENGATURAN TAMPILAN (Templates - Syarat 3c)
# ==========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'laundry_app/templates')], # Lokasi file HTML
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ==========================================
# 4. BASIS DATA (Database SQLite - Syarat 3k)
# ==========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==========================================
# 5. FILE STATIS (CSS & JS - Syarat 3b)
# ==========================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'laundry_app/static')
]

# Pengaturan default tipe data (Syarat 3d)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'