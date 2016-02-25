from django import forms 
from blog.models import Post

# ModelForm mapping user input to specific DB columns
class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title', 'content', 'tag', 'image']