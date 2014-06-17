import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('--doit-num-process', metavar='NUM_PROCESSES', 
                    type=int, default=1, 
                    help='Number of tasks to execute in parallel')

parser.add_argument('--doit-db-file', metavar='DB_FILE',
                    default=os.path.join(os.getcwd(), '.doit.db'), 
                    help='Location of doit database file')

parser.add_argument('-v', '--verbosity', action='count',
                    help='Set the verbosity level (-v is least verbose, -vvv is most)')


