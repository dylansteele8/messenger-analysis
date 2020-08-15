# messenger analysis

## Setup

Create a Python 3 virtual environment, activate it, and install the dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

In the activated virtual environment, run the `main.py` script

```bash
python main.py <path/to/inbox/directory>
```

Show the help message and additional arguments with

```bash
python main.py --help
```

> **NOTE:** The downloaded Facebook data must be in the same directory as the `main.py` script at the path `messages/inbox`.

## Developing

### Formating Code

Code is formatted with [`black`](https://github.com/psf/black). Please format your code before creating a PR. In the activated virtual environment, run `black`

```bash
black main.py
```
