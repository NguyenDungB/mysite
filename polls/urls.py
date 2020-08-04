
from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/detils/5/
#     #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^details/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/ 
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
# ]