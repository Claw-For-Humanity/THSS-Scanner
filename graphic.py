import tkinter as tk
import QRdetector
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
    chooseCamStat = None
    captureCanvas = None
    startCaptureState = False
    capturingWindow = None
    
    def prev_data():
        pass
        # savePath = os.getcwd() + "/THSS_detector/json"
        # if os.path.exists(os.path.join(savePath, "save.json")):
        #     f = open(os.path.join(savePath, "save.json"))
        #     prevData = json.load(f)

        #     THSS_detector.camList_val = prevData['camList_val']
        # else:
        #     pass
    
    def updateCamPorts():
        camPort = camWork.camWork.searchPortCam()
        print(f"Updated camPorts: {camPort}")
        THSS_detector.camPorts = camPort
        
        if THSS_detector.chooseCamStat == True:
            THSS_detector.window.after(3000, THSS_detector.updateCamPorts)
        else:
            THSS_detector.chooseCam()
            THSS_detector.updateCamPorts()
            
            
       
        
    
    def chooseCam():
        
        if THSS_detector.chooseCamStat == None:
            THSS_detector.chooseCamStat = True
        else:
            pass
        
        
        THSS_detector.window = tk.Tk()
        THSS_detector.window.title("Claw For Humanity Ticket Check Configuration")
        THSS_detector.window.geometry("1200x1200")
        
        if THSS_detector.camList_val != 'None':
            THSS_detector.camList_val = tk.StringVar(THSS_detector.window, str(THSS_detector.camList_val))
        else:
            THSS_detector.camList_val = tk.StringVar(THSS_detector.window, "Cam Port")
        
        
        THSS_detector.canvas = tk.Canvas(THSS_detector.window)
        THSS_detector.canvas_image = THSS_detector.canvas.create_image(0,50,anchor=tk.NW)
        THSS_detector.canvas.place (x=30, y=60)
        
        
        CamPortLabel = tk.Label(THSS_detector.window, text='Select Camera Port', font=('Arial',15))
        CamPortLabel.place(x=30, y=20)
        NextButton = tk.Button(THSS_detector.window, text="next", command=THSS_detector.startCapture)
        
        
        CamOption = tk.OptionMenu(THSS_detector.window, THSS_detector.camList_val, *THSS_detector.camPorts)
        CamOption.place(x= 30, y= 45)
        
        if THSS_detector.camList_val.get() != "None":
            if camWork.camWork.camState != True:
                camWork.camWork.capture_vid(int(THSS_detector.camList_val.get()))
                
            else:
                THSS_detector.camResX, THSS_detector.camResY = camWork.camWork.recommendedRes()
                
                THSS_detector.canvas.config(width = THSS_detector.camResX, height = THSS_detector.camResY)
                THSS_detector.displayCam()
                NextButton.place(x=90, y= 30)
                print('pass')
        
        
        THSS_detector.window.after(50, THSS_detector.chooseCam)
            
    def displayCam():
        frame = cv2.cvtColor(camWork.camWork.flow_vid(camWork.camWork.camera), cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        if THSS_detector.startCaptureState:
            THSS_detector.captureCanvas.itemconfig(THSS_detector.canvas_capture_image, image = imgtk)
            THSS_detector.captureCanvas.image = imgtk
            
            # THSS_detector.window.after(50, THSS_detector.)
            
        else:
            THSS_detector.canvas.itemconfig(THSS_detector.canvas_image, image = imgtk)
            THSS_detector.canvas.image = imgtk
        print('done ')
        
    
    def startCapture():
        
        THSS_detector.window.destroy()
        
        THSS_detector.capturingWindow = tk.Tk()
        THSS_detector.capturingWindow.title("Claw For Humanity Ticket Checker")
        THSS_detector.capturingWindow.geometry("1200x1200")
        THSS_detector.capturingWindow.resizable(True, True)
        
        label_capturing = tk.Label(THSS_detector.capturingWindow, text="capturing...", font=('Arial', 15))
        label_capturing.place(x=500, y= 20)
        
        if THSS_detector.captureCanvas == None:
            THSS_detector.captureCanvas = tk.Canvas(THSS_detector.capturingWindow)
            THSS_detector.canvas_capture_image = THSS_detector.canvas.create_image(0,50,anchor=tk.NW)
            THSS_detector.captureCanvas.place (x=30, y=60)
        else:
            pass
        
        THSS_detector.startCaptureState = True
        THSS_detector.displayCam()
        
        THSS_detector.capturingWindow.mainloop()
        
    def Start():
        THSS_detector.prev_data()
        print('\nentering choosecam\n')
        
        THSS_detector.updateCamPorts()
        THSS_detector.chooseCam()
        
        
        
        print('wow')
        
        THSS_detector.window.mainloop()
    
            
THSS_detector.Start()