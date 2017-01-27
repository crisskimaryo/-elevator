from .views import booksViewSet 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(prefix='books', viewset=booksViewSet)
