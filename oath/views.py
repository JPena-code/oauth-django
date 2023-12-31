from django.shortcuts import redirect


def home(request, *args, **kwargs):
    """
        Simple redirect to the login page after request the home page
        return HTTPResponseRedirect
    """
    return redirect('/login')
