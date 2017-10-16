# Project Title

Tool To Visualize Intersections of Data from Different Sources

## Getting Started

These instructions will get you a copy of the tool running on your local machine.

### Prerequisites

This is project was developed on Python 2.7. There is a virtual environment used in this project so the only required packages are Python 2.7 and virtualenv. Below is how to install virtualenv if you are using Python 2.7.

#### Getting PIP
    
First copy the file from the following link onto your computer as "get-pip.py":

```
https://bootstrap.pypa.io/get-pip.py
```

Then run that file using the following command in the Terminal:

```
python get-pip.py install
```

Now you have pip which can be used to install a variety of software packages for python.

#### Getting virtualenv
Now we can use pip to install virtualenv:

```
sudo pip install virtualenv
```

Now you have virtualenv which are required to run this tool easily.

### Installing

Below are the steps to install this project and run it locally. First follow the steps in pre-requisites.

First make a folder called venn_tool and navigate to it in the terminal. Then copy the contents of the [Zip File](https://github.com/jasonschray/memFlash/archive/master.zip) to the folder or  enter the following command in the terminal if you have git:

```
git clone https://github.com/jasonschray/memFlash.git
```

If you have a MAC cpmputer,you must update the matplotlibrc file on your computer so that the plotting will run properly. Enter the following commands to update the file. 

```
cd ~/.matplotlib
touch matplotlibrc
echo backend: TkAgg > matplotlibrc
```

The file format for running this script is a .csv file. Currently the project only supports 3 column .csv files with the following format:

```
Title1,Title2,Title3
Data01,Data02,Data03
Data11,Data12,Data13
Data21,Data22,...
Data31,...,...
.
.
.
.
DataN1,DataN2,DataN3
```

Run the script with the following command:

```
python main.py -i test.csv
```


## Built With

* [Matplotlib Venn](https://pypi.python.org/pypi/matplotlib-venn) - The venn diagram project used
* [PurpleBooth README Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - The template for this README file

## Contributing

## Authors

* **Jason Schray** - *Initial work* - [Jason Schray](https://github.com/jasonschray)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Acknowledgments

* Thanks to Lisa for being nice to me and including me in her excitement. It was so fun to work on this tool for her.

