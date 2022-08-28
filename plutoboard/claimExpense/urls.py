from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home', views.index, name = 'home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name ='signup'),
    path('register', views.user_register, name="register" ),
    path('expenseclaim', views.expenseclaim, name="expenseclaim"),
    path('onClickFormExpense', views.onClick_formExpense, name = 'formExpense'),
]