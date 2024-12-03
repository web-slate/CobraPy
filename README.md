# CobraPy
Suggests agility and power, suitable for a versatile Python project.

## Installation Command

```
pip install -r requirements.txt
```

## Development Installation Command

```
pip install -r dev-requirements.txt
```

## Build and Run

```
docker build -t math_api .
docker run -p 8000:8000 math_api
```

##  Static Binaries with PyInstaller

```
pyinstaller --onefile main.py --name math_api
mv dist/math_api static/
```

## Packaging

```
python setup.py build_ext --inplace
```

## Command to Fix All Files

```
autopep8 --in-place --aggressive --aggressive *.py
```
