import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Goal, Work


@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        if user_exist(request):
            return JsonResponse({"Result": False})
        else:
            data = json.loads(request_bytes_to_json(request))
            user = User()
            user.create(data['user_id'], data['password'], data['name'])
            return JsonResponse({"Result": True})


@csrf_exempt
def user_read(request):
    data = json.loads(request_bytes_to_json(request))
    if User().is_exist(data['user_id']) and request.method == 'POST':
        user = User()
        user_data = user.read(data['user_id'])
        return JsonResponse({"Result": True,
                             "user_id": user_data.user_id,
                             "password": user_data.password,
                             "name": user_data.name})
    return JsonResponse({"Result": False})


@csrf_exempt
def user_update(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and User().is_exist(data['user_id']):
        user = User()
        user.update(data['user_id'], data['password'], data['name'])
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def user_delete(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and User().is_exist(data['user_id']):
        user = User()
        user.dele(data['user_id'])
        del request.session['user_id']
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def user_exist(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and User().is_exist(data['user_id']):
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def goal_create(request):
    if request.method == 'POST':
        data = json.loads(request_bytes_to_json(request))
        goal = Goal()
        try:
            print(data['complete_day'])
        except KeyError:
            data['complete_day'] = 0
        goal.create(data['user_id'],
                    data['name'],
                    data['iteration_type'],
                    data['frequency'],
                    data['object_time'],
                    data['complete_day'])

        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def goal_read(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Goal().is_exist(data['user_id'], data['name']):
        goal = Goal()
        goal_data = goal.read(data['user_id'], data['name'])
        return JsonResponse({"Result": True,
                             "user_id": goal_data.user_id.user_id,
                             "name": goal_data.name,
                             "iteration_type": goal_data.iteration_type,
                             "frequency": goal_data.frequency,
                             "object_time": goal_data.object_time,
                             "complete_day": goal_data.complete_day,
                             "start_day": goal_data.start_day})
    return JsonResponse({"Result": False})


@csrf_exempt
def goal_list_read(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and User().is_exist(data['user_id']):
        goal = Goal()
        goal_data = goal.filter(data['user_id'])
        return JsonResponse({"Result": True,
                             "user_id": goal_data.user_id.user_id,
                             "name": goal_data.name,
                             "iteration_type": goal_data.iteration_type,
                             "frequency": goal_data.frequency,
                             "object_time": goal_data.object_time,
                             "complete_day": goal_data.complete_day,
                             "start_day": goal_data.start_day})
    return JsonResponse({"Result": False})


@csrf_exempt
def goal_update(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Goal().is_exist(data['user_id'], data['name']):
        goal = Goal()
        goal.update(data['user_id'], data['prev_name'], data['name'], data['iteration_type'],
                    data['frequency'], data['object_time'], data['complete_day'])
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def goal_delete(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Goal().is_exist(data['user_id'], data['name']):
        goal = Goal()
        goal.dele(data['user_id'], data['prev_name'])
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def goal_exist(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Goal().is_exist(data['user_id'], data['name']):
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def work_create(request):
    if request.method == 'POST':
        data = json.loads(request_bytes_to_json(request))
        work = Work()
        try:
            print(data['complete_time'])
        except KeyError:
            data['complete_time'] = 0
        work.create(data['user_id'], data['name'], data['date'], data['complete_time'])
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def work_read(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Work().is_exist(data['user_id'], data['name'], data['date']):
        work = Work()
        work_data = work.read(data['user_id'], data['name'], data['date'])
        return JsonResponse({"Result": True,
                             "user_id": work_data.user_id.user_id,
                             "name": work_data.name.name,
                             "date": work_data.date,
                             "complete_time": work_data.complete_time})
    return JsonResponse({"Result": False})


@csrf_exempt
def work_list_read(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Goal().is_exist(data['user_id'], data['name']):
        work = Work()
        work_data = work.filter(user_id=data['user_id'], name=data['name'])
        work_list = dict()
        for work_i in work_data:
            work_list[str(work_i.date)] = work_i.complete_time
        return JsonResponse({"Result": True,
                             'work_list': json.dumps(work_list)})
    return JsonResponse({"Result": False})


@csrf_exempt
def work_update(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Work().is_exist(data['user_id'], data['name'], data['date']):
        work = Work()
        work.update(user_id=data['user_id'],
                    name=data['name'],
                    date=data['date'],
                    complete_time=data['complete_time'])
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def work_delete(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Work().is_exist(data['user_id'], data['name'], data['date']):
        work = Work()
        work.dele(data['user_id'], data['name'], data['date'])
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


@csrf_exempt
def work_exist(request):
    data = json.loads(request_bytes_to_json(request))
    if request.method == 'POST' and Work().is_exist(data['user_id'], data['name'], data['date']):
        return JsonResponse({"Result": True})
    return JsonResponse({"Result": False})


"""
request:param
parse information from bytes to json
POST로 부를 때랑 web에서 부를 때랑 리턴하는 bytes값이 달라서 그 부분 다르게 처리
ex)
POST: b'{\n  "user_id": "davkim"\n\t,"name": "work out"\n}'
WEB: b'csrfmiddlewaretoken=2athveO3rdBySDxcNWmzEHFlbSSICB5S9aqf7rgtXjXstm9XHNNyycB7Ctf55C3X&user_id=davkim&name=work+out'
"""
def request_bytes_to_json(request):
    dic = dict()
    str_arr = str(request.body)
    # WEB 부분 처리
    if str_arr.__contains__('='):
        str_arr = str(request.body)[2:-1]\
            .replace('+', ' ').split('&')
    # POST 부분 처리
    else:
        str_arr = str_arr[2:-1]\
            .replace('\\n', '').replace('\\t', '')\
            .replace('{', '').replace('}', '')\
            .replace(': ', '=').replace('  ', '') \
            .replace('"', '').split(',')

    for i in range(len(str_arr)):
        dic[str_arr[i].split('=')[0]] = str_arr[i].split('=')[1]

    return json.dumps(dic)


def bytes_to_dict(bytes_in):
    dic = dict()
    str_arr = str(bytes_in)[3:-2] \
        .replace(' "', '').replace(': ', ':').replace('"', '').split(',')

    for i in range(len(str_arr)):
        dic[str_arr[i].split(':')[0]] = str_arr[i].split(':')[1]

    print(dic)
    return dic
