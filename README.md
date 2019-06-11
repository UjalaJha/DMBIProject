# Polyline Marking using GeoJson 
When given a stream of Latitude and Longitude or any GeoJson File, we should be able to plot it over any Map API,
In the below project we implement it using google maps API. The below project is implemented in Django so the first steps includes installation of Django.

## Requirements
* Python
* Django
* Git

## Django Installation Step
This is the recommended way to install Django.

Install pip. The easiest is to use the standalone pip installer. If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.

Take a look at virtualenv and virtualenvwrapper. These tools provide isolated Python environments, which are more practical than installing packages systemwide. They also allow installing packages without administrator privileges. The contributing tutorial walks through how to create a virtualenv.

After you’ve created and activated a virtual environment, enter the command:

``` pip install Django ```

Once done with django installation, kindly clone this repo at any location, example desktop

## Project Cloning
Install git after downloading it from https://git-scm.com/downloads
Once done enter the following command

``` git clone https://github.com/UjalaJha/DMBIProject.git ```

Once done with cloning project it is time to run the project in localhost

## Run project on localhost
Kindly navigate to the project directory, inside the project directory open the command line and enter the following command
Run the project using command, 
```python manage.py runserver```

After this the project is locally hosted.
Open the hosted URL http://localhost:8000/ to view the marking

Project View.
![Project SS1](https://github.com/UjalaJha/DMBIProject/blob/master/dm.PNG "Logo Title Text 1")

https://drive.google.com/file/d/1kMTf6jBc3EJ4IcFaRywDBamOGoTgzqeM/view?usp=sharing


## Polyline Marking 
Now that we are done hosting the project, we proceed for polyline marking, for this follow the below steps

### Step 1
Save the Lat Long Stream / GeoJson file in media directory of this project

![Lat Long SS](https://github.com/UjalaJha/DMBIProject/blob/master/Latlong.JPG "Logo Title Text 1")

https://drive.google.com/file/d/1QDUWSm9zOGi1GFS-WvFXWbCgXZmwXI39/view?usp=sharing

### Step 2
Refresh the hosted URL http://localhost:8000/ to view the marking

Screen Shot Showing Polyline 1 Marking
![Project SS1](https://github.com/UjalaJha/DMBIProject/blob/master/image1.JPG "Logo Title Text 1")

https://drive.google.com/file/d/1kMTf6jBc3EJ4IcFaRywDBamOGoTgzqeM/view?usp=sharing


Screen Shot Showing Polyline 2 Marking
![Project SS2](https://github.com/UjalaJha/DMBIProject/blob/master/image2.JPG "Logo Title Text 1")

https://drive.google.com/file/d/1eX25P83o1lDMEZVmY1BPJmjXuu4oNI7l/view?usp=sharing


## Thank You
