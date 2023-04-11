import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
#��ȡͼ��
img = cv2.imread('../paojie_g.jpg', 0)
#����Ҷ�任
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
fshift = np.fft.fftshift(dft)
#���ô�ͨ�˲���
# w ����
# radius: �����ĵ�Ƶ��ƽ��ԭ��ľ���
rows, cols = img.shape
crow,ccol = int(rows/2), int(cols/2) #����λ��
w = 30
radius = 30
mask = np.ones((rows, cols, 2), np.uint8)
for i in range(0, rows):
    for j in range(0, cols):
        # ����(i, j)�����ĵ�ľ���
        d = math.sqrt(pow(i - crow, 2) + pow(j - ccol, 2))
        if radius - w / 2 < d < radius + w / 2:
            mask[i, j, 0] = mask[i, j, 1] = 0
        else:
            mask[i, j, 0] = mask[i, j, 1] = 1
#��Ĥͼ���Ƶ��ͼ��˻�
f = fshift * mask
#����Ҷ��任
ishift = np.fft.ifftshift(f)
iimg = cv2.idft(ishift)
res = cv2.magnitude(iimg[:,:,0], iimg[:,:,1])
#��ʾԭʼͼ��ʹ�ͨ�˲�����ͼ��
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(122), plt.imshow(res, 'gray'), plt.title('Band Pass Filter Image')
plt.axis('off')
plt.show()


