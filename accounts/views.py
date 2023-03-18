from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth import login, authenticate, get_user_model
from .models import Profile
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required 

from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy



@user_passes_test(lambda u: u.is_superuser or u.is_staff, login_url='main-page')
def signup(request):
    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("mail")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password2")
        
        if pass1 == pass2:
            if User.objects.filter(username=username).first():
                messages.error(request, "This username is already taken")
                return redirect('main-page')
            user = User.objects.create(
                username=username, 
                email=email,
                is_active=False)
            
            user.set_password(pass1)
            user.save()
            
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)

            user.is_active = False
            user.save()
            
            messages.success(request, "Account created, but must be verified by admin before logging in.")
            return redirect('main-page') 
        else:
            messages.error(request, "Passwords do not match.")
            # Redirect to main page in case of an error
            return redirect('main-page')
            
    return render(request, "signup.html")



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main-page')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')



@user_passes_test(lambda u: u.is_superuser or u.is_staff, login_url='decode_pnr')
def main_page(request):
    users = User.objects.all()
    return render(request, 'main_page.html', {'users': users})



class ForgotPasswordView(PasswordResetView):
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
      


User = get_user_model() 

@login_required
@user_passes_test(lambda user: user.is_superuser or hasattr(user, 'profile') and user.profile.is_moderator, login_url='main-page')
def signup_moderator(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('main-page')

    if not request.user.has_perm('accounts.can_add_moderator'):
        messages.error(request, "You do not have permission to add a moderator.")
        return redirect('main-page')

    if request.method == "POST":
        username = request.POST.get("name")
        email = request.POST.get("mail")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("password2")

        if pass1 == pass2:
            if User.objects.filter(username=username).first():
                messages.error(request, "This username is already taken")
                return redirect('main-page')

            user = User.objects.create(
                username=username,
                email=email,
                is_active=False,
                is_staff=True,
            )

            user.set_password(pass1)
            user.save()

            moderator_group, created = Group.objects.get_or_create(name='Moderator')
            user.groups.add(moderator_group)

            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.is_moderator = True
                profile.save()

            user.is_active = True
            user.save()

            messages.success(request, "Account created, but must be verified by a moderator before logging in.")
            return redirect('main-page')
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, "signup_moderator.html")