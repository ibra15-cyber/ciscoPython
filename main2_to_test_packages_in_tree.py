from sys import path
path.append('./packages') #adding package path


#******************** one form of import the absolute
import extra.iota

print(extra.iota.funI())


# *****************************specific import 
from extra.iota import funI
print(funI())


# **************** importing deep down 
from sys import path

path.append('.\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())




