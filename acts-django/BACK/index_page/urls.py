from django.conf.urls import url, include
from index_page.views import index_page_render, about_page_render, teacherstaff_page_render


urlpatterns = [
    url(r'^about/', about_page_render),
    url(r'^teacherstaff/', teacherstaff_page_render),
    url(r'^', index_page_render),
]