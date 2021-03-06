from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    # modifies admin view
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)
