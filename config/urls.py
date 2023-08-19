from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # продавец
    path('vendors/', include('vendor.urls')),
    # корзина
    path('cart/', include('cart.urls')),
    # заказы
    path('orders/', include('order.urls')),
    # главная страница
    path('', include('core.urls')),
    # страница товаров
    path('', include('product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
