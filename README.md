####·Para poder hacer la traducion de la manera sencilla.

1. Se debe tener en **{% static i18n %}** en base.html
2. Se debe tener en index.html **{% load i18n %}**
3. En la raiz se debe de crear la carpeta **locale**
4. Se crea : $django-admin makemessages -l es  
5. Se tiene que compilar : django-admin compilemessages