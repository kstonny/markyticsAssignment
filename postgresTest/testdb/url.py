from django.conf.urls import url 
from testdb import views 
 
urlpatterns = [ 
url(r'^signup/$', views.signup, name='signup'),
url(r'^login/$', views.login_view, name='login'),
url(r'^home/$', views.home_view, name='home'),
url(r'^$', views.index, name='index'),
url(r'^logout/$', views.user_logout, name='logout'),
url(r'^card/$', views.card, name='card'),
url(r'^report-incident/$', views.report_incident, name='report-incident'),
]
