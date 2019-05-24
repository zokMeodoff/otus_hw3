import os
import re
from response import Response

class App:
    def __init__(self):
        self.urls_handlers = {}

    def __call__(self, env, start_response):
        url = env['PATH_INFO']

        for handler_url in self.urls_handlers:
            match = re.match(handler_url, url)
            if match is not None:
                handler = self.urls_handlers[handler_url]
                break
            else:
                handler = self.not_found_handler

        response = handler(env)

        status_code = response.status
        headers = [(h, response.headers[h]) for h in response.headers]
        start_response(status_code, headers)
        return [response.content.encode('utf-8')]


    def add_url(self, url, handler):
        self.urls_handlers[url] = handler

    @staticmethod
    def not_found_handler(env):
        status = '404'
        content = generate_view('404.html')
        return Response(content, status)


def index_handler(env):
    content = generate_view('index.html')
    return Response(content)


def info_handler(env):
    content = generate_view('info.html')
    return Response(content)


def redirect_handler(env):
    status = '301'
    content = ''
    response = Response(content, status)
    response.headers['location'] = env['PATH_INFO'] + r'/'
    print(h for h in response.headers)
    return response


def generate_view(template_name):
    template_path = os.path.join('templates', template_name)
    if not os.path.exists(template_path):
        return
    with open(template_path, 'r') as template_view:
        template = template_view.read()
    return template


application = App()
application.add_url(r'^/$', index_handler)
application.add_url(r'^/info/$', info_handler)
application.add_url(r'^.*(?<!/)$', redirect_handler)
