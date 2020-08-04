import xadmin
from django.urls import path

from apps.competition.views import *

urlpatterns = [
    # xadmin后台路由
    path('xadmin/', xadmin.site.urls),
]
