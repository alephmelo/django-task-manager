from django.conf.urls import include, url

urlpatterns = [
    url(r'^sign-in',
    	 'django.contrib.auth.views.login',
    	{'template_name':'accounts/login.html'},
    	name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', 
        {'next_page': 'core:home'}, name='logout'),
    url(r'^join-us$', 'accounts.views.register', 
        name='register'),
]