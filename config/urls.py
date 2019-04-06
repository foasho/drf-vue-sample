from django.contrib import admin
from django.urls import path, re_path, include                   # 修正
from django.views.generic import TemplateView, RedirectView      # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),  # 追加
    path('api/v1/auth/', include('djoser.urls')),                # 追加
    path('api/v1/auth/', include('djoser.urls.jwt')),            # 追加
    path('api/v1/', include('apiv1.urls')),                      # 追加
    re_path('', RedirectView.as_view(url='/')),                  # 追加
]
