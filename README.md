# transmissiontoolkit
transmission toolkit includes compress/decompress and encryption functions.

#### update Dec.16
Add Face Recognition Support

## 关于人脸识别模块

### 配置环境:  
&nbsp;&nbsp;Python 3.7  
&nbsp;&nbsp;安装face_recognition库，如pip install face_recognition。  

### 使用方法:
在调用前，将需要识别的人的图像放在../dataset/groundtruth下，将需要被识别的包括未知人的帧(也就是摄像头传来等待鉴权的图像)放在../dataset/unknown/下。其中:  
&nbsp;&nbsp;&nbsp;&nbsp;groundtruth下的图像遵照 张三.jpg, 李四.jpg，......,王五.jpg。存放。  
&nbsp;&nbsp;&nbsp;&nbsp;unknown下的图像无命名要求，但不要包括奇怪的特殊字符。同样使用jpg格式。  

使用时，调用recognition()，无需参数。支持多人同框，返回识别的名字列表。将返回一个布尔值代表是否成功，和一个人名列表。以下字段:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bool, List[]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;比如:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True, [“张三”,“李四”,...,"王五"，"unknown"]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True, [“张三”]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;True, ["unknown"]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;False, []  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果识别识别，会返回空列表。如果识别的人是未注册的，那么那个人的名字就是unknown。换言之，如果发现返回的人名列表中有unknown，就认为是非法的。  

### 更多细节:
&nbsp;&nbsp;&nbsp;&nbsp;每次调用recognition()时会自动调用train()，算法读取groundtruth里的图像生成已知人脸特征集，然后读取unknown里的图像生成未知人脸特征集。然后做匹配。输出最相似人脸的名。  
&nbsp;&nbsp;&nbsp;&nbsp;因为严格意义讲并没有训练模型，只是通过人脸图像推理特征encoding，所以速度很快。因为它速度很快，所以也不需要单独训练了，直接随用随推理。  
&nbsp;&nbsp;&nbsp;&nbsp;在GPU上推理速度较快，需要小于3GB显存。但也支持CPU。  
&nbsp;&nbsp;&nbsp;&nbsp;此模型识别效果相当不错。  
