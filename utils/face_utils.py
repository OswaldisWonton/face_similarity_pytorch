import os
import cv2
import numpy as np
from tqdm import tqdm

import torch
import torch.nn.functional as F

import face_recognition
from facenet_pytorch import MTCNN, InceptionResnetV1

def face_detection(image):
    face_landmarks_list = face_recognition.face_landmarks(image)
    return bool(len(face_landmarks_list))

class FaceComparison:
    def __init__(self, device="cpu"):
        self.device = device
        self.mtcnn = MTCNN(device=device)
        self.resnet = InceptionResnetV1(pretrained='vggface2', device=device).eval()
        self.ref_image_path = "ref_data/"
        self.ref_features_path = "ref_data/ref_features.pt"
        self._get_ref_features()
        self.label_name = {
            "catfish": "鲶鱼",
            "dog": "犬",
            "frog": "蛙",
            "rat": "鼠",
            "sheep": "羊"
        }
    
    def _get_ref_features(self):
        if os.path.exists(self.ref_features_path):
            tmp = torch.load(self.ref_features_path)
            self.ref_features = tmp["features"].to(self.device)
            self.ref_labels = tmp["labels"]
            return
        print("[INFO] Run code for the first time. Generating features for reference images.")
        self.ref_features = []
        self.ref_labels = []
        for root, dirs, files in os.walk(self.ref_image_path):
            for file in tqdm(files):
                label = file.split("_")[0]
                image = cv2.imread(os.path.join(root, file))
                feature = self.image_feature(image)
                self.ref_features.append(feature)
                self.ref_labels.append(label)
            break
        self.ref_features = torch.stack(self.ref_features)
        torch.save({"features": self.ref_features.detach().cpu(), "labels": self.ref_labels}, self.ref_features_path)
    
    def image_feature(self, image):
        image_cropped = self.mtcnn(image).to(self.device)
        img_embedding = self.resnet(image_cropped.unsqueeze(0))
        return img_embedding.squeeze().detach()

    def comparison(self, image, output=None):
        feature = self.image_feature(image)
        similarity = self.ref_features @ feature
        max_idx = torch.argmax(similarity).item()
        # label = self.label_name[self.ref_labels[max_idx]]
        label = self.ref_labels[max_idx]
        if output is None:
            return label
        else:
            output.append(label)

if __name__ == "__main__":

    image = face_recognition.load_image_file("input/5485.jpg_wh300.jpg")

    print(face_detection(image))
