from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from settings.update_json import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# Create your views here.

def imgn(request):
    return render(request,'image.html')


@csrf_exempt
def upload_img(request):
    print("호출 성공")
    if request.method == 'POST':
        if request.is_ajax():
            img = request.FILES.get('chooseFile')  # 이미지를 request에서 받아옴
            path = default_storage.save(user_id +"/img.jpg", ContentFile(img.read()))
            now_kst = time_now()
            UPLOAD("ynu-mcl-act", user_id + "/img.jpg", user_id + "/MEDIA" + now_kst.strftime("/%Y%m%d%H%M%S"))
            os.remove(user_id+"/img.jpg") # 장고에서 중복된 이름의 파일에는 임의로 이름을 변경하기 때문에 임시파일은 제거
            return redirect('image.html')
    else:
        print("POST 호출 실패!")
        return redirect('image.html')

@csrf_exempt
def save_letter(request): # 문자 설정 -> 확인 버튼 눌렀을 시
    if request != "":
        print("========= 시작 ===========")
        print("요청 방식 = " + request.method)

        change = value_of_request_body_list(request.body)  # change 배열은 현재 임시방편 인터페이스 마저 완성되면 인덱스 값 다 바뀔 예정
        data = make_Timetable()

        now_kst = time_now_local()  # 현재시간 받아옴
        now_kst1 = time_now()
        now_kst += 5

        data["5"]["detail_info"]["x"] = str(change[0])
        data["5"]["detail_info"]["y"] = str(change[1])
        data["5"]["detail_info"]["width"] = str(change[2])
        data["5"]["detail_info"]["height"] = str(change[3])
        #data["5"]["detail_info"]["scroll_fix"] =
        data["5"]["detail_info"]["play_speed"] = str(change[4])
        data["5"]["detail_info"]["play_count"] = str(change[5])
        #data["5"]["detail_info"]["play_second"] =
        #data["5"]["detail_info"]["font_size"] = str(change[6])
        data["5"]["detail_info"]["font_size"] = "64"     # 폰트사이즈 - 인터페이스 수정 전까지 고정시킴

        data["5"]["title"] = "지준영"

        data["5"]["time"]["year"] = str(time.localtime(now_kst).tm_year)
        data["5"]["time"]["month"] = str(time.localtime(now_kst).tm_mon)
        data["5"]["time"]["day"] = str(time.localtime(now_kst).tm_mday)
        data["5"]["time"]["hour"] = str(time.localtime(now_kst).tm_hour)
        data["5"]["time"]["minute"] = str(time.localtime(now_kst).tm_min)
        data["5"]["time"]["second"] = str(time.localtime(now_kst).tm_sec)

        createDirectory(user_id)
        save_file(data)
        #UPLOAD(user_id, user_id + "/send", "JSON/TIMETABLE" + now_kst1.strftime("/%Y%m%d%H%M%S"))

        print("========= 종료 ===========")
        return redirect('image.html')
    else:
        return redirect('image.html')



def make_Timetable():
    now_kst = time_now()  # 현재시간 받아옴

    data = dict()
    # 1
    video_play = dict()
    video_play_time = dict()
    video_play["time"] = video_play_time
    video_play_time["year"] = str(now_kst.strftime("%Y"))
    video_play_time["month"] = str(now_kst.strftime("%m"))
    video_play_time["day"] = str(now_kst.strftime("%d"))
    video_play_time["hour"] = str(now_kst.strftime("%H"))
    video_play_time["minute"] = str(now_kst.strftime("%M"))
    video_play_time["second"] = str(now_kst.strftime("%S"))
    video_play["type"] = "video"
    video_play["action"] = "play"
    video_play["title"] = ["",""]
    data["1"] = video_play

    # 2
    video_stop = dict()
    video_stop_time = dict()
    video_stop["time"] = video_stop_time
    video_stop_time["year"] = str(now_kst.strftime("%Y"))
    video_stop_time["month"] = str(now_kst.strftime("%m"))
    video_stop_time["day"] = str(now_kst.strftime("%d"))
    video_stop_time["hour"] = str(now_kst.strftime("%H"))
    video_stop_time["minute"] = str(now_kst.strftime("%M"))
    video_stop_time["second"] = str(now_kst.strftime("%S"))
    video_stop["type"] = "video"
    video_stop["action"] = "stop"
    video_stop["title"] = ""
    data["2"] = video_stop

    # 3
    img_play = dict()
    img_play_time = dict()
    img_play["time"] = img_play_time
    img_play_time["year"] = str(now_kst.strftime("%Y"))
    img_play_time["month"] = str(now_kst.strftime("%m"))
    img_play_time["day"] = str(now_kst.strftime("%d"))
    img_play_time["hour"] = str(now_kst.strftime("%H"))
    img_play_time["minute"] = str(now_kst.strftime("%M"))
    img_play_time["second"] = str(now_kst.strftime("%S"))
    img_play["type"] = "image"
    img_play["action"] = "play"
    img_play["title"] = ""
    data["3"] = img_play

    # 4
    img_stop = dict()
    img_stop_time = dict()
    img_stop["time"] = img_stop_time
    img_stop_time["year"] = str(now_kst.strftime("%Y"))
    img_stop_time["month"] = str(now_kst.strftime("%m"))
    img_stop_time["day"] = str(now_kst.strftime("%d"))
    img_stop_time["hour"] = str(now_kst.strftime("%H"))
    img_stop_time["minute"] = str(now_kst.strftime("%M"))
    img_stop_time["second"] = str(now_kst.strftime("%S"))
    img_stop["type"] = "image"
    img_stop["action"] = "stop"
    img_stop["title"] = ""
    data["4"] = img_stop

    # 5
    text_play = dict()
    text_play_time = dict()
    detail_info = dict()
    text_play["time"] = text_play_time
    text_play["detail_info"] = detail_info
    text_play_time["year"] = str(now_kst.strftime("%Y"))
    text_play_time["month"] = str(now_kst.strftime("%m"))
    text_play_time["day"] = str(now_kst.strftime("%d"))
    text_play_time["hour"] = str(now_kst.strftime("%H"))
    text_play_time["minute"] = str(now_kst.strftime("%M"))
    text_play_time["second"] = str(now_kst.strftime("%S"))
    text_play["type"] = "string"
    text_play["action"] = "play"
    text_play["title"] = "안녕하세요"
    detail_info["x"] = "0"
    detail_info["y"] = "0"
    detail_info["width"] = "0"
    detail_info["height"] = "0"
    detail_info["scroll_fix"] = "0"
    detail_info["play_speed"] = "0"
    detail_info["play_count"] = "0"
    detail_info["play_second"] = "0"
    detail_info["font_name"] = "NotoSansCJK-Regular.ttc"
    detail_info["font_size"] = "64"
    detail_info["thickness_italics"] = "0"
    detail_info["red_green_blue"] = ["0","0","0"]
    data["5"] = text_play

    # 6
    text_stop = dict()
    text_stop_time = dict()
    text_stop["time"] = text_stop_time
    text_stop_time["year"] = str(now_kst.strftime("%Y"))
    text_stop_time["month"] = str(now_kst.strftime("%m"))
    text_stop_time["day"] = str(now_kst.strftime("%d"))
    text_stop_time["hour"] = str(now_kst.strftime("%H"))
    text_stop_time["minute"] = str(now_kst.strftime("%M"))
    text_stop_time["second"] = str(now_kst.strftime("%S"))
    text_stop["type"] = "string"
    text_stop["action"] = "stop"
    data["6"] = text_stop

    return data