from rest_framework.routers import SimpleRouter

from app.views.account import AccountViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'^account', AccountViewSet)

urlpatterns = router.urls
