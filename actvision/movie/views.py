from django.shortcuts import render
import os
user_id = "./new_folder SSIbafaefaaeffefafeafawefeafefeafaaal"

# Create your views here.
def movie(request):
    return render(request,'mov.html')

def make_folder(request):
    print("--------시작------------")
    create_Directory(user_id)
    print("--------종료------------")
    return render(request,'mov.html')

def create_Directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            f = open("temp", 'w', encoding="UTF-8-sig")
            f.close()
    except :
        pass