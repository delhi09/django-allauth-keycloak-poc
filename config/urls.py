from django.contrib import admin
from django.urls import path, include
from allauth.account.decorators import secure_admin_login


admin.autodiscover()
admin.site.login = secure_admin_login(admin.site.login)

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("app/", include("app.urls")),
]
urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
