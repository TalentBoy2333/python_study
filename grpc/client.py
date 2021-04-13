import grpc 

import hello_pb2 as pb2
import hello_pb2_grpc as pb2_grpc 

def main(): 
    conn = grpc.insecure_channel('0.0.0.0:5000')
    client = pb2_grpc.BilibiliStub(channel=conn)
    resp = client.Hello(
        pb2.HelloReq(
            name='jljy', 
            age=33, 
        )
    )
    print(resp.result)


if __name__ == '__main__': 
    main() 