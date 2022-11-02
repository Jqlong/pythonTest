unprinted_designs = ['iphone', 'robot', 'xiaomi']
completed_models = []

while unprinted_designs:
    # 弹出元素
    current_models = unprinted_designs.pop()

    # 打印
    print(current_models)
    completed_models.append(current_models)

for completed_model in completed_models:
    print(completed_model.title())