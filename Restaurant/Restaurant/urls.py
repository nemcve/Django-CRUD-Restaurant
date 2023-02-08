"""banka1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menu import views as menu_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_views.home),
    path('', include("django.contrib.auth.urls")),
    path('show', include("django.contrib.auth.urls")),
    path('add', menu_views.addMeal),
    path('show', menu_views.showMenu),
    path('update/<int:id>', menu_views.editMeal, name="update"),
    path('delete/<int:id>', menu_views.deleteMeal, name="delete"),
    path('search', menu_views.searchMenu),
    path('register/', accounts_views.register_request),
    path('login/', accounts_views.login_request),
    path('logout/', accounts_views.logout_user),
    path('profile/', accounts_views.profile),
    path('filter', menu_views.filterMenu),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
