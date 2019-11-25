from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label ='Nombre' , required = True , widget = forms.TextInput( attrs ={'class':'form-control','placeholder':'Nombre'}))
    correo = forms.EmailField(label ='Correo ' , required = True,widget = forms.EmailInput( attrs ={'class':'form-control','placeholder':'Correo'}))
    telefono = forms.IntegerField(label ='Telefono' , required = True , widget = forms.NumberInput( attrs ={'class':'form-control','placeholder':'Telefono'}))
    mensaje = forms.CharField(label ='Mensaje' , required = True, widget = forms.Textarea( attrs ={'class':'form-control','rows':4,'placeholder':'Escribe tu mensaje...'}))