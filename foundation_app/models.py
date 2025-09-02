from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Model for Contact Form Submissions
class ContactMessage(models.Model):
    """
    Represents a message submitted through the contact form on the website.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-submitted_at'] # Order by most recent messages first

    def __str__(self):
        """String representation for a ContactMessage."""
        return f"Message from {self.name} ({self.email})"

# Model for Foundation Projects/Content
class Project(models.Model):
    """
    Represents a project or initiative of the foundation,
    to be displayed on the home page or a dedicated projects page.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Foundation Project"
        verbose_name_plural = "Foundation Projects"
        ordering = ['-created_at']

    def __str__(self):
        """String representation for a Project."""
        return self.title

# Model for volunteer information
class Volunteer(models.Model):
    """
    Represents a volunteer who has signed up through the dashboard form.
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    availability = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Availability of the volunteer (e.g., Weekends, Weekdays, Full-time)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    link = models.URLField(blank=True, null=True)  # <-- Add this line
    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
class Podcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()  # Spotify, YouTube, Anchor, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return self.title
    
from django.db import models

from django.db import models
from django.utils import timezone

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)  # ✅ gives default automatically

    def __str__(self):
        return self.title

class NewspaperCutting(models.Model):
    title = models.CharField(max_length=200)  # Optional, just to identify image
    image = models.ImageField(upload_to='newspaper_cuttings/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title or f"Newspaper Cutting {self.id}"


class EventPhoto(models.Model):
    image = models.ImageField(upload_to='event_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Event Photo {self.id}"
class Review(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="reviews/images/", blank=True, null=True)
    video = models.FileField(upload_to="reviews/videos/", blank=True, null=True)  # MP4, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Campaign(models.Model):
    # The title of the fundraising campaign.
    title = models.CharField(max_length=200)

    # The financial goal for the campaign in Indian Rupees.
    goal_amount = models.IntegerField()

    # A detailed description of the campaign.
    description = models.TextField()

    # The user who created this campaign. The on_delete=models.CASCADE
    # ensures that if a user is deleted, their campaigns are also deleted.
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='campaigns')

    # The date and time the campaign was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # A human-readable representation of the Campaign model.
        return self.title

# foundation_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaigns")
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def progress_percentage(self):
        if self.goal_amount > 0:
            return (self.raised_amount / self.goal_amount) * 100
        return 0

    def __str__(self):
        return self.title
