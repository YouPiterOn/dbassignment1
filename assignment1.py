from read_uncommited_demo import *
from read_commited_demo import *
from repeatable_read_demo import *
from nonrepeatable_read_demo import *

if __name__ == "__main__":
    read_uncommited_demo()
    read_commited_demo()
    nonrepeatable_read_demo()
    repeatable_read_demo()