"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from user import urls as userurls
from branch import urls as branchurls
from subject import urls as subjecturls
from document import urls as documenturls

from restapi import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/', include(userurls)),
    path('branch/', include(branchurls)),
    path('subject/', include(subjecturls)),
    path('document/', include(documenturls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
