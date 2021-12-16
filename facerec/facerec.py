import face_recognition
import numpy as np
from glob import glob

"""
人脸识别模块

配 置 环 境:
    Python 3.7
    安装face_recognition库，如pip install face_recognition。

使 用 方 法:
在调用前，将需要识别的人的图像放在../dataset/groundtruth下，将需要被识别的包括未知人的帧(也就是摄像头传来等待鉴权的图像)放在../dataset/unknown/下。其中:
    groundtruth下的图像遵照 张三.jpg, 李四.jpg，......,王五.jpg。存放。
    unknown下的图像无命名要求，但不要包括奇怪的特殊字符。同样使用jpg格式。

使用时，调用recognition()，无需参数。支持多人同框，返回识别的名字列表。将返回一个布尔值代表是否成功，和一个人名列表。以下字段:
    Bool, List[]
    比如:
        True, [“张三”,“李四”,...,"王五"，"unknown"]
        True, [“张三”]
        True, ["unknown"]
        False, []
    如果识别识别，会返回空列表。如果识别的人是未注册的，那么那个人的名字就是unknown。换言之，如果发现返回的人名列表中有unknown，就认为是非法的。

更多细节:
    每次调用recognition()时会自动调用train()，算法读取groundtruth里的图像生成已知人脸特征集，然后读取unknown里的图像生成未知人脸特征集。然后做匹配。输出最相似人脸的名。
    因为严格意义讲并没有训练模型，只是通过人脸图像推理特征encoding，所以速度很快。因为它速度很快，所以也不需要单独训练了，直接随用随推理。
    在GPU上推理速度较快，需要小于3GB显存。但也支持CPU。
    此模型识别效果相当不错。

"""

def train():
    trainset_images = glob('../dataset/groundtruth/*.jpg')
    known_face_encodings = []
    known_face_names = []
    for trainset_image in trainset_images:
        cache_image = face_recognition.load_image_file(trainset_image)
        cache_face_encoding = face_recognition.face_encodings(cache_image)[0]
        known_face_encodings.append(cache_face_encoding)
        known_face_names.append(trainset_image.split('/')[-1].split('.')[0])
    return known_face_encodings, known_face_names


def recognition():
    # Initialize some variables
    print('Initializing groundtruth faces...')
    known_face_encodings, known_face_names = train()
    print('Initialized')
    #print(known_face_encodings, known_face_names)
    face_encodings = []
    face_names = []
    target_images = glob('../dataset/unknown/*.jpg')
    for target_image in target_images:
        cache_image = face_recognition.load_image_file(target_image)
        try:
            cache_embedding = face_recognition.face_encodings(cache_image)[0]
        except:
            print('获取Face Encoding失败，检查输入图像是否正常。')
            return False, []
        face_encodings.append(cache_embedding)

    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
    return True, face_names


if __name__ == '__main__':
    success, facenames = recognition()
    print(success, facenames)