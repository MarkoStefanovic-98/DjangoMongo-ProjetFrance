from django.forms import ModelForm
from .models import Hopital, Scolaire, Agriculture
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class hopitalForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(hopitalForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
		self.helper.form_method = 'POST'

	class Meta:
		model = Hopital
		fields = ['titre', 'description']

class scolaireForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(scolaireForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
		self.helper.form_method = 'POST'

	class Meta:
		model = Scolaire
		fields = ['titre', 'description']

class agricultureForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(agricultureForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
		self.helper.form_method = 'POST'

	class Meta:
		model = Agriculture
		fields = ['titre', 'description']