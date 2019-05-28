from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('',views.index,name="index"),
    path('<int:entity_id>/', views.detail, name='detail'),
    path('register/qwertyuiop0987654321',views.register,name="register"),
    path('register/qwertyuiop0987654321/post',views.post_register,name="register"),
    path('login',views.login,name="login"),
    path('post_login',views.post_login,name="login"),
    path('submit_thread',views.submit,name="submit"),
    path('search',views.search,name="search"),
    path('posts',views.posts,name="posts"),
    path('posts_add',views.add_post,name="posts"),
    path('create_post',views.post_posts,name="add posts")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)