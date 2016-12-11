from django.conf.urls import url
from django.contrib import admin

from .models import CacheAdmin
from . import views

# Register your models here.


class CacheDashboardAdmin(admin.ModelAdmin):
    """
    @brief      Cache Dashboard
    """

    def get_urls(self):
        """
        @brief      Gets the urls.
        @return     The urls.
        """

        urls = super(CacheDashboardAdmin, self).get_urls()
        urlpatterns = [
            url(r'^$', self.admin_site.admin_view(views.dashboard),
                name='dashboard'),
            url(r'^add/', views.add, name='add'),
            url(r'^keys/(?P<key_name>.*)/$', views.update, name='update'),
        ]
        return urlpatterns + urls


admin.site.register(CacheAdmin, CacheDashboardAdmin)
