from django.contrib import admin
from .models import ContactMessage, Project, Volunteer, News, Podcast, Video, NewspaperCutting, EventPhoto, Review, Campaign

# Register the models to be displayed in the Django admin site.

# Admin class for the ContactMessage model
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # Display these fields in the change list page
    list_display = ('name', 'email', 'subject', 'submitted_at')
    # Make these fields clickable to open the detail view
    list_display_links = ('name',)
    # Add a search bar for these fields
    search_fields = ('name', 'email', 'subject', 'message')
    # Filter by submission date
    list_filter = ('submitted_at',)
    date_hierarchy = 'submitted_at'

# Admin class for the Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

# Admin class for the new Volunteer model
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'availability', 'created_at')
    search_fields = ('full_name', 'email', 'phone')
    list_filter = ('availability', 'created_at')
    date_hierarchy = 'created_at'

# Admin class for the News model
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    # We prepopulate the slug from the title
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created_at')
    search_fields = ('title', 'url')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(NewspaperCutting)
class NewspaperCuttingAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_amount', 'created_by', 'created_at')

    def created_by(self, obj):
        return obj.user.username   # or obj.user.get_full_name()
    created_by.admin_order_field = 'user'   # makes it sortable
    created_by.short_description = 'Created By'
