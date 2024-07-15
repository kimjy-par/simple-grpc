import grpc
import hello_pb2_grpc as pb2_grpc
import hello_pb2 as pb2


class HelloClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.HelloStub(self.channel)

    def get_url(self, message):
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = HelloClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')