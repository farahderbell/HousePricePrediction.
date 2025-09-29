def test(model, X_test):
    predictions = model.predict(X_test)
    print("Sample predictions:", predictions[:10])
    return predictions

