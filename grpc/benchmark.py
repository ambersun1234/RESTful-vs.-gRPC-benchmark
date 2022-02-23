import grpc
from proto import echo_pb2
from proto import echo_pb2_grpc
import time

if __name__ == "__main__":
    round = 100000
    with grpc.insecure_channel('localhost:6600') as channel:
        stub = echo_pb2_grpc.EchoStub(channel)

        with open("grpc-benchmark.txt", "w") as f:
            for i in range(round):
                start_time = time.perf_counter_ns()
                response = stub.Echo(echo_pb2.EchoRequest(input="2"))
                end_time = time.perf_counter_ns()
                print(end_time - start_time)
                f.write(f"{i + 1} {end_time - start_time}\n")
