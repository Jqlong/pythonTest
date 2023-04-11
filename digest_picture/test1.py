# coding=utf-8
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 低通、高通、带阻和带通滤波器
x = np.arange(100)
y = np.where(x > 50, x, 1)
lp = np.where(x < 50, y, 0)

hp = 1 - lp

plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(16, 8))
plt.subplot(2, 2, 1), plt.plot(lp), plt.title('低通滤波器'), plt.xticks([]), plt.yticks([0, 1]), plt.ylim([0, 2])
plt.subplot(2, 2, 2), plt.plot(hp), plt.title('高通滤波器'), plt.xticks([]), plt.yticks([0, 1]), plt.ylim([0, 2])

y = np.where(x > 30, x, 1)
l_1 = np.where(x < 30, y, 0)

y = np.where(x > 70, x, 1)
l_2 = np.where(x < 70, y, 0)
h_1 = 1 - l_2

br = h_1 + l_1
plt.subplot(2, 2, 3), plt.plot(br), plt.title('阻带滤波器'), plt.xticks([]), plt.yticks([0, 1]), plt.ylim([0, 2])
bp = 1 - br
plt.subplot(2, 2, 4), plt.plot(bp), plt.title('通带滤波器'), plt.xticks([]), plt.yticks([0, 1]), plt.ylim([0, 2])

plt.show()

height, width = 597, 597
m = int((height - 1) / 2)
n = int((width - 1) / 2)
X = np.linspace(-8.2, 8.2, height)
Y = np.linspace(-8.2, 8.2, width)
x, y = np.meshgrid(X, Y)
circle = 0.5 * (1 + np.cos(x ** 2 + y ** 2))
for i in range(circle.shape[0]):
    for j in range(circle.shape[1]):
        if np.sqrt((i - m) ** 2 + (j - n) ** 2) > m:
            circle[i, j] = 0
        else:
            continue
plt.imshow(circle, 'gray'), plt.title('Concentric circles'), plt.xticks([]), plt.yticks([])
plt.tight_layout()

plt.show()


def zone(x, y):
    return 0.5 * (1 + math.cos(x * x + y * y))
SIZE = 597
image = np.zeros((SIZE, SIZE))

start = -8.2
end = 8.2
step = 0.0275


def dist_center(y, x):
    global SIZE
    center = SIZE / 2
    return math.sqrt((x - center) ** 2 + (y - center) ** 2)


for y in range(0, SIZE):
    for x in range(0, SIZE):
        if dist_center(y, x) > 300:
            continue
        y_val = start + y * step
        x_val = start + x * step
        image[y, x] = zone(x_val, y_val)
plt.imshow(image)
plt.show()
kernel_size = 15


def gkern(size, sigma=1.0):
    x = np.arange(-size // 2 + 1, size // 2 + 1)
    g = norm.pdf(x, scale=sigma)
    kernel = np.outer(g, g)
    kernel = kernel / kernel.sum()
    return kernel


lowpass_kernel_gaussian = gkern(kernel_size)
lowpass_kernel_gaussian = lowpass_kernel_gaussian / lowpass_kernel_gaussian.sum()

lowpass_kernel_box = np.ones((kernel_size, kernel_size))
lowpass_kernel_box = lowpass_kernel_box / (kernel_size * kernel_size)

lowpass_image_gaussian = cv2.filter2D(image, -1, lowpass_kernel_gaussian)
lowpass_image_box = cv2.filter2D(image, -1, lowpass_kernel_box)

highpass_image_gaussian = image - lowpass_image_gaussian
highpass_image_gaussian = np.absolute(highpass_image_gaussian)

highpass_image_box = image - lowpass_image_box
highpass_image_box = np.absolute(highpass_image_box)

bandreject_image = lowpass_image_gaussian + highpass_image_box
bandpass_image = image - bandreject_image
bandpass_image = np.absolute(bandpass_image)