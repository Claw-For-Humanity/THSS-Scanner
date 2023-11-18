import cv2
import tkinter as tk

class camWork:
    camera = None
    camState = None
    
    def searchPortCam():
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index)
            if not cap.read()[0]:
                break
            else:
                arr.append(str(f'{index}'))
            cap.release()
            index += 1
            
        return arr

    def capture_vid(camPort):
        if camWork.camera == None or camWork.camera == False:
            camWork.camera = cv2.VideoCapture(int(camPort))
            if camWork.camera.isOpened():
                print('camera captured successfully \n')
                is_captured = True
                camWork.camState = is_captured
                return is_captured 
                 
    
            
            else:
                tk.messagebox.showinfo(title= 'warninig', message = 'camera encountered problem // line 165 // unknown issue // exitting')
                camWork.camera.capture_vid(int(camPort))
                is_captured = False
                camWork.camState = is_captured
                return is_captured
        else:
            pass
        
        
    def flow_vid(capturedCam):
        while True:
            ret, frame = capturedCam.read()
            if ret:
                return frame
            else:
                pass
    
    def recommendedRes():
        if camWork.camera.isOpened():
            camWork.camera.set(cv2.CAP_PROP_FRAME_WIDTH, int(camWork.camera.get(cv2.CAP_PROP_FRAME_WIDTH)))
            camWork.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, int(camWork.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        else:
            tk.messagebox.showinfo(title = 'warning', message = 'capture camera first!!')
        a,b = int(camWork.camera.get(cv2.CAP_PROP_FRAME_WIDTH)),int(camWork.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        return a,b