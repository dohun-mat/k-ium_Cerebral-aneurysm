# k-ium_Cerebral-aneurysm

## 2023-06 ~ 2023-07

# 데이터  
환자 1127명  
총 데이터셋 = 9016개  
환자 1명의 뇌동맥류 CT이미지 8장  
모든 환자의 뇌동맥류 유무에 대한 CSV파일  

# 예시
![image](https://github.com/dohun-mat/k-ium_Cerebral-aneurysm/assets/81942144/f99dc604-1718-46e2-bcb5-6e0d479bc50c)

전처리 방식
![image](https://github.com/dohun-mat/k-ium_Cerebral-aneurysm/assets/81942144/42418828-22cc-4a2b-9322-df2c8360dbc8)

canny 윤곽선 검출(성능 향상 x)
기본 이미지로 진행

이미지에서 local한 부분을 잘 얻기위해서 이미지크기를 720,720으로 설정

# 뇌동맥류 예측 AI  
## 1. 3차원 1개의 이미지 8장을 24차원의 이미지 1장으로 압축후 resnet모델 사용
- val 성능 : 65%    
## 2. 3차원 1개의 이미지 8장을 24차원 의 이미지 1장으로 압축후 efficientNET모델 사용
- val 성능 : 55%
## 3. 2d 이미5를 1장씩 z축으로 올려서 3d이미지 1장으로 만든뒤 pointNet모델을 이용해 3D classification 진행 
- val 성능 : 45%
## 4. 3,8,720,720의 이미지 전체를 넣은 후 3dResnet모델을 이용해 3D classification을 진행
- val 성능 : 67%
