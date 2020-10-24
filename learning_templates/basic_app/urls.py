from django.conf.urls import url
from django.urls import path
from basic_app import views

#TEMPALTE TAGGING
app_name = 'basic_app'


urlpatterns = [
    # path('base/',views.base,name="base"),
    # path('index/', views.index, name = 'index'),
    path('other/', views.other, name = 'other'),
    path("relative/",views.relative,name="relative")
]
