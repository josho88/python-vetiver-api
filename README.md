# Python MLOps: Vetiver API


<!-- README.md is generated from README.qmd. Please edit that file -->

## :writing_hand: Author

[Josh Olney](induco.sols@gmail.com)

## :wave: Introduction

This repository demonstrates how to build and deploy a machine learning
model in Python, using the `vetiver` MLOps framework.

*“… MLOps, is a set of practices to deploy and maintain machine learning
models in production reliably and efficiently. The vetiverframework is
for MLOps tasks in Python and R.*

*The goal of vetiver is to provide fluent tooling
to **version**, **deploy**, and **monitor** a trained model. Functions
handle both recording and checking the model's input data prototype, and
predicting from a remote API endpoint.”*

With `vetiver`, models are deployed as a Plumber API in R or a FastAPI
in Python. These include a POST endpoint for making predictions from the
trained machine learning model. Deploying a model as an API is a typical
step in many MLOps frameworks. This approach ensures we deploy machine
learning models in a consistent fashion, can version them effectively
and can monitor the performance of our models in production.

## Train a `vetiver` model

## Create API endpoint

## Deploy with Docker

``` bash
docker build -t my-vetiver-api .
```

``` bash
docker run -d --name vetiver-api -p 8080:8080 my-vetiver-api
```

## Predict from your model endpoint

``` python
from vetiver.server import predict, vetiver_endpoint

endpoint = vetiver_endpoint("http://127.0.0.1:8080/predict")
endpoint
#> 'http://127.0.0.1:8080/predict'
```

If such a deployed model endpoint is running via one process (either
remotely on a server or locally, perhaps via Docker or a background job
in the RStudio IDE), you can make predictions with that deployed model
and new data in another, separate process1

``` python
import pandas as pd

new_car_dict = {"cyl": [4], "disp": [200], 
                 "hp": [100], "drat": [3],
                 "wt": [3], "qsec": [17], 
                 "vs": [0], "am": [1],
                 "gear": [4], "carb": [2]}
new_car = pd.DataFrame(new_car_dict)
predict(endpoint, new_car)
#>      predict
#> 0  22.292603
```

Being able to predict with a `vetiver` model endpoint takes advantage of
the model’s input data prototype and other metadata that is stored with
the model.

- Model card
- Unit tests
- Visualise
