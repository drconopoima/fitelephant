# fitelephant.py

Python script for creating an elephant outline in a figure by using 4 parameters.

## Requirements

- Python 3.3.0 or greater. Python 2.7.17 (WARNING! DEPRECATED AS OF JAN. 1st, 2020)
- matplotlib >= 2.2.5, <= 4.0.0
- numpy >= 1.16.6, <= 2.0.0

## Run fitelephant package

Just invoke the `fitelephant.py` script with your python interpreter:

```sh
    python fitelephant.py
```

## Package Installation (and python environment notes)

Clone or download the project to your PC and change into the project folder:

```sh
    git clone git@github.com:drconopoima/fitelephant.git
    cd fitelephant
```

### Local user dependency packages

Use local-user installed packages at all times when available. To install dependencies to your local user only, use `--user` flag at the installation command:
In order to install requirements by using pip:

```sh
    python3 -m pip install --user -r requirements.txt
```

### Using Python venv (virtual environment)

Moreover, please use a virtual environment (venv) when using python >3.3.

```sh
    mkdir ${HOME}/python-venv
    python3 -m venv ${HOME}/python-venv/fitelephant
    source ${HOME}/python-venv/fitelephant/bin/activate
```

When the `venv` activates, it will prepend your shell promt with the name of the virtual environment:

> (fitelephant) \$

Then install `fitelephant` requirements as follows:

```sh
    python3 -m pip install -r requirements.txt
```

When you want to finish working within your virtual environment:

```sh
    deactivate
```

## Manage python pip locally (Ubuntu 19.10)

You can ensure that you will only manage your local user's python packages by adding pip globally, using it for installation of local user pip package and finally removing global pip:

First install global pip as root (or by using sudo). Uncomment any version for following the same procedure for python 2 as well:

```sh
    sudo apt install -y python3-pip # python-pip
    python3 -m pip install --user --upgrade pip; # python -m pip install --user --upgrade pip
    sudo apt remove -y python3-pip # python-pip
```

Afterwards, you can manage python packages as your regular user:

```sh
    python3 -m pip --version; python -n pip --version
```

Process succeeded if you see a local path in your output:

> pip 20.0.2 from ~/.local/lib/python3.7/site-packages/pip (python 3.7)

```sh
    sudo python[3] -m pip --version
```

> /usr/bin/python[3]: No module named pip

## Troubleshooting

### Python 2.7

Some additional steps for making the script work on python 2.7 using Ubuntu 19.10.

#### functools_lru_cache (Ubuntu 19.10)

In case matplotlib raises the following error:

> ImportError: No module named functools_lru_cache

Install from your package manager the referenced package:

```sh
    sudo apt install -y python-backports.functools-lru-cache
```

#### backports.functools_lru_cache (Ubuntu 19.10)

In case matplotlib raises the following error:

> ImportError: No module named backports.functools_lru_cache

Reinstall package `backports.functools_lru_cache.pyc`. First get `apt-file` and update its cache.

```sh
    sudo apt install -y apt-file
    sudo apt-file update
    apt-file search /usr/lib/python2.7/dist-packages/backports/functools_lru_cache.pyc
```

It returned to be installed by:

> python-backports.functools-lru-cache: /usr/lib/python2.7/dist-packages/backports/functools_lru_cache.py

In order to remove it:

```sh
    sudo apt remove -y python-backports.functools-lru-cache
    sudo apt clean
    sudo apt install -y python-backports.functools-lru-cache
```

If no return, another option to search for package (forcefully resolving links):

```sh
    dpkg -S $(realpath /usr/lib/python2.7/dist-packages/backports/functools_lru_cache.py)
```

Alternatively, check the version of the python system package with pip and reinstall the latest from the MINOR (Semantic Versioning) by using pip:

```sh
    pip show backports.functools_lru_cache
```

> Name: backports.functools-lru-cache
> Version: 1.5

```sh
    sudo python2.7 -m pip uninstall --verbose backports.functools_lru_cache
    sudo python2.7 -m pip install --upgrade "backports.functools_lru_cache>=1.5.0,<1.6.0"
```

#### python-tk (Ubuntu 19.10)

In case matplotlib raises the following error:

> ImportError: No module named \_tkinter, please install the python-tk package

Install the system package `python-tk`

```sh
    sudo apt install -y python-tk
```

## Contributing

- By tracking and finding bugs:

Please open a [Github issue](https://github.com/drconopoima/fitelephant/issues)

- By creating code yourself:

Please open a [Github Pull Request](https://github.com/drconopoima/fitelephant/pulls). Please ensure you provide as clear as possible commit messages and description.

## References and special thanks

I've found and adapted the code found in [John D. Cook's 2011 online article](https://www.johndcook.com/blog/2011/06/21/how-to-fit-an-elephant/). John himself credit [Piotr Zolnierczuk](http://twitter.com/zolnie) for the code.

Along with using matplotlib, I adapted it to abide by the 4 parameters. The original used a 5th parameter to draw an eye for the elephant. While anybody knows the 5th parameter makes the elephant wiggle his trunk!

Parameters are based on the following paper:

> Drawing an elephant with four complex parameters. Jurgen Mayer, Khaled Khairy, and Jonathon Howard, Am. J. Phys. 78, 648 (2010), DOI:10.1119/1.3254017

## TO-DO

- Add a 5th parameter that makes the elephant wiggle his trunk.
