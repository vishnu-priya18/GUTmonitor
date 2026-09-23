import os
import sys
import torch
import torch.nn as nn
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.tongue.config import NUM_CLASSES, EMBEDDING_DIM

class TongueClassifier(nn.Module):
    def __init__(self, num_classes=NUM_CLASSES, embedding_dim=EMBEDDING_DIM):
        super(TongueClassifier, self).__init__()
        try:
            weights = MobileNet_V3_Small_Weights.DEFAULT
            self.backbone = mobilenet_v3_small(weights=weights)
        except Exception:
            self.backbone = mobilenet_v3_small(weights=None)
            
        in_features = self.backbone.classifier[0].in_features
        self.backbone.classifier = nn.Identity()
        
        self.embedding_layer = nn.Sequential(
            nn.Linear(in_features, 64),
            nn.ReLU(),
            nn.BatchNorm1d(64),
            nn.Linear(64, embedding_dim),
            nn.BatchNorm1d(embedding_dim)
        )
        
        self.classifier = nn.Linear(embedding_dim, num_classes)
        
    def forward(self, x):
        features = self.backbone(x)
        embedding = self.embedding_layer(features)
        logits = self.classifier(embedding)
        return logits, embedding
