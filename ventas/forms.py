from django import forms
from ventas.models import Venta
class VentaForm(forms.ModelForm):
	class Meta:
		model=Venta
		fields=['nombre']
		labels={'Nombre':'Nombre de la venta'}
		widget={'Nombre':forms.TextInput()}
		
	def __init__(self,*args,**kwargs):
		super().__init__ (*args,**kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class':'form-control'
			})
			
			