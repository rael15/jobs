from django.contrib import admin
from django.urls import path
from emprego import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empregos/', views.lista_empregos),
    # path('', views.lista_empregos),

    path('login/', views.login_user),
    path('empregos/novo_emprego/', views.novo_emprego),
    path('empregos/novo_emprego/submit', views.submit_emprego),
    path('empregos/novo_emprego/delete/<int:id_emprego>/', views.delete_emprego),
    path('login/submit', views.submit_login),
    path('', RedirectView.as_view(url='empregos/')),
    path('logout/', views.logout_user)

]