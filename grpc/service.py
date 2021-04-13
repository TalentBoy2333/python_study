import grpc 
import time 

from concurrent import futures

import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc 

class Bilibili(pb2_grpc.BilibiliServicer): 
    def Hello(self, request, context): 
        name = request.name 
        age = request.age 

        result = f'my name is {name}, age is {age}'
        return pb2.HelloReply(result=result)

def run(): 
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_BilibiliServicer_to_server(Bilibili(), grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    grpc_server.start() 
    print('server start at 0.0.0.0:5000')

    try: 
        while True:
            time.sleep(3600) 
    except KeyboardInterrupt: 
        grpc_server.stop(0)

if __name__ == '__main__': 
    run()
