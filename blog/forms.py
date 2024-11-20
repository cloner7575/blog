from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        is_published = cleaned_data.get('is_published')

        # بررسی تکمیل بودن فیلدهای ضروری
        required_fields = ['title', 'image', 'category', 'short_description', 'description', 'content', 'author', 'released_at']
        missing_fields = [
            self._meta.model._meta.get_field(field).verbose_name
            for field in required_fields
            if not cleaned_data.get(field)
        ]

        if is_published and missing_fields:
            raise ValidationError({
                'is_published': f"برای انتشار پست، فیلدهای زیر باید تکمیل شوند: {', '.join(missing_fields)}"
            })

        return cleaned_data
