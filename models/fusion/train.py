import os
import sys
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.fusion.config import (
    RESULTS_DIR, MODEL_SAVE_PATH, BATCH_SIZE, EPOCHS, LEARNING_RATE, SEED,
    TONGUE_EMBED_DIM, SKIN_EMBED_DIM, CLINICAL_EMBED_DIM
)
from models.fusion.model import GatedMultimodalFusion
from models.fusion.evaluate import evaluate_fusion_model

def generate_proto_fusion_dataset(n_samples=600):
    np.random.seed(SEED)
    labels = np.random.choice([0, 1, 2], size=n_samples, p=[0.4, 0.35, 0.25])
    
    tongue_embs = []
    skin_embs = []
    clinical_embs = []
    
    for l in labels:
        t_base = np.random.normal(loc=l*0.5, scale=0.3, size=TONGUE_EMBED_DIM)
        s_base = np.random.normal(loc=l*0.4, scale=0.3, size=SKIN_EMBED_DIM)
        c_base = np.random.normal(loc=l*0.6, scale=0.2, size=CLINICAL_EMBED_DIM)
        
        tongue_embs.append(t_base)
        skin_embs.append(s_base)
        clinical_embs.append(c_base)
        
    t_tensor = torch.tensor(np.array(tongue_embs), dtype=torch.float32)
    s_tensor = torch.tensor(np.array(skin_embs), dtype=torch.float32)
    c_tensor = torch.tensor(np.array(clinical_embs), dtype=torch.float32)
    l_tensor = torch.tensor(labels, dtype=torch.long)
    
    return t_tensor, s_tensor, c_tensor, l_tensor

def train():
    torch.manual_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training Multimodal Prototype Fusion Model on device: {device}")
    
    t_data, s_data, c_data, labels = generate_proto_fusion_dataset(n_samples=600)
    split_idx = int(0.8 * len(labels))
    
    train_dataset = TensorDataset(t_data[:split_idx], s_data[:split_idx], c_data[:split_idx], labels[:split_idx])
    test_dataset = TensorDataset(t_data[split_idx:], s_data[split_idx:], c_data[split_idx:], labels[split_idx:])
    
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    
    model = GatedMultimodalFusion().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    
    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        for t_b, s_b, c_b, l_b in train_loader:
            t_b, s_b, c_b, l_b = t_b.to(device), s_b.to(device), c_b.to(device), l_b.to(device)
            optimizer.zero_grad()
            logits, _ = model(t_b, s_b, c_b)
            loss = criterion(logits, l_b)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * len(l_b)
            
        print(f"Epoch [{epoch+1}/{EPOCHS}] Fusion Train Loss: {running_loss / len(train_dataset):.4f}")
        
    torch.save(model.state_dict(), MODEL_SAVE_PATH)
    print(f"Saved Fusion Model state dict to {MODEL_SAVE_PATH}")
    
    evaluate_fusion_model(model, test_dataset, device)

if __name__ == "__main__":
    train()
