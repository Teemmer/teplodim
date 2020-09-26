SECRET_KEY = '<YOUR_KEY>'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.<ENGINE>',
        'NAME': '<DB_NAME>',
        'USER': '<DB_USER>',
        'PASSWORD': '<DB_PASS>',
        'HOST': '<DB_HOST>',
        'PORT': '<DB_PORT>',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = '<EMAIL_HOST>'
EMAIL_HOST_PASSWORD = '<EMAIL_PASS>'
