
"""
Fine-tuning de un modelo de clasificación emocional con Hugging Face Transformers.
Usa un CSV con columnas: texto, label (etiqueta de emoción o diagnóstico).
"""

import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from sklearn.preprocessing import LabelEncoder
import torch

# CONFIGURACIÓN
MODEL_NAME = "distilbert-base-uncased"  # o multilingual: 'bert-base-multilingual-cased'
MAX_LENGTH = 128
NUM_EPOCHS = 3
BATCH_SIZE = 8
OUTPUT_DIR = "./modelo_emocional"

# 1. Cargar y preparar los datos
def load_dataset(csv_path):
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=["texto", "label"])
    label_encoder = LabelEncoder()
    df["label_id"] = label_encoder.fit_transform(df["label"])
    dataset = Dataset.from_pandas(df[["texto", "label_id"]])
    return dataset, label_encoder

# 2. Tokenización
def tokenize_dataset(dataset, tokenizer):
    return dataset.map(lambda x: tokenizer(x["texto"], truncation=True, padding="max_length", max_length=MAX_LENGTH), batched=True)

# 3. Fine-tuning
def train_model(dataset, num_labels):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenized_dataset = tokenize_dataset(dataset, tokenizer)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=num_labels)

    training_args = TrainingArguments(
        output_dir=OUTPUT_DIR,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        num_train_epochs=NUM_EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        weight_decay=0.01,
        logging_dir=f"{OUTPUT_DIR}/logs",
        logging_steps=10,
        save_total_limit=1,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset.select(range(min(100, len(tokenized_dataset)))),
        tokenizer=tokenizer
    )

    trainer.train()
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

if __name__ == "__main__":
    dataset, label_encoder = load_dataset("dataset_emociones.csv")  # Reemplaza por tu CSV real
    train_model(dataset, num_labels=len(label_encoder.classes_))
