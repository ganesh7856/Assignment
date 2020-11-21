from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


from productsapi.views import ProductViewSet,CategoryViewSet,CategoryDetailView


router = DefaultRouter()
router.register("product", ProductViewSet)
router.register("Category", CategoryViewSet)
router.register(r'mostviewed', views.CategoryDetailView, basename="CategoryDetailView")

#router.register(r"Product/", ProductsDetailView, basename='Product')


urlpatterns = [
               path("", include(router.urls)),

               ]
