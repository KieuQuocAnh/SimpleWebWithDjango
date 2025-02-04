from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,AuthenticationForm
from .models import Profile
from django import forms
from django.utils.translation import gettext_lazy as _

from django.forms.widgets import ClearableFileInput
class CustomFileInput(ClearableFileInput):
    template_name = 'custom_widgets/custom_file_input.html'

    class Media:
        css = {
            'all': ('custom_css/custom_file_input.css',)  # CSS tùy chỉnh
        }    
class CustomTextInput(ClearableFileInput):
    template_name = 'custom_widgets/custom_text_input.html'

    class Media:
        css = {
            'all': ('custom_css/custom_text_input.css',)  # CSS tùy chỉnh
        }    

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
                                max_length=150,
                                widget=forms.TextInput(attrs={'placeholder':_('Enter Your Register Username')}))
    
    password = forms.CharField(
            label=_("Password"),
            widget=forms.PasswordInput(attrs={
                
            "id": "password-field",
            'placeholder':_('Enter Your Password')

            },
        )
    )
    def __init__(self, *args, **kwargs):
        # Lấy request từ kwargs (nếu được truyền)
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label=_("Username"),
                                max_length=150,
                                widget=forms.TextInput(attrs={'placeholder': _('Enter Your Register Username')}))
    email = forms.EmailField(
        label=_('Email address'),
        max_length=200, help_text=_('Required. Inform a valid email address.'),
        widget=forms.EmailInput(attrs={'placeholder': _('Enter Your Email')}))
    password1 = forms.CharField(
        help_text=_('*Password must be at least 8 characters long and not similar to the username, email, or personal information.'),
        label=_("Password"),
        widget=forms.TextInput(attrs={
            "id": "password-field",
            'placeholder':_('Enter Your Password')
            },
            )
            )
    password2 = forms.CharField(
        label=_('Confirm Password'),
        help_text=_('*Password must be at least 8 characters long and not similar to the username, email, or personal information.'),
        widget=forms.TextInput(attrs={
            "id": 'password-field',
            'placeholder':_('Confirm Your Password')
            },
            ),
            )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=200,
                            label=_('Email address'),
                            help_text=_('Required. Inform a valid email address.'),
                            widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': _('Enter Your Email')}))
                             

    
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    user_name = forms.CharField(
        required=False,
        label=_('Your name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Enter Your name If You want')

            }
            ))    
    PR_content=forms.CharField(
        required=False,
        label=_('About Your Self'),
        widget=forms.TextInput(
            attrs={'class': 'form-control','placeholder': _('Do you Want to write something about yourself')}
            
        )   
        )
    image = forms.ImageField(
        label=_('Upload Your Image'),
        widget=CustomFileInput(
            attrs={
                'id': 'profile_image',  # ID để liên kết với thẻ <label>
                'label': _('Select a file'),  # Nội dung nút bấm
                'accept': 'image/*',  # Chỉ chấp nhận file ảnh
            }
            ))
    class Meta:
        model = Profile
        fields=['user_name','image','PR_content']
        # widgets = {
        #     'user_name': forms.TextInput(attrs={'class': 'form-control-file','placeholder': _('Enter Your name If You want')}),
        #     'PR_content': forms.TextInput(attrs={'class': 'form-control-file','placeholder': _('Do you Want to write something about yourself')}),
        #     'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        # }
        
# class Profile_PR_comtent(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['PR_content']  # Chỉ định trường cần hiển thị  



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_('Old PassWord'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Enter current password')})
    )
    new_password1 = forms.CharField(
        label=_('PassWord'),
        help_text=_('*Password must be at least 8 characters long and not similar to the username, email, or personal information.'),
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Enter new password')})
    )
    new_password2 = forms.CharField(
        label=_('Confirm Password'),
        help_text=_('*Password must be at least 8 characters long and not similar to the username, email, or personal information.'),
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Confirm new password')})
    )
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')    


