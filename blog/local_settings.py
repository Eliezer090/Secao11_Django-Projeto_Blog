DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_django',
        'HOST': '192.168.64.2',
        'USER': 'eliezer2',
        'PASSWORD': '123456',
        'PORT': '3306',
    }
}

SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = None
SESSION_COOKIE_SECURE = None
CSRF_COOKIE_SECURE = None