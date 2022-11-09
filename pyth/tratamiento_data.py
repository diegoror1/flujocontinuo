#String json_data = "{\"Sesor_id\":\"3E24R\",\"Value\":" + (String)randNumber + "}";

import serial, time, json
import keyboard
import threading
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

hw_sensor = serial.Serial(port='COM3', baudrate=115200, timeout=1, write_timeout=1)
ydata = []
xdata =[]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


if __name__ == '__main__':
    #while True:
    def animate(i,xdata,ydata):
        hw_sensor.write('getValue'.encode('utf-8'))                         # solicita datos a esp32 
        time.sleep(0.1)                                                     # Espera para procesar siguiente dato
        try:                                                                
            raw_string_b = hw_sensor.readline()                             # lee datos enviados por esp32
            raw_string_s = raw_string_b.decode('utf-8')                     # decodifica datos enviados
            if(raw_string_s.index("}")>=0 and raw_string_s.index("{")==0):  # desempaqeutado de datos
                raw_string_s = raw_string_s[0:raw_string_s.index("}")+1]    
                raw_string_j = json.loads(raw_string_s)                     # crea objeto json
                #print(">> ","Presion"," = ",raw_string_j["Value"])          # imprime objeto json
                value= float(raw_string_j["Value"])                         # combierte en flotantee
                ydata.append(value)                                      # agrada a arreglo  
            else:
                print("error/ no } found.")
        except:
            print("Exception occurred, somthing wrong...")
        xdata.append(i)
        ax.clear()
        ax.plot(xdata,ydata)
    if keyboard.is_pressed('ESC'):
        print('se presionó esc!')
        #break
    print("prueba")
    ani = animation.FuncAnimation(fig, animate, fargs = (xdata,ydata))
    print("prueba2")
    plt.show()
    hw_sensor.close()
    data = {'xdata':xdata,
            'presion':ydata
            }
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

