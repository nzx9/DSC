from django.urls import path
from streams import views
from django.conf import settings
from django.conf.urls.static import static

import streams

urlpatterns = [
    path('', views.streams_view, name="streams_view"),
    path('rec/<str:e_word>/', views.streams_rec_view, name="streams_rec_view"),
    # path('upload/', views.uploadStreams, name="stream_uploads"),
    path('submit/<str:e_word>/', views.submit, name="submit"),
    path('verification', views.streams_verification, name="stream_verification"),
    path('get/<str:pk>', views.get_stream, name="get_stream"),
    path('verify/<str:pk>', views.verify_stream, name="verify_stream"),
    path('table', views.streams_table_home, name="streams_table_home")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
