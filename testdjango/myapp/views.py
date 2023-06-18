from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def user_model(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        new_email = request.POST.get('new_email')
        new_password = request.POST.get('new_password')
        
        
        User = get_user_model()
        user = get_object_or_404(User, email=email)

        # Modificar el correo electrónico y/o la contraseña
        if new_email:
            user.email = new_email
        if new_password:
            user.set_password(new_password)

        user.save()

        return JsonResponse({'message': 'Usuario modificado exitosamente.'})

    return JsonResponse({'error': 'Método no permitido.'})


def home (request):
    return render(request, 'register.html')