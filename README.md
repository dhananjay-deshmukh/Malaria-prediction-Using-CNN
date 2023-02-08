
# Malaria Detection Using Deep Learning

This project focuses on classifying images of human cells as "Infected" or "Uninfected". This is done using Convolutional Neural Network (CNN).

The dataset used can be downloaded from the below link:

Training data : https://github.com/dhananjay-deshmukh/Malaria-prediction-/tree/main/train

Testing data : https://github.com/dhananjay-deshmukh/Malaria-prediction-/tree/main/test

These directories have already been structured for ease of use. 

Test
|--Uninfected
|--Parasitized

Train
|--Uninfected
|--Parasitized

A streamlit app has also been included to demo the built model. 
The model gives results with an accuracy of 95%

![image](https://drive.google.com/uc?export=view&id=1jFn49MFFvOsHVuZ3fOnwhoOiNSOGMjMm)

## Run Locally

Clone the project

```bash
  git clone https://https://github.com/dhananjay-deshmukh/Malaria-prediction-Using-CNN.git
```

Go to the project directory

```bash
  cd Malaria-prediction-
```

Install dependencies

```bash
  pip install requirements.txt
```

Run the app

```bash
  streamlit run app.py
```

Upload any cell image from the "test" folder downloaded earlier and click "predict now".

## Demo Screenshot


![image](https://drive.google.com/uc?export=view&id=1opQhNfq-M2cUAyhR10d8nAMXCIwOWW3S)

