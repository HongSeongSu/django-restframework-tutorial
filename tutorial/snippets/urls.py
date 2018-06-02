from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import function_views, class_views

# urlpatterns = [
#     url(r'^snippets/$', function_views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', function_views.snippet_detail),
#
# ]

urlpatterns = format_suffix_patterns([
    url(r'^$', class_views.api_root),
    url(r'^snippets/$', class_views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', class_views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', class_views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^users/$', class_views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', class_views.UserDetail.as_view(), name='user-detail')
])
