class Response:
    def __init__(self, content='', status='200'):
        self.content = content
        self.status = status
        self.headers = {'Content-Type': 'text/html'}
