from django.urls import path, include
from .views import BookingList, BookingView, RoomDetailView, RoomListView

app_name = 'app'
urlpatterns = [
    path('room_list/', RoomListView, name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
]
