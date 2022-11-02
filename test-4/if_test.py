age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $10")
else:
    print("Your admission cost is $100")


alien_0 = {'color':'green','point':5}
print(alien_0['point'])
print(alien_0['color'])


alien_0 = {'x_position': 10, 'y_position': 25, 'speed':'medium'}
print("x的坐标为:" + str(alien_0['x_position']))

if 'speed' == 'slow':
    x_increase = 1;
elif 'speed' == 'medium':
    x_increase = 2;
else:
    x_increase = 3;

print("x的坐标为：" + str(alien_0['x_position'] + x_increase))

user_0 = {
    'username':'jiang qin long',
    'first': 'jiang',
    'last': 'qin long',
}
# 遍历字典
for key,value in user_0.items():
    print(key)
    print(value + "\n")

for keys in user_0.keys():
    print(keys.title())


# 创建30个外星人
aliens = [] # 空列表
for alien in range(30):
    new_aliens = {'color': 'green', 'point': 5}
    aliens.append(new_aliens)
# 打印输出前5个外星人
for ali in aliens[:5]:
    print(ali)