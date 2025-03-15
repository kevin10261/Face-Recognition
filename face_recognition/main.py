import cv2
from simple_facerec import SimpleFacerec

sfr = SimpleFacerec()
sfr.load_encoding_images("face/")

# Initialize Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Detect known faces
    face_location,face_names = sfr.detect_known_faces(frame)
    for face_loc, face_name in zip(face_location, face_names):
        top,left,bottom,right = face_loc[0],face_loc[1],face_loc[2],face_loc[3]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 4)
        cv2.putText(frame, face_name, (left, top), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('frame', frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()