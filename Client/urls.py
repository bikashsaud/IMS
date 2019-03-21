from django.urls import path
# from CMS.views import base,agentsignin,signup,signout,agent,client,clientsignin
# from . import views
from . import views
app_name='Client'

urlpatterns = [
    path('register-client/', views.register_client,name='register_client'),
    path('register-agent/', views.register_agent,name='register_agent'),
    path('client-login/',views.client_login,name="client_login"),
    path('agent-login/',views.agent_login,name="agent_login"),
    path('client-detail/',views.client_detail,name="client_detail"),
    path('add-policy/(?P<id>[0-9]+)/$',views.add_policy,name="add_policy"),
    ]
