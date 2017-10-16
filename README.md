# Venn Tool

Tool To Visualize Intersections of Data from Different Sources

## Getting Started

These instructions will get you a copy of the tool running on your local machine.

### Prerequisites

This is project was developed on Python 2.7. There is a virtual environment used in this project so the only required packages are Python 2.7 and virtualenv. Below is how to install virtualenv if you are using Python 2.7.

#### Getting PIP
    
First copy the text from the following link onto your computer in a new file that you name "get-pip.py":

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
https://github.com/jasonschray/venn_tool.git
```

If you have a MAC cpmputer,you must update the matplotlibrc file on your computer so that the plotting will run properly. Enter the following commands to update the file. 

```
cd ~/.matplotlib
touch matplotlibrc
echo backend: TkAgg > matplotlibrc
```

To install the requirements for the tool globally so you dont need to run the tool in virtualenv use pip:

```
sudo pip install -r requirements.txt
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

Run the script in virtualenv command:

```
source env/bin/activate
python main.py -i test.csv
```

Turn off virtualenv when you aren't using the tool with the following command:

```
deactivate
```

Run the script with the following command if you installed the modules and dont want to use virtualenv:

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

