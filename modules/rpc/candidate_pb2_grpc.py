# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import modules.rpc.candidate_pb2 as candidate__pb2


class CandidateStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateCandidate = channel.unary_unary(
        '/Candidate/CreateCandidate',
        request_serializer=candidate__pb2.CreateCandidateRequest.SerializeToString,
        response_deserializer=candidate__pb2.CreateCandidateResponse.FromString,
        )
    self.GetCandidate = channel.unary_unary(
        '/Candidate/GetCandidate',
        request_serializer=candidate__pb2.GetCandidateRequest.SerializeToString,
        response_deserializer=candidate__pb2.GetCandidateResponse.FromString,
        )
    self.UpdateCandidate = channel.unary_unary(
        '/Candidate/UpdateCandidate',
        request_serializer=candidate__pb2.UpdateCandidateRequest.SerializeToString,
        response_deserializer=candidate__pb2.UpdateCandidateResponse.FromString,
        )
    self.RemoveCandidate = channel.unary_unary(
        '/Candidate/RemoveCandidate',
        request_serializer=candidate__pb2.RemoveCandidateRequest.SerializeToString,
        response_deserializer=candidate__pb2.RemoveCandidateResponse.FromString,
        )
    self.GetCandidates = channel.unary_unary(
        '/Candidate/GetCandidates',
        request_serializer=candidate__pb2.GetCandidatesRequest.SerializeToString,
        response_deserializer=candidate__pb2.GetCandidatesResponse.FromString,
        )
    self.CastVote = channel.unary_unary(
        '/Candidate/CastVote',
        request_serializer=candidate__pb2.CastVoteRequest.SerializeToString,
        response_deserializer=candidate__pb2.CastVoteResponse.FromString,
        )
    self.CountVote = channel.unary_unary(
        '/Candidate/CountVote',
        request_serializer=candidate__pb2.CountVoteRequest.SerializeToString,
        response_deserializer=candidate__pb2.CountVoteResponse.FromString,
        )


class CandidateServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateCandidate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCandidate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateCandidate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveCandidate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCandidates(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CastVote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CountVote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CandidateServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateCandidate': grpc.unary_unary_rpc_method_handler(
          servicer.CreateCandidate,
          request_deserializer=candidate__pb2.CreateCandidateRequest.FromString,
          response_serializer=candidate__pb2.CreateCandidateResponse.SerializeToString,
      ),
      'GetCandidate': grpc.unary_unary_rpc_method_handler(
          servicer.GetCandidate,
          request_deserializer=candidate__pb2.GetCandidateRequest.FromString,
          response_serializer=candidate__pb2.GetCandidateResponse.SerializeToString,
      ),
      'UpdateCandidate': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateCandidate,
          request_deserializer=candidate__pb2.UpdateCandidateRequest.FromString,
          response_serializer=candidate__pb2.UpdateCandidateResponse.SerializeToString,
      ),
      'RemoveCandidate': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveCandidate,
          request_deserializer=candidate__pb2.RemoveCandidateRequest.FromString,
          response_serializer=candidate__pb2.RemoveCandidateResponse.SerializeToString,
      ),
      'GetCandidates': grpc.unary_unary_rpc_method_handler(
          servicer.GetCandidates,
          request_deserializer=candidate__pb2.GetCandidatesRequest.FromString,
          response_serializer=candidate__pb2.GetCandidatesResponse.SerializeToString,
      ),
      'CastVote': grpc.unary_unary_rpc_method_handler(
          servicer.CastVote,
          request_deserializer=candidate__pb2.CastVoteRequest.FromString,
          response_serializer=candidate__pb2.CastVoteResponse.SerializeToString,
      ),
      'CountVote': grpc.unary_unary_rpc_method_handler(
          servicer.CountVote,
          request_deserializer=candidate__pb2.CountVoteRequest.FromString,
          response_serializer=candidate__pb2.CountVoteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Candidate', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
