from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Nome",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
        error_messages={'required': 'O nome é obrigatório'}
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
        error_messages={'required': 'O email é obrigatório', 'invalid': 'Por favor, insira um email válido'}
    )
    subject = forms.CharField(
        max_length=200, 
        label="Assunto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto'}),
        error_messages={'required': 'O assunto é obrigatório'}
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem', 'rows': 5}),
        label="Mensagem",
        error_messages={'required': 'A mensagem é obrigatória'}
    )

    # Validação personalizada do campo nome
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('O nome não pode conter números.')
        return name