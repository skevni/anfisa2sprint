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


class ContestForm1(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea({'cols': '22', 'rows': '5'}),
    )
    price = forms.IntegerField(
        label='Цена',
        min_value=10, max_value=100,
        help_text='Рекомендованная розничная цена',
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea({'cols': '22', 'rows': '5'}),
    )