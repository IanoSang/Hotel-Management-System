from django.urls import path, include
from .views import RoomList, BookingList, BookingView, RoomDetailView

app_name = 'app'
urlpatterns = [
    path('room_list/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
]
