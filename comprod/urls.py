from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from company.views import CompanyViewSet
from product.views import ProductViewSet

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='v1',
        description="API documentation of App",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
]