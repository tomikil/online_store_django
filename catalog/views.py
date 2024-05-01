from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('catalog/data/contacts.txt', 'a', encoding="UTF-8") as file:
            file.writelines(f"{name} ({phone}): {message}\n")
        print(f"{name} ({phone}): {message}")
    return render(request, 'contacts.html')
