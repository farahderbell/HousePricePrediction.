import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

def evaluate(y_test, predictions):
    print('MAE:', metrics.mean_absolute_error(y_test, predictions))
    print('MSE:', metrics.mean_squared_error(y_test, predictions))
    print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

    # Scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, predictions, color='blue', alpha=0.5, label='Predictions vs Actual')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             'r--', label='Perfect Prediction Line')
    plt.xlabel('Actual Values (y_test)')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.legend()
    plt.grid(True)
    plt.show()

