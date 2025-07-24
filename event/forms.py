from django import forms
from event.models import Event, Participant, EventDetails


class CustomTimeInput(forms.TimeInput):
    input_type = "time"


class StyleClassMixin:
    default_classes = "border border-gray-600 rounded-lg text-white bg-gray-800 p-2 my-2 shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-rose-500"

    def applyStyles(self):
        for field_name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, (forms.TextInput, forms.PasswordInput, forms.EmailInput)):
                widget.attrs.update({
                    "class": f"w-full {self.default_classes}",
                })

            elif isinstance(widget, forms.Textarea):
                widget.attrs.update({
                    "class": f"w-full h-28 resize-none {self.default_classes}",
                })

            elif isinstance(widget, forms.SelectDateWidget):
                widget.attrs.update({
                    "class": f"{self.default_classes}", 
                })

            elif isinstance(widget, forms.Select):
                widget.attrs.update({
                    "class": f"{self.default_classes}",
                })




class EventForm(StyleClassMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full",
                    "placeholder": "Enter event name",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter event description",
                }
            ),
            "date": forms.SelectDateWidget(attrs={}),
            "participants": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "border border-gray-600 rounded-lg text-white bg-gray-800 p-2 my-2 shadow-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-rose-500",
                }
            ),
            "time": CustomTimeInput(
                attrs={
                    "class": "h-5 p-2 rounded-lg bg-gray-800 my-2 text-blue-300",
                },
                format="%H:%M",
            ),
            "location": forms.TextInput(
                attrs={
                    "class":"h-10",
                    "placeholder": "Enter event location",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles()


class EventDetailsForm(StyleClassMixin, forms.ModelForm):
    class Meta:
        model = EventDetails
        fields = ["notes", "livestream_url", "speakers"]
        widgets = {
            "livestream_url": forms.TextInput(
                attrs={
                    "class": "w-full text-blue-300 bg-gray-800 p-2 my-2 shadow-sm border-1 rounded-lg",
                    "placeholder": "Enter URL",
                }
            ),
            "speakers": forms.Textarea(
                attrs={
                    "placeholder": "Enter speakers' names",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles()
