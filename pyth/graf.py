import serial 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arduinoSerialData = serial.Serial("COM3", 9600 , timeout=1)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xdatos = []
ydatos = []

while True:
    if (arduinoSerialData.inWaiting()>0):
        def animate(i,xdatos,ydatos):
            datos = arduinoSerialData.readline()
            datos = float (datos)
            print(datos)
            xdatos.append(i)
            ydatos.append(datos)
            ax.clear()
            ax.plot(xdatos,ydatos)
        ani = animation.FuncAnimation(fig, animate, fargs = (xdatos,ydatos))
        plt.show()
