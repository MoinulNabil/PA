from django.views import generic
from django.contrib.auth import get_user_model


User = get_user_model()


class Home(generic.ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'user_profile/list.html'
