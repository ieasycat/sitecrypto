from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUser(LoginView):
    """
    Handles user authentication and displays the login form.

    This view provides a form for users to enter their credentials. Upon form submission,
    it authenticates the user based on the provided credentials. If the credentials are
    correct, the user is logged in and redirected as configured.

    Permissions:
        - Accessible to all users, including unauthenticated users.
    """

    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'LogIn'}
