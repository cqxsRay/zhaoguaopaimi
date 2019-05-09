import os
import readConfig
proDir = os.path.split(os.path.realpath(__file__))[0]
a=os.path.dirname(os.path.realpath(__file__))
c=readConfig.proDir
print(proDir)
print(a)
print(c)