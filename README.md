# k-ium_Cerebral-aneurysm

# 데이터  
환자 1명의 뇌동맥류 CT이미지 8장  
모든 환자의 뇌동맥류 유무에 대한 CSV파일  

# 뇌동맥류 예측 AI  
## 1. 3차원 1개의 이미지 8장을 24차원의 이미지 1장으로 압축후 resnet모델 사용  
## 2. 3차원 1개의 이미지 8장을 24차원 의 이미지 1장으로 압축후 efficientNET모델 사용  
## 3. 2d 이미지를 1장씩 z축으로 올려서 3d이미지 1장으로 만든뒤 pointNet모델을 이용해 3D classification 진행  
## 4. 3,8,224,224의 이미지 전체를 넣은 후 3dResnet모델을 이용해 3D classification을 진행
