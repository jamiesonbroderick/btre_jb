# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ubsq#xai!qa_!djygyuu76gjn)lxtl*x48$fi0v-l^k%0z1^bn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['34.222.52.170']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'dixieann',
        'HOST': 'localhost'
    }
}