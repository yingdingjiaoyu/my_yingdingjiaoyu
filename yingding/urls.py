from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('zytb/',views.zytb),
	path('test/',views.test),
	path('zytb/api/admissions/filter',views.admissions_data_filter_api)
]