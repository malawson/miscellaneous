from django.contrib import admin
from blog.models import Post

# Register your models here.

# import the model and
# tell django which models we want available in the admin

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'views')

admin.site.register(Post, PostAdmin)
