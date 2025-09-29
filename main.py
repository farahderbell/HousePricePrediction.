import argparse
from prepare import prepare
from train import train
from test import test
from evaluate import evaluate

def main(args):
    # Step 1: Prepare data
    house_df = prepare()

    # Step 2: Train model
    X_train, X_test, y_train, y_test, model = train(house_df, test_size=args.test_size)

    # Step 3: Test model
    predictions = test(model, X_test)

    # Step 4: Evaluate model
    evaluate(y_test, predictions)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="House Price Prediction Pipeline")
    parser.add_argument("--test_size", type=float, default=0.4, help="Proportion of test data (default=0.4)")
    args = parser.parse_args()

    main(args)
