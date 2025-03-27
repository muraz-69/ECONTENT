from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils import timezone
from django.urls import reverse
from .models import * 
from .forms import BibleAndManResourceForm
from .forms import ClimateChangeResourceForm
from .forms import HealthWellnessResourceForm
from .forms import TrendyFashionResourceForm
from .forms import EBookForm
from .forms import OnlineCourseForm
from .forms import NewsletterForm





# Create your views here.
@login_required
def Home(request):
    return render(request, 'index.html') 

def RegisterView(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exists')

        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, 'Password must be at least 5 characters long')

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')
        
    return render(request, 'register.html')

    

def LoginView(request):

     if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

     return render(request, 'login.html')

def LogoutView(request):

    logout(request)

    return redirect('login')

def ForgotPassword(request):
     
      if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})

            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'
        
            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver 
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")

            return redirect('forgot-password')

      return render(request, 'forgot_password.html')

def PasswordResetSent(request, reset_id):
     
     if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
     else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

def ResetPassword(request, reset_id):

    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            passwords_have_error = False

            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')

            if len(password) < 5:
                passwords_have_error = True
                messages.error(request, 'Password must be at least 5 characters long')

            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'Reset link has expired')

                password_reset_id.delete()

            if not passwords_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()

                messages.success(request, 'Password reset. Proceed to login')
                return redirect('login')
            else:
                # redirect back to password reset page and display errors
                return redirect('reset-password', reset_id=reset_id)

    
    except PasswordReset.DoesNotExist:
        
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

    return render(request, 'reset_password.html')

#check if user is admin
def is_admin(user):
    return user.is_superuser

# list all resources
def bible_and_man_list(request):
    resources = BibleAndManResource.objects.all()
    return render(request, 'bible_and_man/list.html', {'resources': resources})

#view details of a single resource
def bible_and_man_detail(request, pk):
    resource = get_object_or_404(BibleAndManResource, pk=pk)
    return render(request, 'bible_and_man/detail.html', {'resource': resource})

#ADMIN - add new resource
@login_required
@user_passes_test(is_admin)
def bible_and_man_create(request):
    if request.method == 'POST':
        form = BibleAndManResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.save()
            return redirect('bible_and_man_list')
        else:
            return render(request, 'bible_and_man/form.html', {'form': form})
    else:
        form = BibleAndManResourceForm()
        return render(request, 'bible_and_man/form.html', {'form': form})
    
#admin- edit resource
@login_required
@user_passes_test(is_admin)
def bible_and_man_update(request, pk):
    resource = get_object_or_404(BibleAndManResource, pk=pk)
    if request.method == 'POST':
        form = BibleAndManResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            resource.uploaded_by = request.user
            resource.save()
            return redirect('bible_and_man_list')
    else:
        form = BibleAndManResourceForm(instance=resource)
        return render(request, 'bible_and_man/form.html', {'form': form})
    
