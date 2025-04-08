import tensorflow as tf
import numpy as np
import os
import json
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib

matplotlib.use('TkAgg')

# Load trained model
MODEL_PATH = "artifacts/training/model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Define test directory
TEST_DIR = r"C:\Users\OMEN\Documents\Chicken-fecal-images"

# Image preprocessing
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 16

test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# Get class labels
class_indices = test_generator.class_indices
class_names = list(class_indices.keys())

# Predictions
y_pred_probs = model.predict(test_generator)
y_pred = np.argmax(y_pred_probs, axis=1)
y_true = test_generator.classes

# Classification Report
report = classification_report(y_true, y_pred, target_names=class_names)
print("\nClassification Report:\n", report)

# Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

# Plot and Save Confusion Matrix
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.savefig("confusion_matrix.png")  # Save confusion matrix plot
plt.close()  # Close the figure

print("\n✅ Confusion matrix plot saved successfully!")
