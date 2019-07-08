from django.conf.urls import url
from SceneApp import views

urlpatterns = [
    #url(r'^index/',views.index,name='index'),
    url(r'^index_class/', views.IndexClass.as_view(), name='index_class'),
    #新增场景
    url(r'^scene_create/',views.SceneCreateView.as_view(),name='scene_create'),
    #场景列表
    url(r'^scene_list/',views.SceneListView.as_view(),name='scene_list'),
    #场景删除
    url(r'^scene_delete/',views.SceneDeleteView.as_view(),name='scene_delete'),
    #场景编辑
    url(r'^scene_update/',views.SceneUpdateView.as_view(),name='scene_update'),
    #场景环境列表
    url(r'^envir_list/',views.SceneEnvirListViwe.as_view(),name='nvir_list'),
    #场景安防列表
    #url(r'^save_list/',views.SceneSaveListView.as_view(),name='save_list'),
]
