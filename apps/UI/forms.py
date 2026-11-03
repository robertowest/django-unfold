from django import forms
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row

from unfold.layout import Submit
from unfold.widgets import (
    BASE_INPUT_CLASSES,
    UnfoldAdminCheckboxSelectMultipleWidget,
    UnfoldAdminIntegerFieldWidget,
    UnfoldAdminRadioSelectWidget,
    UnfoldAdminSelectMultipleWidget,
    UnfoldAdminSelectWidget,
    UnfoldAdminSplitDateTimeVerticalWidget,
    UnfoldAdminTextInputWidget,
    UnfoldAdminURLInputWidget,
    UnfoldBooleanSwitchWidget,
    UnfoldBooleanWidget,
)

MONEDAS = [('EUR', 'Euro'), ('USD', 'Dólar'), ('GBP', 'Libra')]

DEPARTAMENTOS_CORTOS = [('sales', 'Sales'), ('marketing', 'Marketing')]

DEPARTAMENTOS = DEPARTAMENTOS_CORTOS + [
    ('development', 'Development'),
    ('human_resources', 'Human Resources'),
    ('other', 'Other'),
]

CATEGORIAS_CORTAS = [('general', 'General Inquiry'), ('technical', 'Technical Support')]

CATEGORIAS = CATEGORIAS_CORTAS + [('feedback', 'Feedback'), ('other', 'Other')]

PRIORIDADES = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]

OPCIONES = [
    ('a', 'Option A – Get instant notifications about price drops and special discounts on selected products.'),
    ('b', 'Option B – Stay updated on back-in-stock alerts for high-demand or previously sold-out items.'),
    ('c', 'Option C – Receive recommendations for products that match your shopping preferences and interests.'),
    ('d', 'Option D – Access exclusive member-only flash sales and early access to new product launches.'),
    ('e', 'Option E – Track your order status and get real-time shipping and delivery updates.'),
]


class FormularioHorizontalForm(forms.Form):
    """
    Formulario de ejemplo con etiquetas a la izquierda y campos a la derecha.
    """

    name = forms.CharField(label='Name', widget=UnfoldAdminTextInputWidget())
    email = forms.EmailField(label='Email', widget=UnfoldAdminTextInputWidget())
    age = forms.IntegerField(label='Age', widget=UnfoldAdminIntegerFieldWidget())
    salary = forms.DecimalField(label='Salary', max_digits=12, decimal_places=2, help_text='Enter your salary', widget=UnfoldAdminTextInputWidget())
    currency = forms.ChoiceField(label='Currency', choices=MONEDAS, widget=UnfoldAdminSelectWidget(), initial='EUR')
    subscribe = forms.BooleanField(
        label='Subscribe to newsletter',
        required=False,
        initial=True,
        help_text='Toggle to receive our newsletter with updates and offers',
        widget=UnfoldBooleanSwitchWidget(),
    )
    notifications = forms.BooleanField(
        label='Receive notifications',
        required=False,
        help_text='Toggle to receive notifications about your inquiry status',
        widget=UnfoldBooleanWidget(),
    )
    department = forms.ChoiceField(
        label='Department',
        choices=DEPARTAMENTOS_CORTOS,
        help_text='Select the department to contact',
        widget=UnfoldAdminRadioSelectWidget(),
    )
    category = forms.MultipleChoiceField(
        label='Category',
        choices=CATEGORIAS_CORTAS,
        help_text='Select the category of your message',
        widget=UnfoldAdminCheckboxSelectMultipleWidget(),
    )
    date_time = forms.SplitDateTimeField(label='Date and Time', widget=UnfoldAdminSplitDateTimeVerticalWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # form-horizontal hace que unfold_crispy coloque la etiqueta a la izquierda
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            'name',
            'email',
            'age',
            Row(Column('salary', css_class='w-full'), Column('currency', css_class='w-full')),
            'subscribe',
            'notifications',
            'department',
            'category',
            'date_time',
        )
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('submit_2', 'Submit 2'))
        self.helper.add_input(Submit('submit_3', 'Submit 3'))


class FormularioVerticalForm(forms.Form):
    """
    Formulario de ejemplo con etiquetas encima de cada campo y dos columnas.
    """

    name = forms.CharField(label='Name', widget=UnfoldAdminTextInputWidget())
    email = forms.EmailField(label='Email', widget=UnfoldAdminTextInputWidget())
    age = forms.IntegerField(label='Age', widget=UnfoldAdminIntegerFieldWidget())
    url = forms.URLField(label='URL', widget=UnfoldAdminURLInputWidget())
    salary = forms.DecimalField(label='Salary', max_digits=12, decimal_places=2, help_text='Enter your salary', widget=UnfoldAdminTextInputWidget())
    currency = forms.ChoiceField(label='Currency', choices=MONEDAS, widget=UnfoldAdminSelectWidget(), initial='EUR')
    priority = forms.ChoiceField(
        label='Priority',
        choices=PRIORIDADES,
        initial='medium',
        help_text='Select the priority of your message',
        widget=UnfoldAdminSelectWidget(),
    )
    options = forms.MultipleChoiceField(
        label='Select Multiple Options',
        choices=OPCIONES,
        help_text='You can select more than one option',
        widget=UnfoldAdminSelectMultipleWidget(),
    )
    subscribe = forms.BooleanField(
        label='Subscribe to newsletter',
        required=False,
        initial=True,
        help_text='Toggle to receive our newsletter with updates and offers',
        widget=UnfoldBooleanSwitchWidget(),
    )
    notifications = forms.BooleanField(
        label='Receive notifications',
        required=False,
        help_text='Toggle to receive notifications about your inquiry status',
        widget=UnfoldBooleanWidget(),
    )
    department = forms.ChoiceField(
        label='Department',
        choices=DEPARTAMENTOS,
        help_text='Select the department to contact',
        widget=UnfoldAdminRadioSelectWidget(),
    )
    category = forms.MultipleChoiceField(
        label='Category',
        choices=CATEGORIAS,
        help_text='Select the category of your message',
        widget=UnfoldAdminCheckboxSelectMultipleWidget(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    Row(Column('name', css_class='w-full'), Column('email', css_class='w-full')),
                    Row(Column('age', css_class='w-full'), Column('url', css_class='w-full')),
                    Row(Column('salary', css_class='w-full'), Column('currency', css_class='w-full')),
                    'priority',
                    'options',
                ),
                Column(
                    'subscribe',
                    'notifications',
                    'department',
                    'category',
                ),
            ),
        )
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('submit_2', 'Submit 2'))
        self.helper.add_input(Submit('submit_3', 'Submit 3'))
