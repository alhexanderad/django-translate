####·Para poder hacer la traducion de la manera sencilla.

1. Se debe tener en **{% static i18n %}** en base.html
2. Se debe tener en index.html **{% load i18n %}**
3. En la raiz se debe de crear la carpeta **locale**
4. Se crea : $django-admin makemessages -l es  
5. Se tiene que compilar : django-admin compilemessages

#### Middleware
1. Se ingreso **'django.middleware.locale.LocaleMiddleware',** en settings.py.
2. Se realizo la configuración en core/urls.py 

    ```python
    from django.contrib import admin
    from django.urls import path, include

    from django.conf import settings
    from django.conf.urls.static import static
    from django.conf.urls.i18n import i18n_patterns

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]

    urlpatterns += i18n_patterns(
        path('', include('base.urls')),
    )
    ```
3. El codigo:
    ```python
    urlpatterns += i18n_patterns(
        path('', include('base.urls')),
        prefix_default_language=False,
    )
    ```
    nos ayuda que la pagina se nuestra de manera predetermina al idioma de la configuracion de settings.py