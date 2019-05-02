clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	
proto:
	python -m grpc_tools.protoc -I protos/ --python_out=modules/rpc/ --grpc_python_out=modules/rpc protos/*.proto