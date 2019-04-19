from flask import Flask, jsonify, abort
from flask import make_response
from flask import request

app = Flask(__name__)

tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]

@app.route("/")
def hello():
    return "Hello World!"




@app.route('/api/v1/activity', methods=['GET'])
def get_activities():
    activities = {

        "message": {

                "status": 200

        },

        "result": {

                "event_name": "流行精選 Popular Selection",

                "event_items": [{

                                "active_id": "1",

                                "title": "復興館B1 【雅詩蘭黛粉嫩慾望美唇修護系列】新品登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19040110401686",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040110474008001.jpg"

                        },

                        {

                                "active_id": "2",

                                "title": "復興館7F Samsonite BAG STORE-AMERICAN TOURISTER Modern Dream系列新品登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041513541227",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041502050046301.jpg"

                        },

                        {

                                "active_id": "3",

                                "title": "復興館6F ASICS Onitsuka Tiger MEXICO 66 SLIP-ON 春夏新品登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041615491132",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041604035483601.jpg"

                        },

                        {

                                "active_id": "4",

                                "title": "復興館3F HOGAN專櫃2019春夏男士系列",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041617153674",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041605392679801.jpg"

                        },

                        {

                                "active_id": "5",

                                "title": "復興館7F TANI日系內著春夏新品",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041712100200",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041712143591311.jpg"

                        },

                        {

                                "active_id": "6",

                                "title": "復興館6F ASICS GEL-QUANTUM INFINITY 指定門市限量登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041616364657",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041604530746601.jpg"

                        },

                        {

                                "active_id": "7",

                                "title": "復興館B1 SWAROVSKI夏季新品推廣",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041511434182",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041501341681611.jpg"

                        },

                        {

                                "active_id": "8",

                                "title": "復興館6F ASICS Onitsuka Tiger復活節配色登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041616230909",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041604280890601.jpg"

                        },

                        {

                                "active_id": "9",

                                "title": "復興館5F NUDE 2019絲柔光璨 快閃SOGO",

                                "url": "https://www.sogo.com.tw/tp2/popular/19040813211943",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040801253533501.jpg"

                        },

                        {

                                "active_id": "10",

                                "title": "復興館5F izzue 2019春季男裝系列",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041117063984",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041105124863911.jpg"

                        },

                        {

                                "active_id": "11",

                                "title": "復興館B1 PANDORA 漫漫桃花Peach Blossom系列珠寶",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041510464670",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041510511905701.jpg"

                        },

                        {

                                "active_id": "12",

                                "title": "復興館5F izzue 2019春季女裝系列",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041117270093",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041105315956701.jpg"

                        },

                        {

                                "active_id": "13",

                                "title": "復興館6F New Balance 890 v7進化輕量登場！",

                                "url": "https://www.sogo.com.tw/tp2/popular/19040318154973",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040306184673401.jpg"

                        },

                        {

                                "active_id": "14",

                                "title": "New Balance 無所不型，由我定義。經典數字潮鞋再推新作574S v2 全新登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19040411255624",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040411253789901.jpg"

                        },

                        {

                                "active_id": "15",

                                "title": "復興館6F ASICS Onitsuka Tiger x Kanta & Kaede 4/2聯名登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19040115072535",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040103173208911.jpg"

                        },

                        {

                                "active_id": "16",

                                "title": "YSL新品登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19032913330156",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040103173208911.jpg"

                        },

                        {

                                "active_id": "17",

                                "title": "10/10HOPE新品登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19032914483412",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19032902452558301.jpg"

                        },

                        {

                                "active_id": "18",

                                "title": "復興館6F PUMA X BARBIE 粉嫩時尚單品耀眼登台",

                                "url": "https://www.sogo.com.tw/tp2/popular/19040115353154",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19040103400058901.jpg"

                        },

                        {

                                "active_id": "19",

                                "title": "復興館6F TRAVELER Spring Summer 2019 collection",

                                "url": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19032212221440601.jpg",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19032212221440601.jpg"

                        },

                        {

                                "active_id": "20",

                                "title": "復興館5F 杏桃鬆餅屋 5月季節料理亮麗登場",

                                "url": "https://www.sogo.com.tw/tp2/popular/19041510154878",

                                "thumbnail": "https://photo.sogo.com.tw/Content/Upload/images/_upload/19041510195658811.jpg"

                        }

                ]}
        }
    return jsonify(activities)









@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})







# 吃參數
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})



#統一 error response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# post
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201




@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

