import os

target_path = 'C:/Users/jsl11/Desktop/dataset/' + 'Abra' + '/'  # 원본 이미지 경로
print(len(os.walk(target_path)[2]))