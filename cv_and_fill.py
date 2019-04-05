import cv2
import numpy as np





#size = 280x407
##############setting#########

X_SIZE = 256
Y_SIZE = 192

DIV_SIZE = 20 
X_PLUS = int(X_SIZE/DIV_SIZE)
Y_PLUS = int(Y_SIZE/DIV_SIZE)
COLOR = 190
BLACK = 10

##

def check_color(color):
    
    check = True #True = 조건 만족
    SIZE = 30

    if abs(int(color[0]) - int(color[1])) > SIZE:
        check = False
    if abs(int(color[0]) - int(color[2])) > SIZE:
        check = False
    if abs(int(color[1]) - int(color[2])) > SIZE:
        check = False

    if check == False:
        print("FALSE : " + str(color) )
    

    return check

def flood_fill(img,x,y):
    h, w = img.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    seed_pt = None
    fixed_range = True
    connectivity = 4
    lo = 50
    hi = 30

    cv2.imshow("start",img)

    flooded = img.copy()
    mask[:] = 0
    flags = connectivity
    seed_pt = y, x

    if fixed_range:
        flags |= cv2.FLOODFILL_FIXED_RANGE
    cv2.floodFill(flooded, mask, seed_pt, (0, 0, 0), (lo,)*3, (hi,)*3, flags)
    #cv2.circle(flooded, seed_pt, 2, (0, 0, 255), -1) #잡은 포인트 표시

    #cv2.imshow("final",flooded)
    #cv2.waitKey(0) # 키입력까지 대기
    #cv2.destroyAllWindows()
    return flooded

def x_findwhite(img):    
    ori_img = img
    count = 0

    befo_color = 0 # 0 = black , 1 = white, 2 = others


    for x in range(0,X_SIZE): # X_SIZE로 나눈거로 하얀게 있나 검사
        count = count + 1
        befo_color = 0

        for y in range(0, int(Y_SIZE/2)):
            color = ori_img[x,y]
            #print(color)
            if color[0] > COLOR and color[1] > COLOR and color[2] > COLOR and check_color(color) == True:
                ori_img = flood_fill(ori_img,x,y)
                #ori_img[x,y] = (0,0,0)
                #ori_img[x+1, y] = (255, 0, 0)
                #ori_img[x - 1, y] = (255, 0, 0)

                befo_color = 1
                print("1")

            elif befo_color != 0:
                print("0")
                break
            elif color[0] > BLACK and color[1] > BLACK and color[2] > BLACK: #안쪽까지 가지 않게하기 위해
                break

        befo_color = 0

        for y in range(Y_SIZE-1, int(Y_SIZE/2), -1):
            color = ori_img[x,y]
            #print(color)
            if color[0] > COLOR and color[1] > COLOR and color[2] > COLOR and check_color(color) == True:
                print(color)
                ori_img = flood_fill(ori_img, x, y)
                #ori_img[x,y] = (0,0,0)
                #ori_img[x+1, y] = (255, 0, 0)
                #ori_img[x - 1, y] = (255, 0, 0)
                befo_color = 1
                print("1")
            elif befo_color != 0:
                print("0")
                break
            elif color[0] > BLACK and color[1] > BLACK and color[2] > BLACK:
                break

    print(count)
    return ori_img

def use_floodfill(img):
    lo = 100
    hi = 100
    


##
'''
ori_img = cv2.imread('black_test.png')

x_plus = int(X_SIZE/30)
y_plus = int(Y_SIZE/30)

save_list = [[0 for x in range(Y_SIZE)] for y in range(X_SIZE)]
save_color = ()

print(ori_img[X_SIZE-5][Y_SIZE-5])


befo_color = 0 # 0 = black , 1 = white, 2 = others

new_img = x_findwhite(ori_img)


cv2.imshow("final",new_img)
cv2.imwrite("result.png",new_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])

cv2.waitKey(0) # 키입력까지 대기
cv2.destroyAllWindows()
'''

for i in range(1,9):

    ori_img = cv2.imread('cvcontour/' + str(i) + '.png')

    x_plus = int(X_SIZE/30)
    y_plus = int(Y_SIZE/30)

    save_list = [[0 for x in range(Y_SIZE)] for y in range(X_SIZE)]
    save_color = ()

    print(ori_img[X_SIZE-5][Y_SIZE-5])


    befo_color = 0 # 0 = black , 1 = white, 2 = others

    new_img = x_findwhite(ori_img)


    #cv2.imshow("final",ori_img)
    cv2.imwrite("cvcontour/"+str(i)+"_result.png",new_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])