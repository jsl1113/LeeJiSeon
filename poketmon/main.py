# -*- coding:utf-8 -*-
import cv2
import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


pokemon = []
name_path = 'C:/Users/jsl11/Desktop/dataset/'
pokemon = os.listdir(name_path)


for p in pokemon:
    dir1 = 'C:/Users/jsl11/Desktop/img/test/' + p + '/'
    dir2 = 'C:/Users/jsl11/Desktop/img/train/' + p + '/'
    os.mkdir(dir1)
    os.mkdir(dir2)

def fileCnt(path):
     file_list = os.listdir(path)
     return len(file_list)


for pokemon_name in pokemon:
    target_path = 'C:/Users/jsl11/Desktop/dataset/' + pokemon_name + '/'  # 원본 이미지 경로
    train_path = 'C:/Users/jsl11/Desktop/img/train/' + pokemon_name + '/'    # 훈련 이미지 저장 경로
    test_path = 'C:/Users/jsl11/Desktop/img/test/' + pokemon_name + '/'      # 테스트 이미지 저장 경로

    wid_rate = 1  # ga로비
    hei_rate = 1  # se로비
    width = 244  # resize width
    height = 244  # resize height


    # 1. 폴더내 이미지 파일 읽어오기

    pre_data = []
    filelist = os.listdir(target_path)

    for file in filelist:
        try:
            src = cv2.imread(target_path + file, cv2.IMREAD_GRAYSCALE)

            resized_img = cv2.resize(src, dsize=(width, height),
                                     fx=wid_rate, fy=hei_rate,
                                     interpolation=cv2.INTER_LINEAR)
            pre_data.append(resized_img)
        except Exception as e:
            print(str(e))

    # 2. 이미지 부풀리기
    datagen = ImageDataGenerator(rescale=1. / 255,  # : 1/255로 스케일링하여 0-1 범위로 변환
                                 rotation_range=10,  # : 이미지 회전 범위 (degrees)
                                 width_shift_range=0.2,  # : 그림을 수평 또는 수직으로 랜덤하게 평행 이동시키는 범위
                                 height_shift_range=0.2,
                                 shear_range=0.7,  # : 임의 전단 변환 (shearing transformation) 범위
                                 zoom_range=[0.9, 2.2],  # : 임의 확대/축소 범위
                                 horizontal_flip=True,
                                 # : True로 설정할 경우, 50% 확률로 이미지를 수평으로 뒤집습니다. 즉, 뒤집어도 자연스러울 때 사용하면 좋습니다.
                                 vertical_flip=True,  # : 수직 ''
                                 fill_mode='nearest')  # : 이미지를 회전, 이동하거나 축소할 때 생기는 공간을 채우는 방식

    for j in range(len(pre_data)):
        i = 0
        x = img_to_array(pre_data[j])
        x = x.reshape((1,) + x.shape)

        # 아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
        # 지정된 `PP_img/` 폴더에 저장
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir=train_path,
                                  save_prefix='pp_',
                                  save_format='jpg'):
            i += 1
            if i >= 55:  # 사진 1장당 10장씩 부풀리기
                break

        if fileCnt(train_path) >= 2000:
            break

    for j in range(len(pre_data)):
        i = 0
        x = img_to_array(pre_data[j])
        x = x.reshape((1,) + x.shape)
        for batch in datagen.flow(x, batch_size=1,
                                  save_to_dir=test_path,
                                  save_prefix='pp_',
                                  save_format='jpg'):
            i += 1

            if i >= 27:  # 사진 1장당 10장씩 부풀리기
                break

        if fileCnt(test_path) >= 1000:
            break


