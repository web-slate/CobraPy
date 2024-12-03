# CobraPy
Suggests agility and power, suitable for a versatile Python project.

## Installation Command

```
pip install -r requirements.txt
```

## Build and Run

```
docker build -t myapp .
docker run -p 8000:8000 myapp
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