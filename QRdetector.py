# detects qr code

import cv2



class qrcheck:
    
    def scan(picture):

        img = cv2.imread(picture)

        dat = cv2.QRCodeDetector()

        val, pts, st_code = dat.detectAndDecode(img)
        
        return val

