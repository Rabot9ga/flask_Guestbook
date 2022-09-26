from wtforms_alchemy import ModelForm
from models import Guestbook

class GuestForm(ModelForm):
    class Meta:
        model = Guestbook