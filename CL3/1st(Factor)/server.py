import grpc
import factorial_pb2
import factorial_pb2_grpc

class FactorialServicer(factorial_pb2_grpc.FactorialServiceServicer):
	def Calculate(self, request, context):
		n = request.n
		if n < 0:
			context.abort(grpc.status_code.INVALID_ARGUMENT, "n must be non-negative")
			factorial = 1
			for i in range(2, n + 1):
				factorial *= i
			return factorial_pb2.FactorialResponse(factorial=factorial)
	def serve():
		server = grpc.server(concurrent=4)
		factorial_pb2_grpc.add_FactorialServiceServicer_to_server(FactorialServicer(), server)
		server.add_insecure_port("[::]:50051") # Replace with your desired port
		server.start()
		server.wait_for_termination()