import os
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.fusion.config import CONCAT_DIM, HIDDEN_DIM, NUM_CLASSES, TONGUE_EMBED_DIM, SKIN_EMBED_DIM, CLINICAL_EMBED_DIM

class GatedMultimodalFusion(nn.Module):
    def __init__(self, concat_dim=CONCAT_DIM, hidden_dim=HIDDEN_DIM, num_classes=NUM_CLASSES):
        super(GatedMultimodalFusion, self).__init__()
        
        self.tongue_gate = nn.Sequential(nn.Linear(TONGUE_EMBED_DIM, 8), nn.Sigmoid())
        self.skin_gate = nn.Sequential(nn.Linear(SKIN_EMBED_DIM, 8), nn.Sigmoid())
        self.clinical_gate = nn.Sequential(nn.Linear(CLINICAL_EMBED_DIM, 8), nn.Sigmoid())
        
        self.fusion_fc1 = nn.Linear(concat_dim, hidden_dim)
        self.bn1 = nn.BatchNorm1d(hidden_dim)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)
        
        self.classifier = nn.Linear(hidden_dim, num_classes)
        
    def forward(self, tongue_emb, skin_emb, clinical_emb):
        concat_emb = torch.cat([tongue_emb, skin_emb, clinical_emb], dim=1)
        
        h = self.fusion_fc1(concat_emb)
        h = self.bn1(h)
        h = self.relu(h)
        h = self.dropout(h)
        
        logits = self.classifier(h)
        return logits, h
