# Programming_Final

#Create a virtual environment:

```sh
conda create -n final-env python=3.10

conda activate final-env
```
Install third-party packages:

```sh
pip install -r requirements.txt
```
Run program

```sh
python app/basecode.py
```
test

```sh
pytest
```
web app

```sh
export FLASK_APP=web_app
flask run