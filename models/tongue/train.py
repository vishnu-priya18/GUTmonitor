import os
import sys
import json
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from models.tongue.config import DATA_DIR, RESULTS_DIR, MODEL_SAVE_PATH, BATCH_SIZE, EPOCHS, LEARNING_RATE, SEED, CLASSES
from models.tongue.dataset import TongueDataset
from models.tongue.model import TongueClassifier
from models.tongue.evaluate import evaluate_model

def train():
    torch.manual_seed(SEED)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training Tongue Model on device: {device}")
    
    train_dataset = TongueDataset(DATA_DIR, split="train")
    val_dataset = TongueDataset(DATA_DIR, split="val")
    
    if len(train_dataset) == 0:
        print("Error: Tongue train dataset is empty. Run python data/prepare_datasets.py first.")
        return
        
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
    
    model = TongueClassifier().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE, weight_decay=1e-4)
    
    history = {"train_loss": [], "val_loss": [], "val_acc": []}
    best_acc = 0.0
    
    for epoch in range(EPOCHS):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            logits, _ = model(images)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item() * images.size(0)
            
        epoch_train_loss = running_loss / len(train_dataset)
        
        # Validation
        model.eval()
        val_loss = 0.0
        correct = 0
        with torch.no_grad():
            for images, labels in val_loader:
                images, labels = images.to(device), labels.to(device)
                logits, _ = model(images)
                loss = criterion(logits, labels)
                val_loss += loss.item() * images.size(0)
                preds = logits.argmax(dim=1)
                correct += (preds == labels).sum().item()
                
        epoch_val_loss = val_loss / len(val_dataset)
        epoch_val_acc = correct / len(val_dataset)
        
        history["train_loss"].append(round(epoch_train_loss, 4))
        history["val_loss"].append(round(epoch_val_loss, 4))
        history["val_acc"].append(round(epoch_val_acc, 4))
        
        print(f"Epoch [{epoch+1}/{EPOCHS}] Train Loss: {epoch_train_loss:.4f} | Val Loss: {epoch_val_loss:.4f} | Val Acc: {epoch_val_acc:.4f}")
        
        if epoch_val_acc >= best_acc:
            best_acc = epoch_val_acc
            torch.save(model.state_dict(), MODEL_SAVE_PATH)
            
    print(f"Saved best Tongue Model to {MODEL_SAVE_PATH}")
    
    with open(os.path.join(RESULTS_DIR, "training_history.json"), "w") as f:
        json.dump(history, f, indent=2)
        
    evaluate_model(model, device)

if __name__ == "__main__":
    train()
