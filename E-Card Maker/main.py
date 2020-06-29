import numpy as np
import cv2


text = input('Enter Text: ')

image = cv2.imread(r'templates/starry_sky.png', cv2.IMREAD_UNCHANGED)




position = (0, 50)

font = cv2.FONT_HERSHEY_TRIPLEX
font_thickness = 1
font_color = (100, 150, 200, 255)
font_size = 1

(text_width, text_height) = cv2.getTextSize(text, font, font_size, font_thickness)[0]

text_height += position[1] - 15

mask = np.zeros((text_height, text_width), dtype=np.uint8)
mask = cv2.putText(mask,text, position, font, font_size, font_color, font_thickness, cv2.LINE_AA)

new_position = (int(300 - (text_width / 2)), int(200 - (text_height / 2)))

cv2.putText(image, text, new_position, font, font_size, font_color, font_size)
cv2.imshow('E-Card', image)
cv2.waitKey(0)
cv2.imwrite('e_card.png', image)