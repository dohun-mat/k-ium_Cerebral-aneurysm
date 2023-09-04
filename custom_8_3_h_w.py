from torch.utils.data import Dataset, DataLoader
import cv2
import os 
import glob
import torch
from source import utils
import numpy as np
import pandas as pd

train_csv = pd.read_csv('C:/Users/dhkim/Desktop/directory/k-ium/data/2023_k_ium_composition/train_set/train.csv')
pat_number = train_csv['Index'].tolist()
pat_number

from torch.utils.data import Dataset, DataLoader
import cv2
import os 

class Custom_dataset(Dataset):
    def __init__(self, root_path, mode, transforms):
        self.all_data = sorted(glob.glob(os.path.join(root_path, mode, '*')))
        self.transforms = transforms
        
    def __getitem__(self, index):
        images = []
        if torch.is_tensor(index):
            index = index.tolist()
            
        data_path = self.all_data[index]
        in_data = sorted(glob.glob(os.path.join(data_path, '*')))
        for i in range(8):
            image = cv2.imread(in_data[i])
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
            #transform 적용
            if self.transforms is not None:
                augmentation = self.transforms(image = image)
                image = augmentation['image']
            
            images.append(image)
            
            for i in pat_number:
                if str(i) in data_path:
                    patient_index=train_csv[train_csv['Index'] == i]
                    patient_aneurysm = patient_index['Aneurysm']
                    label = int(patient_aneurysm.values)
        
        output_images = torch.stack(images, dim=0)  # 크기: (8, 3, H, W)
#         print(output_images.shape)
        return output_images, label       
            
    def __len__(self):
        length = len(self.all_data)
        return length
        
        