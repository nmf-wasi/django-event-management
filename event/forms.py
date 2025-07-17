from django import forms
from event.models import Event, Participant


class CustomTimeInput(forms.TimeInput):
    input_type = "time"


class StyleClassMixin:
    default_classes = "border-1 rounded-lg text-blue-300 bg-gray-800 p-2 my-2 shadow-sm"

    def applyStyles(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update(
                    {
                        "class": f"{self.default_classes}",
                    }
                )
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update(
                    {
                        "class": f"{self.default_classes} w-full ",
                        "placeholder": f"Enter event description ",
                    }
                )
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update(
                    {
                        "type": "date",
                        "class": f"{self.default_classes}",
                    }
                )
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update(
                    {
                        "class": f"{self.default_classes}",
                    }
                )


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
                    "class": "p-2 m-2 rounded-lg my-2 border-none",
                }
            ),
            "time": CustomTimeInput(
                attrs={
                    "class": "p-2 rounded-lg bg-gray-800 my-2 text-blue-300",
                },
                format="%H:%M",
            ),
            "location": forms.TextInput(
                attrs={
                    "placeholder": "Enter event location",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.applyStyles()
