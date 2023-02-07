from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ProfileAdmin


@login_required
def all_profiles(request):

    """ Dsiplay the user's profile """

    all_profiles = ProfileAdmin.objects.all()
    print(all_profiles)

    template = 'adminpage/adminpage.html'
    
    context = {
        'profiles': all_profiles,
	}
    
    return render(request, template, context)
