from django.urls import path
from .views import AjaxCommentCreateView, CommentListView

urlpatterns = [
    path('ajax/add_comment/', AjaxCommentCreateView.as_view(), name='ajax_add_comment'),
    path('list/', CommentListView.as_view(), name='comment_list'),

]


