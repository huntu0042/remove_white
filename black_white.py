import cv2
import numpy as np



#다른색 나와도 안으로 들어갈 수 있게 숮어중

#size = 280x407
##############setting#########

X_SIZE = 256
Y_SIZE = 192

DIV_SIZE = 20 
X_PLUS = int(X_SIZE/DIV_SIZE)
Y_PLUS = int(Y_SIZE/DIV_SIZE)
COLOR = 190
BLACK = 10

mask_list = [[0 for x in range(Y_SIZE)] for y in range(X_SIZE)]

##

def check_color(color):
    
    check = True #True = 조건 만족 
    SIZE = 35 #size 크기 만큼 오차 

    if abs(int(color[0]) - int(color[1])) > SIZE:
        check = False
    if abs(int(color[0]) - int(color[2])) > SIZE:
        check = False
    if abs(int(color[1]) - int(color[2])) > SIZE:
        check = False

    if check == False:
        print("FALSE : " + str(color) )
    

    return check



def x_findwhite(img):    
    ori_img = img
    count = 0

    befo_color = 0 # 0 = black , 1 = white, 2 = others
    # 처음 블랙일땐 안으로 계속 들어가고 흰색을 찾아서 나왔을 때(>COLOR) 검은색으로 변경
    # check_color를 이용해 세 개의 RGB 차이가 SIZE 이상 나지 않아야함 (흰색,회색 체크 위해)

    other_color_count = 0

    for x in range(0,X_SIZE): # X_SIZE로 나눈거로 하얀게 있나 검사
        count = count + 1
        befo_color = 0

        for y in range(0, int(Y_SIZE/2)):
            color = ori_img[x,y]
            #print(color)
            if color[0] > COLOR and color[1] > COLOR and color[2] > COLOR and check_color(color) == True:
                ori_img[x,y] = (0,0,0)
                mask_list[x,y] = (255,255,255)
                #ori_img[x+1, y] = (255, 0, 0)
                #ori_img[x - 1, y] = (255, 0, 0)

                befo_color = 1

            elif befo_color != 0: #흰색 나왔다가 끝난 경우. 안쪽까지 가지 않게 하기 위해
                other_color_count = other_color_count + 1
                break
            elif color[0] > BLACK and color[1] > BLACK and color[2] > BLACK: #안쪽까지 가지 않게하기 위해
                break

        befo_color = 0

        for y in range(Y_SIZE-1, int(Y_SIZE/2), -1):
            color = ori_img[x,y]
            #print(color)
            if color[0] > COLOR and color[1] > COLOR and color[2] > COLOR and check_color(color) == True:
                print(color)
                ori_img[x,y] = (0,0,0)
                mask_list[x,y] = (255,255,255)
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

##
for i in range(1,2):

    ori_img = cv2.imread('fill/' + str(i) + '.png')

    x_plus = int(X_SIZE/30)
    y_plus = int(Y_SIZE/30)

    save_list = [[0 for x in range(Y_SIZE)] for y in range(X_SIZE)]
    save_color = ()

    print(ori_img[X_SIZE-5][Y_SIZE-5])


    befo_color = 0 # 0 = black , 1 = white, 2 = others

    new_img = x_findwhite(ori_img)


    #cv2.imshow("final",ori_img)

    cv2.imwrite("fill/"+str(i)+"_result.png",new_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imwrite("fill/"+str(i)+"_mask.png",mask_list, [cv2.IMWRITE_PNG_COMPRESSION, 0])


#cv2.waitKey(0) # 키입력까지 대기
#cv2.destroyAlimglWindows()


#for y in range(0,270,y_plus):

\