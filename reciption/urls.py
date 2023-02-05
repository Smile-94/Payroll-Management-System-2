from django.urls import path

app_name='reception'
# Views
from reciption.views import ReceptionView
from reciption.views import AddAttendanceView
from reciption.views import AttendanceListView
from reciption.views import IssuSortLeaveView
from reciption.views import SortleaveListView
from reciption.views import SortLeaveUpdateView
from reciption.views import SortLeaveDetailView


urlpatterns = [
    path('reception/',ReceptionView.as_view(),name='reception_home'),
    path('add-attendance/',AddAttendanceView.as_view(),name='add_attendance'),
    path('attendance-list/',AttendanceListView.as_view(),name='attendance_list'),
    path('sortleave/', IssuSortLeaveView.as_view(), name='sortleave'),
    path('sortleave-list/', SortleaveListView.as_view(), name='sortleave_list'),
    path('sortleave-detail/<int:pk>/', SortLeaveDetailView.as_view(), name='sortleave_detail'),
    path('sortleave-update/<int:pk>/',SortLeaveUpdateView.as_view(), name='sortleave_update'),
  
]
