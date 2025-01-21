import numpy as np

def calculate_accuracy(predictions, true_labels):
    predicted_classes = np.argmax(predictions, axis=1)
    true_classes = np.argmax(true_labels, axis=1)
    correct_predictions = np.sum(predicted_classes == true_classes)
    accuracy = correct_predictions / len(true_labels)
    return accuracy
