# RESTful-API vs. gRPC benchmark testing
This gist contains the benchmark testing code of RESTful-API and gRPC

# How to do a benchmark test
There are 2 types of benchmark testing(grpc, rest)
First, start the server
```shell
$ cd ./grpc or cd ./rest
$ go run server.go
```

Then do a benchmark test
```shell
$ cd ./grpc or cd ./rest
$ python3 benchmark.py
```

# Plot
Once you finished with benchmark testing
Just simple run
```shell
$ make plot
```

Then you'll get a benchmark result on project root