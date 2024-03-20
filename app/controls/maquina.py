import socket
import pyautogui
import pickle



def app():
    # Instanciamos el objeto socket
    mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mi_socket.bind(('0.0.0.0', 12345))

    mi_socket.listen(5)
    
    conn, addr = mi_socket.accept()
    # print("Se agrego tiempo", addr)


    while True:
       
        response = conn.recv(4096)

        if response:
            data = pickle.loads(response)
            if len(data) > 0:

                with open('config/horas.txt', 'w') as file_horas:
                    file_horas.write(data[0])
                with open('config/minutos.txt', 'w') as file_minutos:
                    file_minutos.write(data[1])
                pyautogui.press('5')
                break
            else:
                pyautogui.press('0')
            
                break



        

            conn.close()
app()
on=True
while on:
    
    app()