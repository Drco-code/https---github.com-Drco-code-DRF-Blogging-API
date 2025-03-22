from django.urls import path

from .import views

urlpatterns = [
    path(
        "",
        views.BlogPostListCreateAPIView.as_view(),
        name="blogs"
    )
    
]
