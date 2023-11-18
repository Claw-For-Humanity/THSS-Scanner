import tkinter as tk
import detector
import cv2
import serial
import camWork
import os
import json
from PIL import Image, ImageTk


class THSS_detector:
    
    camList_val = None
    window = None
    camResX, camResY = None, None
    canvas = None
    canvas_image = None
    i = 0
    camPorts = None
    
    def prev_data():
        
        savePath = os.getcwd() + "/THSS_detector/json"
        if os.path.exists(os.path.join(savePath, "save.json")):
            f = open(os.path.join(savePath, "save.json"))
            prevData = json.load(f)

            THSS_detector.camList_val = prevData['camList_val']
        else:
            pass
    
    def updateCamPorts():
        camPort = camWork.camWork.searchPortCam()
        print(f"Updated camPorts: {camPort}")
        THSS_detector.camPorts = camPort
        THSS_detector.window.after(3000, THSS_detector.updateCamPorts)
       
        
    
    def chooseCam():
        
        
        CamPortLabel = tk.Label(THSS_detector.window, text='Select Camera Port', font=('Arial',15))
        CamPortLabel.place(x=30, y=130)
        
        
        CamOption = tk.OptionMenu(THSS_detector.window, THSS_detector.camList_val, *THSS_detector.camPorts)
        CamOption.place(x= 30, y= 45)
        
        if THSS_detector.camList_val.get() != "None":
            if camWork.camWork.camState != True:
                camWork.camWork.capture_vid(int(THSS_detector.camList_val.get()))
                
            else:
                THSS_detector.camResX, THSS_detector.camResY = camWork.camWork.recommendedRes()
                
                THSS_detector.canvas.config(width = THSS_detector.camResX, height = THSS_detector.camResY)
                THSS_detector.displayCam()
                print('pass')
        
        
        THSS_detector.window.after(50, THSS_detector.chooseCam)
            
    def displayCam():
        frame = cv2.cvtColor(camWork.camWork.flow_vid(camWork.camWork.camera), cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        THSS_detector.canvas.itemconfig(THSS_detector.canvas_image, image = imgtk)
        THSS_detector.canvas.image = imgtk
        print('done ')
        
        
        
    def Start():
        
        THSS_detector.prev_data()
        
        THSS_detector.window = tk.Tk()
        THSS_detector.window.title("Project Claw For Humanity Port Selector")
        THSS_detector.window.geometry("1200x1200")
        
        if THSS_detector.camList_val != 'None':
            THSS_detector.camList_val = tk.StringVar(THSS_detector.window, str(THSS_detector.camList_val))
        else:
            THSS_detector.camList_val = tk.StringVar(THSS_detector.window, "Cam Port")
        
        
        THSS_detector.canvas = tk.Canvas(THSS_detector.window)
        THSS_detector.canvas_image = THSS_detector.canvas.create_image(0,50,anchor=tk.NW)
        THSS_detector.canvas.place (x=30, y=60)
        
        print('\nentering choosecam\n')
        THSS_detector.updateCamPorts()
        THSS_detector.chooseCam()
        
        
        print('wow')
        
        THSS_detector.window.mainloop()
    
            
THSS_detector.Start()