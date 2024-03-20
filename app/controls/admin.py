import socket
import pickle
import ping3

PORT = 12345


class ControlMachines:
    def __init__(self, ip, time):
        self.ip = ip
        self.time = time

    def ping_machine(self):
        machine = ping3.ping(self.ip, timeout=0.29)
        return machine

    # Conecta con el receptor
    def add_time_machine(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.settimeout(2)
                client_socket.connect((self.ip, PORT))
                send_date = pickle.dumps(self.time)
                # Envía la solicitud para pulsar la tecla '5'
                client_socket.sendall(send_date)
                return True
        except socket.timeout as time:
            return 'timeout'
        except ConnectionRefusedError:
            return 'connect'
        finally:
            client_socket.close()