#admin - Delete resources
@login_required
@user_passes_test(is_admin)
def bible_and_man_delete(request, pk):
    resource = get_object_or_404(BibleAndManResource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('bible_and_man_list')
    return render(request, 'bible_and_man/confirm_delete.html', {'resource': resource})

# Check if user is admin
def is_admin(user):
    return user.is_superuser

# List all resources
def climate_change_list(request):
    resources = ClimateChangeResource.objects.all()
    return render(request, 'climate_change/list.html', {'resources': resources})

# View details of a single resource
def climate_change_detail(request, pk):
    resource = get_object_or_404(ClimateChangeResource, pk=pk)
    return render(request, 'climate_change/detail.html', {'resource': resource})

# Admin - Add new resource
@login_required
@user_passes_test(is_admin)
def climate_change_create(request):
    if request.method == 'POST':
        form = ClimateChangeResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.save()
            return redirect('climate_change_list')
    else:
        form = ClimateChangeResourceForm()
    return render(request, 'climate_change/form.html', {'form': form})

# Admin - Edit resource
@login_required
@user_passes_test(is_admin)
def climate_change_update(request, pk):
    resource = get_object_or_404(ClimateChangeResource, pk=pk)
    if request.method == 'POST':
        form = ClimateChangeResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            resource.uploaded_by = request.user
            resource.save()
            return redirect('climate_change_list')
    else:
        form = ClimateChangeResourceForm(instance=resource)
    return render(request, 'climate_change/form.html', {'form': form})

# Admin - Delete resource
@login_required
@user_passes_test(is_admin)
def climate_change_delete(request, pk):
    resource = get_object_or_404(ClimateChangeResource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('climate_change_list')
    return render(request, 'climate_change/confirm_delete.html', {'resource': resource})

#health and wellness
# List View
def health_wellness_list(request):
    resources = HealthWellnessResource.objects.all()
    return render(request, 'health_wellness/list.html', {'resources': resources})

# Detail View
def health_wellness_detail(request, pk):
    resource = get_object_or_404(HealthWellnessResource, pk=pk)
    return render(request, "health_wellness/detail.html", {"resource": resource})
# Create View
def health_wellness_create(request):
    if request.method == "POST":
        form = HealthWellnessResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('health_wellness_list')
    else:
        form = HealthWellnessResourceForm()
    return render(request, 'health_wellness/form.html', {'form': form})

# Update View
def health_wellness_update(request, pk):
    resource = get_object_or_404(HealthWellnessResource, pk=pk)
    if request.method == "POST":
        form = HealthWellnessResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('health_wellness_list')
    else:
        form = HealthWellnessResourceForm(instance=resource)
    return render(request, 'health_wellness/form.html', {'form': form})

# Delete View
def health_wellness_delete(request, pk):
    resource = get_object_or_404(HealthWellnessResource, pk=pk)
    if request.method == "POST":
        resource.delete()
        return redirect('health_wellness_list')
    return render(request, 'health_wellness/confirm_delete.html', {'resource': resource})

def is_admin(user):
    return user.is_superuser

# List all resources
def trendy_fashion_list(request):
    resources = TrendyFashionResource.objects.all()
    return render(request, 'trendy_fashion/list.html', {'resources': resources})

# View details of a single resource
def trendy_fashion_detail(request, pk):
    resource = get_object_or_404(TrendyFashionResource, pk=pk)
    return render(request, 'trendy_fashion/detail.html', {'resource': resource})

# Admin - Add new resource
@login_required
@user_passes_test(is_admin)
def trendy_fashion_create(request):
    if request.method == 'POST':
        form = TrendyFashionResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.save()
            return redirect('trendy_fashion_list')
    else:
        form = TrendyFashionResourceForm()
    return render(request, 'trendy_fashion/form.html', {'form': form})

# Admin - Edit resource
@login_required
@user_passes_test(is_admin)
def trendy_fashion_update(request, pk):
    resource = get_object_or_404(TrendyFashionResource, pk=pk)
    if request.method == 'POST':
        form = TrendyFashionResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('trendy_fashion_list')
    else:
        form = TrendyFashionResourceForm(instance=resource)
    return render(request, 'trendy_fashion/form.html', {'form': form})

# Admin - Delete resource
@login_required
@user_passes_test(is_admin)
def trendy_fashion_delete(request, pk):
    resource = get_object_or_404(TrendyFashionResource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('trendy_fashion_list')
    return render(request, 'trendy_fashion/confirm_delete.html', {'resource': resource})

def is_admin(user):
    return user.is_superuser

# List all e-books
def ebook_list(request):
    ebooks = EBook.objects.all()
    return render(request, 'ebooks/list.html', {'ebooks': ebooks})

# View details of a single e-book
def ebook_detail(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    return render(request, 'ebooks/detail.html', {'ebook': ebook})

# Admin - Add new e-book
@login_required
@user_passes_test(is_admin)
def ebook_create(request):
    if request.method == 'POST':
        form = EBookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save(commit=False)
            ebook.uploaded_by = request.user
            ebook.save()
            return redirect('ebooks_list')
    else:
        form = EBookForm()
    return render(request, 'ebooks/form.html', {'form': form})

# Admin - Edit e-book
@login_required
@user_passes_test(is_admin)
def ebook_update(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    if request.method == 'POST':
        form = EBookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EBookForm(instance=ebook)
    return render(request, 'ebooks/form.html', {'form': form})

# Admin - Delete e-book
@login_required
@user_passes_test(is_admin)
def ebook_delete(request, pk):
    ebook = get_object_or_404(EBook, pk=pk)
    if request.method == 'POST':
        ebook.delete()
        return redirect('ebook_list')
    return render(request, 'ebooks/confirm_delete.html', {'ebook': ebook})

def is_admin(user):
    return user.is_superuser

# List all courses
def online_course_list(request):
    courses = OnlineCourse.objects.all()
    return render(request, 'online_courses/list.html', {'courses': courses})

# View a single course
def online_course_detail(request, pk):
    course = get_object_or_404(OnlineCourse, pk=pk)
    return render(request, 'online_courses/detail.html', {'course': course})

# Admin - Add new course
@login_required
@user_passes_test(is_admin)
def online_course_create(request):
    if request.method == 'POST':
        form = OnlineCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('online_course_list')
    else:
        form = OnlineCourseForm()
    return render(request, 'online_courses/form.html', {'form': form})

# Admin - Edit course
@login_required
@user_passes_test(is_admin)
def online_course_update(request, pk):
    course = get_object_or_404(OnlineCourse, pk=pk)
    if request.method == 'POST':
        form = OnlineCourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('online_course_list')
    else:
        form = OnlineCourseForm(instance=course)
    return render(request, 'online_courses/form.html', {'form': form})

# Admin - Delete course
@login_required
@user_passes_test(is_admin)
def online_course_delete(request, pk):
    course = get_object_or_404(OnlineCourse, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('online_course_list')
    return render(request, 'online_courses/confirm_delete.html', {'course': course})

def subscribe_newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if NewsletterSubscription.objects.filter(email=email).exists():
                messages.error(request, "This email is already subscribed!")
            else:
                form.save()
                messages.success(request, "Email subscribed successfully!")
        return redirect('home')  # Change 'home' to your actual template name
    
    form = NewsletterForm()
    return render(request, 'newsletter.html', {'form': form})

def is_admin(user):
    return user.is_superuser  # Only allow superusers (admins)

@login_required
@user_passes_test(is_admin)
def manage_subscriptions(request):
    template, created = NewsletterTemplate.objects.get_or_create(id=1)
    subscribers = NewsletterSubscription.objects.all()

    if "save_content" in request.POST:  # If admin clicks "Save Newsletter"
            template.content = request.POST.get("message")
            template.save()
            messages.success(request, "Newsletter content updated successfully!")
            return redirect('manage_subscription')
    
    elif request.method == "POST":
        selected_emails = request.POST.getlist('emails')  # List of selected emails
        message_content = request.POST.get('message', '').strip()  # Extract message content

    
        if not selected_emails:
            messages.error(request, "Please select at least one email.")
            return redirect('manage_subscriptions')

        if not message_content:
            messages.error(request, "Newsletter content cannot be empty.")
            return redirect('manage_subscriptions')

        subject = "Welcome to Fidelity Digital School Newsletter"
        from_email = settings.DEFAULT_FROM_EMAIL

        # Render HTML template for email
        html_content = render_to_string('newsletter.html', {'content': message_content})

        for email in selected_emails:
            msg = EmailMultiAlternatives(subject, message_content, from_email, [email])
            msg.attach_alternative(html_content, "text/html")  # Ensures HTML formatting
            msg.send()

        # Redirect to newsletter page to display the sent message
        return render(request, 'newsletter.html', {'content': message_content})

    return render(request, 'manage_subscriptions.html', {'subscribers': subscribers, "template": template})

@login_required
def edit_newsletter(request):
    template, created = NewsletterTemplate.objects.get_or_create(id=1)

    if request.method == "POST":
        template.subject = request.POST.get("subject")
        template.content = request.POST.get("message")
        template.save()
        messages.success(request, "Newsletter updated successfully!")
        return redirect('manage_subscriptions')

    return render(request, "edit_newsletter.html", {"template": template})
