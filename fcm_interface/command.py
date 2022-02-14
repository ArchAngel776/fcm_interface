from .response import Response


class Command:

    def print(self):
        print('foo')

    def response(self):
        return Response()
