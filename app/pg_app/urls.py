from django.urls import path
from pg_app.views import (
    index,
)


app_name = "app"

urlpatterns = [
    path("", index, name="dashboard"),
]
