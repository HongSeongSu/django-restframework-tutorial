from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import function_views, class_views

# urlpatterns = [
#     url(r'^snippets/$', function_views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', function_views.snippet_detail),
#
# ]

urlpatterns = [
    url(r'^snippets/$', class_views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', class_views.SnippetDetail.as_view()),
    url(r'^users/$', class_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', class_views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
