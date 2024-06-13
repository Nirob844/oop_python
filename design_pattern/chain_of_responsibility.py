from abc import ABC, abstractmethod


class Handler(ABC):
    """Handler Interface"""
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

class LowLevelSupport(Handler):
    """Concrete Handler for Low-Level Support"""
    def handle_request(self, request):
        if request == 'low':
            print("LowLevelSupport: Handling low-level request")
        elif self._successor is not None:
            self._successor.handle_request(request)

class MidLevelSupport(Handler):
    """Concrete Handler for Mid-Level Support"""
    def handle_request(self, request):
        if request == 'mid':
            print("MidLevelSupport: Handling mid-level request")
        elif self._successor is not None:
            self._successor.handle_request(request)

class HighLevelSupport(Handler):
    """Concrete Handler for High-Level Support"""
    def handle_request(self, request):
        if request == 'high':
            print("HighLevelSupport: Handling high-level request")
        elif self._successor is not None:
            self._successor.handle_request(request)

# Client Code
low_level = LowLevelSupport()
mid_level = MidLevelSupport(low_level)
high_level = HighLevelSupport(mid_level)

# Handling Requests
print("Sending 'low' request:")
high_level.handle_request('low')
# Output: LowLevelSupport: Handling low-level request

print("\nSending 'mid' request:")
high_level.handle_request('mid')
# Output: MidLevelSupport: Handling mid-level request

print("\nSending 'high' request:")
high_level.handle_request('high')
# Output: HighLevelSupport: Handling high-level request

print("\nSending 'unknown' request:")
high_level.handle_request('unknown')
# No output since no handler for 'unknown'
