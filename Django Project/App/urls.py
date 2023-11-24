from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet,PurchaseOrderViewSet,VendorPerformanceView,AcknowledgePurchaseOrder

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'purchase_orders', PurchaseOrderViewSet, basename='purchase-order')
urlpatterns = [
     # URLs generated by the router for the viewset
    path('api/', include(router.urls)),
     # Additional custom URLs for specific actions
    path('api/vendors/<int:pk>/', VendorViewSet.as_view(
        {'get':'retrieve',
         'put':'update',
         'patch':'partial_update',
         'delete':'destroy'}), name='vendor-detail'),
    path('api/vendor/',VendorViewSet.as_view({'get':'list','post':'create'}), name='vendor-list'),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('api/purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order'),
]

