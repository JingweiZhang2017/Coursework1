The package can be installed by the following command (windows OS):

$ python setup.py install

And should be invoked by greengraph --from *** --to *** --steps *** --output ***.png. 

There are four optional arguments : with ‘--from’ and ‘--to’ , one can define the starting and ending point city of the calculation; with ‘--steps’, we can specify the data points (images to process) we want to collect; through ‘—output’ name of the output file can be defined. By default, it will generate a graph containing 20 data points of amount of the green pixels in a series of satellite images between New York and London.

One example could be: 

greengraph --from Paris --to ‘Hong Kong’ --steps 15 --output graph.png
