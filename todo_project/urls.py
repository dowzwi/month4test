from django.contrib import admin
from django.urls import path, include  # Не забудьте импортировать include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Подключаем URLs приложения tasks
]
