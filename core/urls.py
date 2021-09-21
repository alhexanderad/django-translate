from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path (_('admin/'), admin.site.urls),
    path('', include('base.urls')),
    path(_('cars/'), include('cars.urls')),
    prefix_default_language=False,
)