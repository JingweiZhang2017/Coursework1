
import numpy as np
import map
from argparse import ArgumentParser
from graph import Greengraph
from matplotlib import pyplot as plt



#parser 
def process():
    parser = ArgumentParser(description = "evaluate the amount of the green pixels between the two points")
    parser.add_argument('--from',default ='New York', help = 'Start location/city，defalut New york', dest='start')
    parser.add_argument('--to',default = 'London',help = 'End location/city,default London', dest='end')
    parser.add_argument('--steps', type = int,default =20, help = 'Number of steps(images to preocess)bewteen two cities,default 20')
    parser.add_argument('--output', help = 'Filename of the output. Default output.png', default = 'output.png')
    arguments = parser.parse_args() 

    mygraph = Greengraph(arguments.start,arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    plt.title('Green pixels between'+ arguments.start + "to " + arguments.end)
    plt.xlabel('Steps')
    plt.ylabel('Fraction of green pixels')
    
    if arguments.output:
        plt.savefig(arguments.output)
    else:
        plt.show()


if __name__ == "__main__":
       process()