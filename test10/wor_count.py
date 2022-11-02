file_path = "../tip"

try:
    with open(file_path, encoding="UTF-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist!")
else:
    # 计算文件包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {file_path} has about {num_words} words.")