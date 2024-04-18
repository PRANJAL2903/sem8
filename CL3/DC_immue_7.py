import numpy as np 
from sklearn.metrics import classification_report

class AIRS: 
    def __init__(self, num_detectors=10, hypermutation_rate=0.1): 
        self.num_detectors = num_detectors 
        self.hypermutation_rate = hypermutation_rate 
    
    def train(self, X, y): 
        
        self.detectors = X[np.random.choice(len(X), self.num_detectors, replace=False)] 
    
    def predict(self, X): 
        predictions = [] 
        for sample in X: 
            distances = np.linalg.norm(self.detectors - sample, axis=1) 
            prediction = int(np.argmin(distances)) 
            predictions.append(prediction)
        return predictions 


def generate_dummy_data(samples=100, features=10): 
    data = np.random.rand(samples, features) 
    labels = np.random.randint(0, 2, size=samples) 
    return data, labels 


def split_data(data, labels, split_ratio=0.8): 
    split_index = int(split_ratio * len(data)) 
    train_data, test_data = data[:split_index], data[split_index:] 
    train_labels, test_labels = labels[:split_index], labels[split_index:] 
    return train_data, test_data, train_labels, test_labels 

# Evaluate accuracy 
def evaluate_accuracy(predictions, true_labels): 
    accuracy = np.mean(predictions == true_labels) 
    return accuracy

def main(): 
    
    data, labels = generate_dummy_data() 
    
    train_data, test_data, train_labels, test_labels = split_data(data, labels) 
    
    airs = AIRS(num_detectors=10, hypermutation_rate=0.1) 
    airs.train(train_data, train_labels) 
  
    predictions = airs.predict(test_data) 
    
    accuracy = evaluate_accuracy(predictions, test_labels) 
    print(f"Accuracy: {accuracy}") 

    # Rename the variable to avoid conflict with the imported function
    report = classification_report(predictions, test_labels)
    print(f"Classification Report: {report}")

if __name__ == "__main__": 
    main()

