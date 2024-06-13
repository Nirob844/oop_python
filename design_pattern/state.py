from abc import ABC, abstractmethod


# Context
class TCPConnection:
    def __init__(self):
        self._state = ClosedState()

    def change_state(self, state):
        print(f"TCPConnection: Changing state to {type(state).__name__}")
        self._state = state

    def open_connection(self):
        self._state.open_connection(self)

    def close_connection(self):
        self._state.close_connection(self)

    def acknowledge(self):
        self._state.acknowledge(self)

# State
class ConnectionState(ABC):
    @abstractmethod
    def open_connection(self, connection):
        pass

    @abstractmethod
    def close_connection(self, connection):
        pass

    @abstractmethod
    def acknowledge(self, connection):
        pass

# Concrete States
class ClosedState(ConnectionState):
    def open_connection(self, connection):
        print("Opening connection")
        connection.change_state(EstablishedState())

    def close_connection(self, connection):
        print("Connection is already closed")

    def acknowledge(self, connection):
        print("Cannot acknowledge, connection is closed")

class EstablishedState(ConnectionState):
    def open_connection(self, connection):
        print("Connection is already established")

    def close_connection(self, connection):
        print("Closing connection")
        connection.change_state(ClosedState())

    def acknowledge(self, connection):
        print("Acknowledging data")

# Usage
tcp_connection = TCPConnection()

tcp_connection.open_connection()
tcp_connection.acknowledge()

tcp_connection.close_connection()
tcp_connection.acknowledge()

tcp_connection.close_connection()
# Output:
# TCPConnection: Changing state to EstablishedState
# Opening connection
# Acknowledging data
# TCPConnection: Changing state to ClosedState
# Closing connection
# Cannot acknowledge, connection is closed
# Connection is already closed
