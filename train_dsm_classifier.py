
"""
Entrenamiento de un modelo DSM con DAIC-WOZ para clasificación binaria de depresión.
"""
import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from sklearn.model_selection import train_test_split

MODEL_NAME = "distilbert-base-uncased"
OUT_DIR = "./modelo_dsm"

def cargar_dataset(csv_path):
    df = pd.read_csv(csv_path)[["texto", "label"]].dropna()
    train_df, test_df = train_test_split(df, test_size=0.2, stratify=df["label"])
    return Dataset.from_pandas(train_df), Dataset.from_pandas(test_df)

def preparar(ds, tokenizer):
    return ds.map(lambda x: tokenizer(x["texto"], truncation=True, padding="max_length", max_length=256), batched=True)

def entrenar(train_ds, test_ds):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
    args = TrainingArguments(output_dir=OUT_DIR, evaluation_strategy="epoch", save_strategy="epoch",
                             logging_dir=f"{OUT_DIR}/logs", num_train_epochs=4, per_device_train_batch_size=8,
                             per_device_eval_batch_size=8, save_total_limit=1, load_best_model_at_end=True)
    trainer = Trainer(model=model, args=args, train_dataset=preparar(train_ds, tokenizer),
                      eval_dataset=preparar(test_ds, tokenizer), tokenizer=tokenizer)
    trainer.train()
    model.save_pretrained(OUT_DIR)
    tokenizer.save_pretrained(OUT_DIR)

if __name__ == "__main__":
    train, test = cargar_dataset("daicwoz_textos.csv")
    entrenar(train, test)
