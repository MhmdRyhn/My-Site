# https://stackoverflow.com/questions/48879661/confused-by-middleware-execution-process-django


class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # do stuff with request
        self.process_request(request)

        response = self.get_response(request)

        # do stuff with request and/or response

        return response

    def process_request(self, request):
        setattr(request, 'myname', 'Rayhan')
