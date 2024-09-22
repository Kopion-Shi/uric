import json


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 在请求处理前执行的代码

        response = self.get_response(request)
        # 在响应返回后执行的代码
        if request.path_info == '/users/login' or request.path_info == '/users/logout':
            return response
        if hasattr(response, 'data'):
            response.data = {
                'code': 20000 if response.status_code == 200 else 20001,
                'data': response.data
            }
            new_content = json.dumps(response.data).encode()
            response.content = new_content


        return response
