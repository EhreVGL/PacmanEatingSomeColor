import cv2
import numpy as np






# mavi renk algılanan objenin etrafına dörtgen çizip yazı yazıyor.
def rectangle_blue(res):


    lr = cv2.pyrDown(res)
    lr2 = cv2.pyrDown(lr)

    kernel_ero = np.ones((3, 3), np.uint8)
    kernel_dil = np.ones((7, 7), np.uint8)

    blur = cv2.medianBlur(lr2, 5)
    erosion = cv2.erode(blur, kernel_ero, iterations=1)
    dilation = cv2.dilate(erosion, kernel_dil, iterations=1)

    gray = cv2.cvtColor(lr2, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("asd",gray)

    # Buradan oncesi goruntuyu duzeltme islemiydi. Buradan sonrası görüntüyü kesme islemi.
    h = gray.shape[0]
    w = gray.shape[1]
    color = []
    for y in range(0, h):
        for x in range(0, w):
            if gray[y, x] > 10:
                color.append((y, x))
    y_buyuk = 0
    y_kucuk = 9999
    x_buyuk = 0
    x_kucuk = 9999

    for x1 in color:
        if x1[0] > y_buyuk:
            y_buyuk = x1[0]
        if x1[1] > x_buyuk:
            x_buyuk = x1[1]
        if x1[0] < y_kucuk:
            y_kucuk = x1[0]
        if x1[1] < x_kucuk:
            x_kucuk = x1[1]

    # print('Sol üst köşe:' + '(' + str(x_kucuk) + ',' + str(y_kucuk) + ')')
    # print('Sağ alt köşe:' + '(' + str(x_buyuk) + ',' + str(y_buyuk) + ')')

    lr2 = cv2.rectangle(lr2, (x_kucuk, y_kucuk), (x_buyuk, y_buyuk), (255, 0, 0), 1)
    cv2.putText(lr2, 'Blue Object', (x_kucuk, y_kucuk - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1, cv2.LINE_AA)

    # canavar(pacman,x_kucuk,y_kucuk,x_buyuk,y_buyuk)

    pr = cv2.pyrUp(lr2)
    pr2 = cv2.pyrUp(pr)
    return pr2,x_kucuk,y_kucuk,x_buyuk,y_buyuk




pacman = cv2.imread('pacman.png')
pacman = cv2.pyrDown(pacman)
pacman = cv2.pyrDown(pacman)
pacman = cv2.pyrDown(pacman)
pacman = cv2.pyrDown(pacman)
# frame boyutu (480,640)
# pacman boyutu (954,954)

# video ve renk algılama kısmı
cap = cv2.VideoCapture(0)
while(1):

    _,frame = cap.read()

    print(frame.shape[0])

    frame_kopya = frame.copy()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,115,0])
    upper_blue = np.array([140,255,255])
    mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
    res_blue = cv2.bitwise_and(frame,frame,mask=mask_blue)
    res_blue_kopya = res_blue.copy()
    res_blue,x_kucuk,y_kucuk,x_buyuk,y_buyuk = rectangle_blue(res_blue)

    x_son = int(x_buyuk/5 )
    y_son = int(y_buyuk/5 )


    for i in range(20):
        frame = frame_kopya.copy()
        # pacman = cv2.pyrDown(pacman)
        # pacman = cv2.pyrDown(pacman)
        # frame = cv2.pyrDown(frame)

        rows, cols, channels = pacman.shape
        # packman'i döndürüyor.
        # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 2, 1)
        payda_son = ((i + 1) * y_son)
        pay_son = ((i + 1) * x_son)
        if i == 0:
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 325, 1)
            pacman = cv2.warpAffine(pacman, M, (cols, rows))

        # img2 = cv2.warpAffine(img2, M, (cols, rows))
        if ((i + 1) * y_son) + 239 >= frame.shape[0] or ((i + 1) * x_son) + 239 >= frame.shape[1]:

            break
        else:
            # İstenilen noktaya şekli koymak için, bu yüzden ROI
            roi = frame[0 + (i + 1) * y_son:rows + (i + 1) * y_son, 0 + (i + 1) * x_son:cols + (i + 1) * x_son]

        # Şimdi bir logo maskesi oluşturun ve bunun ters maskesini de oluşturun
        img2gray = cv2.cvtColor(pacman, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        # Şimdi ROI
        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # maskenin tersini oluşturuyoruz.
        img2_fg = cv2.bitwise_and(pacman, pacman, mask=mask)

        # ROI'ye logo yerleştirin ve ana görüntüyü
        dst = cv2.add(img1_bg, img2_fg)
        frame[0 + (i + 1) * y_son:rows + (i + 1) * y_son, 0 + (i + 1) * x_son:cols + (i + 1) * x_son] = dst

        # pacman = cv2.pyrUp(pacman)
        # pacman = cv2.pyrUp(pacman)
        # frame = cv2.pyrUp(frame)

        cv2.imshow('frame', frame)
        cv2.imshow('blue', res_blue)
        # cv2.imshow('mask',mask_blue)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:  # wait for ESC key to exit
            break


    pay = int(x_kucuk / 5)
    payda = int(y_kucuk / 5)
    # for i in range(30):
    #     frame = frame_kopya.copy()
    #     # frame = frame - res_blue_kopya
    #
    #     if i == 0:
    #         M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    #         img2 = cv2.warpAffine(pacman, M, (cols, rows))
    #     # img2 = cv2.warpAffine(img2, M, (cols, rows))
    #     if ((i + 1) * payda) + 239 + payda_son <= 0 or ((i + 1) * pay) + 239 + payda_son >= frame.shape[1]:
    #         break
    #     # Sol üst köşeye pacman koymak istiyorum, bu yüzden ROI
    #     rows, cols, channels = pacman.shape
    #     roi = frame[payda_son - (i + 1) * payda:rows + payda_son - (i + 1) * payda,pay_son + (i + 1) * pay:cols + pay_son + (i + 1) * pay]
    #     # Şimdi bir logo maskesi oluşturun ve bunun ters maskesini de oluşturun
    #     img2gray = cv2.cvtColor(pacman, cv2.COLOR_BGR2GRAY)
    #     ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    #     mask_inv = cv2.bitwise_not(mask)
    #     # Şimdi ROI
    #     img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    #
    #     # Logo resminden sadece logonun bölgesini alın.
    #     img2_fg = cv2.bitwise_and(pacman, pacman, mask=mask)
    #
    #     # ROI'ye logo yerleştirin ve ana görüntüyü
    #     dst = cv2.add(img1_bg, img2_fg)
    #     frame[payda_son - (i + 1) * payda:rows + payda_son - (i + 1) * payda,pay_son + (i + 1) * pay:cols + pay_son + (i + 1) * pay] = dst
    #
    #
    #     cv2.imshow('frame', frame)
    #     cv2.imshow('blue', res_blue)
    #     k = cv2.waitKey(5) & 0xFF
    #     if k == 27:  # wait for ESC key to exit
    #         break
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 325, 1)
    pacman = cv2.warpAffine(pacman, M, (cols, rows))


# cv2.destroyAllWindows()







