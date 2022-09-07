import json

from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import *
from capstoneApp.serializers import UserinfoSerializer


def index():
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")



@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        if userinfo.objects.filter(userid = data['userid']).exists():
            obj = userinfo.objects.get(userid = data['userid'])
            if obj.password == data['password']:
                return JsonResponse({'code': '0000', 'msg': '로그인 성공'}, status=200)
            else:
                return JsonResponse({'code': '0001', 'msg': '비밀번호 불일치'}, status=200)
        else:
            return JsonResponse({'code': '0002', 'msg': '아이디가 존재하지 않음'}, status=200)
    else:
        return JsonResponse({'code': '0003', 'msg': '통신이 원할하지않습니다.'}, status=500)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if userinfo.objects.filter(userid=data['userid']).exists():
            return JsonResponse({'code': '0000', 'msg': '이미 등록된 아이디가 있습니다.'}, status=200)
        elif len(data['password']) < 6:
            return JsonResponse({'code': '0001', 'msg': '비밀번호를 6자 이상으로 설정해주세요.'}, status=200)
        else:
            serializer = UserinfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'code': '0002', 'msg': '회원가입에 성공하였습니다.'}, status=200)
    else:
        return JsonResponse({'code': '1231', 'msg': '포스트로 보낵라...'}, status=500)



#이미지에서 가져온 text들 json으로 받아와서 모듈 적용시키는 곳
@csrf_exempt
def textrunning(request):
    if request.method == 'POST':
        # data = JSONParser().parse(request)
        data = json.loads(request)
        path = 'ml/dataset/testdata/testdata.json'

        with open(path, 'w', encoding="UTF-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        subprocess.run('python ml/predict_0704.py ml/dataset/testdata/testdata.json', shell=True)

        item_list.object.create(item_name='predict_data/predict_list(*).json'["food_name"])

        serializer = Item_ListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({'code': '0000', "msg": '보내짐'}, status=200)
    else:
        return JsonResponse({"msg": 'connection fail'}, status=500)






#@csrf_exempt
#def insert_item(request):
 #   if request.method == 'POST':
  #      data = JSONParser().parse(request)
   #     if