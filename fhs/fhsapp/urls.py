from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('checklogin',views.checklogin,name="checklogin"),
    path('logout',views.logout,name='logout'),
    path('ad',views.admin,name="admin"),
    path('addma', views.addma, name="addma"),
    path('adres', views.adres, name="adres"),
    path('viewcus', views.viewcus, name="viewcus"),
    path('viewma', views.viewma, name="viewma"),
    path('viewres',views.viewres,name="viewres"),
    path('cus',views.cus,name="cus"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('makereservation', views.makereservation, name="makereservation"),
    path('restaurant', views.restaurant, name="restaurant"),
    path('setcookies',views.setcookies),
    path('getcookies',views.getcookies),
    path('manager',views.manager),
    path('fooditems',views.fooditems),
    path('orderdetails',views.orderdetails),
    path('chefdetails',views.chefdetails),
    path("deletecust/<int:cid>",views.deletecust,name="deletecust"),
    path("deleterest/<int:rid>",views.deleterest,name="deleterest"),
    path("deleteman/<int:mid>",views.deleterest,name="deleteman"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
