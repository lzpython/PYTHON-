__author__ = 'thinkpad'
import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)
from ATM.bin import main
def rech(money):

    main.run(money)