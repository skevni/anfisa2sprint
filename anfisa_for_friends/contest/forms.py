from django import forms

from contest.models import Contest


class ContestForm(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    class Meta():
        """
        docstring
        """
        model = Contest
        fields = '__all__'
        widgets = {
            'description': forms.Textarea({'cols': '22', 'rows': '5'}),
            'comment': forms.Textarea({'cols': '22', 'rows': '5'})
        }
