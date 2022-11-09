 #String json_data = "{\"Sesor_id\":\"3E24R\",\"Value\":" + (String)randNumber + "}";

import serial, time, json
import keyboard
hw_sensor = serial.Serial(port='COM3', baudrate=115200, timeout=1, write_timeout=1)
data = []
if __name__ == '__main__':
    while True:
        hw_sensor.write('getValue'.encode('utf-8'))
        time.sleep(0.1)
        try:
            raw_string_b = hw_sensor.readline()
            raw_string_s = raw_string_b.decode('utf-8')
            if(raw_string_s.index("}")>=0 and raw_string_s.index("{")==0):
                raw_string_s = raw_string_s[0:raw_string_s.index("}")+1]
                raw_string_j = json.loads(raw_string_s)
                print(">> ",raw_string_j["Sensor_id"]," = ",raw_string_j["Value"])
                value= float(raw_string_j["Value"])
                data.append(value)
                if keyboard.is_pressed('p'):
                    print('se presionó [p]arar!')
                    break  
            else:
                print("error/ no } found.")
        except:
            print("Exception occurred, somthing wrong...")
    hw_sensor.close()
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)