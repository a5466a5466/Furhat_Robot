# Furhat Robot HCI Component

## Emotions

* Anger
* Disgust
* Fear
* Happiness
* Sadness
* Surprise
* Neutral

## Instructions

### Requirements

* Python 3.11
* Virtual Furhat 2.7.1

### Install

Run the following in a terminal to install all Python software library packages using Pip

```bash
pip install -r requirements.txt
```

### Run

> * Launch Virtual Furhat  
> * Start Remote API

#### Static Emotion Response Gestures

Run the following in a terminal for the Virtual Furhat to display a gesture matching any of the listed `Emotions`

```bash
python main.py --gesture [emotion]
```

Otherwise, run the following in a terminal for the Virtual Furhat to display all gestures listed in `Emotions`

```bash
python main.py
```
