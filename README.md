# Grid AI Defense Lab

A Python-based AI defense lab that simulates cyber threats against an imaginary power plant and electrical grid. This project was built in a virtual machine using Python, pandas, scikit-learn, and joblib to demonstrate data generation, model training, and attack detection with alerting.

## Project Overview

This lab was designed to simulate how AI could support monitoring and detection in a critical infrastructure environment. The project creates synthetic operational and attack data, trains a machine learning model to classify suspicious behavior, and then runs a detection-and-alert pipeline against new event data.

## Features

- Synthetic telemetry generation for a grid/power-style environment
- Normal vs attack event labeling
- Random Forest model training
- Detection of suspicious activity from new events
- Alert generation for likely attack behavior

## Files

- `make_sample_data.py` - Generates the synthetic dataset
- `train_model.py` - Trains the machine learning model and saves it
- `detect_and_alert.py` - Loads the model, evaluates new events, and generates alerts

## Tools Used

- Python
- pandas
- scikit-learn
- joblib
- VirtualBox
- Ubuntu Linux

## Workflow

1. Generate synthetic operational and attack data
2. Save the dataset as a CSV file
3. Train a machine learning model on the dataset
4. Save the trained model
5. Run new event data through the model
6. Print alerts for suspicious events

## Results

- 600 total synthetic events generated
- 500 labeled as normal
- 100 labeled as attack
- 99% model accuracy during testing
- Successful alerting on suspicious events

## Detection Example

The detection phase evaluates incoming event data using features such as:

- generator load
- transformer temperature
- line voltage
- network traffic
- login failures
- PLC command rate

The model classifies each event as either `normal` or `attack`, and the script prints alerts when suspicious activity is detected.

## Future Improvements

- Add timestamps to alerts
- Add severity levels
- Write alerts to CSV or JSON log files
- Build a SIEM-style dashboard or monitoring layer
- Expand attack scenarios for OT/ICS environments

## Why I Built This

I built this project to combine my background in electrical systems and mission-critical infrastructure with my transition into cybersecurity, AI, and critical infrastructure defense. This lab is part of my effort to build hands-on projects that demonstrate both technical ability and real-world security thinking.
