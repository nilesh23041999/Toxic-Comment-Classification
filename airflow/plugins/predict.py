import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
# Load Huggingface transformers
from transformers import TFBertModel,  BertConfig, BertTokenizerFast, TFAutoModel



# And pandas for data import + sklearn because you allways need sklearn
import pandas as pd
import glob
import tensorflow as tf
import re
import numpy as np
from sklearn.model_selection import train_test_split

def main_predict():
    max_length = 128
    config = BertConfig.from_pretrained("bert-base-uncased")
    tokenizer = BertTokenizerFast.from_pretrained(pretrained_model_name_or_path="bert-base-uncased",
                                                  config=config)
    loaded_1 = load_model("/home/nilu/small_model.h5")
    test_df = pd.read_csv(glob.glob("/mnt/c/Users/Lenovo/OneDrive/Desktop/twitter_data/twitter/*.csv")[0])
    test_df_only = test_df[['author_id', 'tweet']]
    test_sentences = test_df_only["tweet"].values
    test_x = tokenizer(
        text=list(test_sentences),
        add_special_tokens=True,
        max_length=max_length,
        truncation=True,
        padding='max_length',
        return_tensors='tf',
        return_token_type_ids=False,
        return_attention_mask=True,
        verbose=True)
    predictions = loaded_1.predict(x={'input_ids': test_x['input_ids'], 'attention_mask': test_x['attention_mask']},
                                   batch_size=32)
    list_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    submission = pd.DataFrame(predictions, columns=list_classes)
    output = pd.concat([test_df, submission], axis=1)
    output.to_csv("/mnt/c/Users/Lenovo/OneDrive/Desktop/final_report/report.csv", index=False)
