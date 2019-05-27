from app import App, generate_view
from response import Response


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
    return response


application = App()
application.add_url(r'^/$', index_handler)
application.add_url(r'^/info/$', info_handler)
application.add_url(r'^.*(?<!/)$', redirect_handler)