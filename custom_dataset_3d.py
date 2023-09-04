from torch.utils.data import Dataset, DataLoader
import cv2
import os 
import glob
import torch
from source import utils
import numpy as np
import pandas as pd

train_csv = pd.read_csv('data/2023_k_ium_composition/train_set/train.csv')

class Custom_dataset(Dataset):
    def __init__(self, root_path, mode, transforms):
        self.all_data = sorted(glob.glob(os.path.join(root_path, mode, '*')))
        self.transforms = transforms
#         print(self.all_data)
        
    def __preproc__(self, file):
        verts, faces = utils.read_off(file)
        if self.transforms:
            pointcloud = self.transforms((verts, faces))
            
        print(pointcloud.shape)
        return pointcloud
        
    def __getitem__(self, index):
        images = []
        if torch.is_tensor(index):
            index = index.tolist()
        
        pcd_path = self.all_data[index]
#         print(pcd_path)
        
        with open(pcd_path, 'r') as f:
            pointcloud = self.__preproc__(f)
#         print("~~")
        pat_number = pcd_path[53:57]
#         print(pat_number)

        patient_index=train_csv[train_csv['Index'] == int(pat_number)]
#         print(patient_index)
        patient_aneurysm = patient_index['Aneurysm']
#         print(patient_aneurysm)
        label = int(patient_aneurysm.values)
        
        
#         print(pointcloud)
#         print(label)
        return pointcloud, label       
            
    def __len__(self):
        length = len(self.all_data)
        return length
        