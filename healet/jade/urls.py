from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jade'

urlpatterns = [
    path('', views.home, name="home"),
    path('product_list/', views.product_list, name="product_list"),
    path('product_detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.product_detail, name="product_detail"),
    path('product_list_by_category/<slug:category_slug>/', views.product_list, name="product_list_by_category"),
    path('add_product/', views.add_product, name="add_product"),
    path('product_update/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.update_product, name="update_product"),
    path('comments/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.comments, name="comments"),
    path('profile/', views.profile, name="profile"),
    path('about/', views.about, name="about"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
