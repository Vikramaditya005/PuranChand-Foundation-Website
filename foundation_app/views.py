from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, TemplateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import News, ContactMessage, Project, Volunteer, Podcast, Video, NewspaperCutting, EventPhoto, Review, Campaign
from .forms import ContactForm, VolunteerForm, CampaignForm


# Class-based Views
# ------------------------------------------------------------
class HomeView(TemplateView):
    """
    Renders the home page of the foundation website.
    Fetches a few latest projects to display.
    """
    template_name = 'foundation_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch a few latest projects (e.g., top 3)
        context['projects'] = Project.objects.order_by('-created_at')[:3]
        return context


class ProjectDetailView(DetailView):
    """
    Renders a detailed page for a specific project.
    Uses Django's DetailView to fetch the object by primary key (pk).
    """
    model = Project
    template_name = 'foundation_app/project_detail.html'
    context_object_name = 'project'


class AboutUsView(TemplateView):
    """
    Renders the 'About Us' page.
    """
    template_name = 'foundation_app/about_us.html'


class TeamView(TemplateView):
    """
    Renders the 'Our Team' page.
    """
    template_name = 'foundation_app/team.html'





class ContactView(View):
    """
    Handles the contact form submission and renders the contact page.
    """
    template_name = 'foundation_app/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                ContactMessage.objects.create(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    subject=form.cleaned_data['subject'],
                    message=form.cleaned_data['message']
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                print(f"Error saving contact message: {e}")
                messages.error(request, 'There was an error sending your message. Please try again.')
        else:
            messages.error(request, 'Please correct the errors in the form.')
        return render(request, self.template_name, {'form': form})
   


def launch_campaign(request):
    """
    Handles the form submission for launching a new campaign.
    """
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.save()
            messages.success(request, 'Your campaign has been launched successfully!')
        else:
            messages.error(request, 'There was an error launching your campaign. Please check the form.')
    
    return redirect(reverse('foundation_app:dashboard'))


class UserLoginView(TemplateView):
    """
    Handles user login.
    """
    template_name = 'foundation_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('foundation_app:dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, self.template_name, {'form': form})


class UserSignupView(TemplateView):
    """
    Handles user signup.
    """
    template_name = 'foundation_app/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now log in.")
            return redirect('foundation_app:login')
        return render(request, self.template_name, {'form': form})


class NewsListView(ListView):
    """
    Displays a list of all news articles.
    """
    model = News
    template_name = 'foundation_app/news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    """
    Displays a detailed page for a specific news article.
    """
    model = News
    template_name = 'foundation_app/news_detail.html'
    context_object_name = 'news_article'


class AllProjectsView(ListView):
    """
    Displays a list of all projects.
    """
    model = Project
    template_name = 'foundation_app/all_projects.html'
    context_object_name = 'all_projects'


class MediaCentreView(TemplateView):
    """
    Renders the 'Media Centre' page.
    """
    template_name = 'foundation_app/media_centre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['podcasts'] = Podcast.objects.all()
        return context


class PodcastListView(ListView):
    """
    Displays a list of all podcasts.
    """
    model = Podcast
    template_name = "foundation_app/podcast_list.html"
    context_object_name = "podcasts"


class VideoListView(ListView):
    """
    Displays a list of all videos.
    """
    model = Video
    template_name = "foundation_app/video_list.html"
    context_object_name = "videos"


class NewspaperCuttingListView(ListView):
    """
    Displays a list of all newspaper cuttings.
    """
    model = NewspaperCutting
    template_name = "foundation_app/newspaper_cuttings.html"
    context_object_name = "cuttings"


class EventPhotoListView(ListView):
    """
    Displays a list of all event photos.
    """
    model = EventPhoto
    template_name = "foundation_app/event_photos.html"
    context_object_name = "photos"


class ReviewListView(ListView):
    """
    Displays a list of all reviews.
    """
    model = Review
    template_name = "foundation_app/review_list.html"
    context_object_name = "reviews"


def volunteer_submit(request):
    """
    Handles the volunteer form submission.
    """
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for volunteering! We will contact you soon.')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    return redirect('foundation_app:dashboard')


def custom_logout(request):
    """
    Handles user logout.
    """
    if request.method == "POST":
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('foundation_app:home')
    return redirect('foundation_app:home')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CampaignForm
from .models import Campaign

@login_required
def dashboard(request):
    # Forms
    campaign_form = CampaignForm()
    volunteer_form = VolunteerForm()

    # Data
    campaigns = Campaign.objects.all().order_by("-created_at")
    volunteers = Volunteer.objects.all().order_by("-created_at")

    # Handle Campaign Submission
    if request.method == "POST" and "launch_campaign" in request.POST:
        campaign_form = CampaignForm(request.POST)
        if campaign_form.is_valid():
            new_campaign = campaign_form.save(commit=False)
            new_campaign.user = request.user
            new_campaign.save()
            messages.success(request, "Your campaign has been launched successfully!")
            return redirect("foundation_app:dashboard")
        else:
            messages.error(request, "There was an error launching your campaign. Please check the form.")

    # Context
    context = {
        "campaign_form": campaign_form,
        "campaigns": campaigns,
        "volunteers": volunteers,
        "volunteer_form": volunteer_form,
        "personalized_data": {
            "total_donations": "₹5,000",
            "projects_supported": ["Project A", "Project B"],
            "volunteer_hours": "10 hours",
        },
        "key_id": "rzp_test_RCeQhXtvZuW3nm",   # Razorpay Checkout key
    }

    return render(request, "foundation_app/dashboard.html", context)



import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def make_donation(request):
    if request.method == "POST":
        amount = int(request.POST.get("amount", 0))  # Get user entered donation
        if amount <= 0:
            messages.error(request, "Please enter a valid donation amount.")
            return redirect("foundation_app:dashboard")

        client = razorpay.Client(auth=("rzp_test_RCeQhXtvZuW3nm", "8WhtWulOvpImkKNmRM0829Ym"))

        payment = client.order.create({
            "amount": amount * 100,  # convert to paise
            "currency": "INR",
            "payment_capture": "1"
        })

        return render(request, "foundation_app/payment.html", {
            "key_id": "rzp_test_RCeQhXtvZuW3nm",  # matches your template
            "payment": payment,           # full payment object
        })


@csrf_exempt
def payment_success(request):
    return render(request, "foundation_app/success.html")
def volunteer_page(request):
    """
    Displays the volunteer form and the list of registered volunteers.
    """
    volunteers = Volunteer.objects.all().order_by("-created_at")  # latest first
    form = VolunteerForm()

    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for volunteering! We will contact you soon.")
            return redirect("foundation_app:volunteer_page")
        else:
            messages.error(request, "Please correct the errors in the form.")

    return render(request, "foundation_app/volunteer.html", {
        "form": form,
        "volunteers": volunteers,
    })
from django.shortcuts import render
from .models import GalleryImage

def gallery_view(request):
    images = GalleryImage.objects.all()
    return render(request, "foundation_app/gallery.html", {"images": images})
