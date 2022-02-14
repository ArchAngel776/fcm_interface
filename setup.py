class Response:

    def print(self):
        print('bar')


class Command:

    def print(self):
        print('foo')

    def response(self):
        return Response()