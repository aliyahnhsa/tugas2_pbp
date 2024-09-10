from django.shortcuts import render

# Fungsi untuk menampilkan nama aplikasi, nama, dan kelas
def show_main(request):
    context = {
        'appname': 'RandomGames Store App',
        'name': 'Aliyah Nahisa Sugiana',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
