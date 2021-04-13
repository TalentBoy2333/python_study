## note

### 通过 proto 文件生成
```
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto
```