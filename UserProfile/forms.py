from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, get_user_model
User=get_user_model()

class UserLoginForm(forms.Form):
    email=forms.EmailField(max_length=150)
    password=forms.CharField(label='Password', widget=forms.PasswordInput)
    def clean(self,*args,**kwargs):

        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        user_obj=User.objects.filter(email=email).first()
        if not user_obj:
            raise forms.ValidationError("invilid password or Username")
        else:
            if not user_obj.check_password(password):
                raise forms.ValidationError("invilid Password or username")
        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    sfields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Enter Correct Password")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
