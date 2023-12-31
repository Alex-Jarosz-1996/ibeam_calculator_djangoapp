# I-beam Calculator
This project seeks to find an optimal geometric configuration for an I-beam. It aims to find the optimal height and width for a symmetric I-beam around the x-axis.  
The purpose of this file is to find the theoretical ideal relationship between for an I-beam.

## Use me
To use the app:

cd into ibeamroot:
```
$ cd /ibeam_calculator_djangoapp/ibeamroot/
```

Enter the following command in a bash terminal:
```
$ python manage.py runserver
```

Enter all values as desired.

## Docker
The program can be built and ran through Docker with the following steps:
1. Build the docker image:
```
$ docker build -t ibeam-django-app .
```

2. Run the docker container:
```
$ docker run -p 5000:5000 django-app
```

The program can be accessed in thr browser in the following address:
```
http://localhost:5000
```