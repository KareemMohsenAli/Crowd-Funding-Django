
# urls for projects only 


from django.urls import path

from projects.views import *


urlpatterns = [
    path('',AllProjects.as_view(),name="allprojects"),
    path('<int:pk>/detail',ProjectDetailedView.as_view(),name="detail"),
    path('createproject/',ProjectCreateView.as_view(),name="createproject"),
    path('deleteproject/<int:pk>', ProjectDeleteView.as_view(), name='deleteproject'),
    path('updateproject/<int:pk>', ProjectUpdateView.as_view(),name='updateproject'),
    path('<int:pk>/add-comment', add_comment,name='add_comment'),
    path('<int:pk>/delete-comment', delete_comment,name='delete_comment'),
    path('<int:pk>/report-comment', report_comment,name='report_comment')
    #==========================(CommentCreateion)==========================
    # path('createcomment/<int:pk>',CommentCreate.as_view(),name="createcomment"),
    #==========================(donateion)==========================

]

