
#Title :  AI-Powered Log Generation and Anomaly Detection with Docker

This document explains **step-by-step how to set up and run two Docker containers** for generating logs and applying AI-based anomaly detection on those logs.
-----------------------------------------------------------------------------------------------------------------
## Overview

This project is split into two main phases:
* **Phase 1:** Run a containerized Python script that simulates an application generating log entries. These logs include normal informational messages as well as warning and error messages. The logs are saved to a CSV file on your local machine.
* **Phase 2:** Run a second containerized Python program that trains an AI model to detect anomalies by analyzing the generated logs CSV file. It identifies unusual or error-prone log entries and outputs them for review.
----------------------------------------------------------------------------------------------------------------
## Phase 1: Log Generation Container

### Step 1: Prepare the Log Generator Script

* Create a Python script that generates 30 log entries.
* Each log entry contains a timestamp, a log level (INFO, WARNING, or ERROR), and a descriptive message.
* The script randomly decides whether to generate a normal informational log or an error/warning log.
* All generated logs are saved to a CSV file named `app_logs.csv`.
### Step 2: Create a Dockerfile for Log Generation

* Write a Dockerfile that uses a Python base image.
* Copy the log generator script into the container.
* Install any necessary Python packages such as pandas.
* Set the container's command to execute the log generation script.
### Step 3: Build and Run the Log Generator Container

* Use the Docker CLI to build the container image for the log generator.
* Run the container with volume mounting to your local directory so the generated CSV file is saved outside the container.
* After execution, verify that `app_logs.csv` exists in your directory and contains the generated logs.
---------------------------------------------------------------------------------------------------------------
## Phase 2: AI-Based Anomaly Detection Container

### Step 1: Prepare the AI Training Script

* Create a Python script that trains an Isolation Forest AI model using a small set of predefined normal log messages.
* The model learns the pattern of normal logs to detect deviations.
### Step 2: Prepare the Anomaly Detection Script

* Create a Python script that loads the AI model and the generated `app_logs.csv`.
* Extract meaningful features from log entries, such as message length, encoded log levels, and word counts.
* Use the AI model to predict which log entries are anomalous.
* Print or display the detected anomalies clearly.
### Step 3: Create a Dockerfile for AI Analysis

* Write a Dockerfile that uses a Python base image.
* Copy both the training and detection scripts into the container.
* Install all required Python packages (pandas, scikit-learn, pyod, joblib).
* Configure the container to run both the training and detection scripts sequentially upon startup.
### Step 4: Build and Run the AI Analysis Container

* Use the Docker CLI to build the AI analyzer container image.
* Run the container, mounting your working directory so it can access `app_logs.csv` and save the AI model file.
* Observe the output to see which log entries were flagged as anomalies.
--------------------------------------------------------------------------------------------------------------------------------
## Running Both Phases Together

* You can streamline your workflow by running both containers one after the other using a single command.
* First, run the log generator container to produce new logs.
* Then, immediately run the AI analyzer container to process the fresh logs and detect anomalies.
* This setup automates the full cycle of log generation and AI-based monitoring.
--------------------------------------------------------------------------------------------------------------------------------
## Handling Multiple Log Files for Anomaly Detection

* If you have several log files from different sources or times, place all CSV log files in a dedicated folder (e.g., `logs/`).
* Modify the anomaly detection script to loop through all CSV files in this folder, applying the AI model to each.
* Run the AI analyzer container with volume mounting pointing to this logs directory.
* The output will show anomalies detected across multiple files, helping scale your analysis.
-----------------------------------------------------------------------------------------------------------------------------------
## Summary of Commands I use:

Here’s the order of commands you will typically run:
1. **Build the log generator container**
    docker build -f Dockerfile.phase1 -t log-generator .
2. **Run the log generator container to create logs**
    docker run --rm -v $(pwd):/app log-generator
3. **Build the AI anomaly detection container**
    docker build -f Dockerfile.phase2 -t ai-log-analyzer .

4. **Run the AI anomaly detection container on generated logs**
   docker run --rm -v $(pwd):/app ai-log-analyzer
5. **Optional: Run both phases sequentially with a single command**
   docker run --rm -v $(pwd):/app log-generator
   docker run --rm -v $(pwd):/app ai-log-analyzer
