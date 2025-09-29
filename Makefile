VENV = venv
PYTHON = $(VENV)/bin/python

# Default target: run the full pipeline
all: pipeline

# Ensure venv exists and install dependencies
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r requirements.txt

# Run the full pipeline (main.py)
pipeline: $(VENV)/bin/activate
	$(PYTHON) main.py --test_size 0.4

# Run individual steps
prepare: $(VENV)/bin/activate
	$(PYTHON) -c "from prepare import prepare; prepare()"

train: $(VENV)/bin/activate
	$(PYTHON) -c "from prepare import prepare; from train import train; train(prepare())"

test: $(VENV)/bin/activate
	$(PYTHON) -c "from prepare import prepare; from train import train; from test import test; X_train, X_test, y_train, y_test, model = train(prepare()); test(model, X_test)"

evaluate: $(VENV)/bin/activate
	$(PYTHON) -c "from prepare import prepare; from train import train; from test import test; from evaluate import evaluate; X_train, X_test, y_train, y_test, model = train(prepare()); predictions = test(model, X_test); evaluate(y_test, predictions)"


# Clean cache + venv
clean:
	rm -rf __pycache__ *.pyc $(VENV)
