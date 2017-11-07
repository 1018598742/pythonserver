#!/usr/bin/env python3
# _*_ coding = utf-8 _*_
from www.apis import APIValueError
from www.coroweb import get, post
from www.models import Runoob


'''
json 输出：
{
    infos: [
        {
            runoob_id: 2,
            runoob_title: "python教程",
            runoob_author: "菜鸟教程和慕课网",
            submission_date: "2017-10-28"
        },
        {
            runoob_id: 3,
            runoob_title: "学习mysql",
            runoob_author: "网络学习",
            submission_date: "2017-10-28"
        },
        {
            runoob_id: 4,
            runoob_title: "andRoid",
            runoob_author: "android",
            submission_date: "2017-10-28"
        }
    ]
}
'''


@get('/api')
def get_api():
    infos = yield from Runoob.findAll()
    '''
    print('api_info:',infos)
    输出：
    api_info: [{'runoob_id': 2, 'runoob_title': 'python教程', 'runoob_author': '菜鸟教程和慕课网',
                'submission_date': datetime.date(2017, 10, 28)},
               {'runoob_id': 3, 'runoob_title': '学习mysql', 'runoob_author': '网络学习',
                'submission_date': datetime.date(2017, 10, 28)},
               {'runoob_id': 4, 'runoob_title': 'andRoid', 'runoob_author': 'android',
                'submission_date': datetime.date(2017, 10, 28)}]
    '''
    return dict(infos=infos)


'''
json 输出：
    {
        use: {
            name: "fta",
            age: 12
        }
    }
    
json 错误输出：
    {
        error: "value:invalid",
        data: "nameerror",
        message: ""
    }
'''
@get('/a')
def get_a():
    error = ''
    if error:
        infos = {'name': 'fta', 'age': 12}
        return dict(use=infos)
    else:
        raise APIValueError('nameerror',message='test error')

'''
使用命名关键字参数
'''
@post('/p')
def post_p(*,id,request):

    infos = {'name': 'fta', 'age': 12}
    return dict(use=infos)


