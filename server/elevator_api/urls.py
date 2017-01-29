# from .views import booksViewSet, carsViewSet
from .views import  carsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(prefix='books', viewset=booksViewSet),
router.register(prefix='car', viewset= carsViewSet),


