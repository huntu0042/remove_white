import cv2
import numpy as np

#size = 280x407
###############흰색만들기#########

X_SIZE = 407
Y_SIZE = 280

ori_img = cv2.imread('black_test.png')

x_plus = int(X_SIZE/30)
y_plus = int(Y_SIZE/30)

save_list = [[0 for x in range(280)] for y in range(407)]
save_color = ()

print(ori_img[406][270])

count = 0

for x in range(0,X_SIZE,x_plus): # x 10으로 나눈거로 하얀게 있나 검사
    count = count + 1
    for y in range(0, Y_SIZE):
        color = ori_img[x,y]
        #print(color)
        if color[0] > 215 and color[1] > 215 and color[2] > 215:
            print(color)
            ori_img[x,y] = (255,0,0)
            ori_img[x+1, y] = (255, 0, 0)
            ori_img[x - 1, y] = (255, 0, 0)
            break

print(count)
cv2.imshow("final",ori_img)

cv2.waitKey(0) # 키입력까지 대기
cv2.destroyAllWindows()


#for y in range(0,270,y_plus):

print(ori_img.shape)

