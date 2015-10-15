'''
Created on Oct 3, 2015

@author: Jonathan
'''
class Environment(object):
    simClock = 0
    rotatonalPeriod = None
    def __init__(self):
        self.simClock = 0
        
    def getTime(self):
        return self.simClock
    
    def incrementTime(self, microseconds):
        try: i = int(microseconds)
        except: raise ValueError('Environment.incrementTime():  invalid parameter for time to be incremented')
        if (microseconds >= 0):
            self.simClock += self.simClock + microseconds
        else:
            raise ValueError('Environment.incrementTime():  invalid bounds for time to add')
        return self.simClock
    
    def setRotationalPeriod(self, microseconds):
        try: i = int(microseconds)
        except: raise ValueError('Environment.setRotaionalPeriod:  invalid parameter for rotational period')
        if (microseconds >= 1000000):
            self.rotatonalPeriod = microseconds
            return microseconds
        else:
            raise ValueError('Environment.setRotationalPeriod():  parameter does not fall in range')
    
    def getRotationalPeriod(self):
        if (self.rotatonalPeriod == None):
            raise ValueError('Environment.getRotationalPeriod():  rotational period has not initially been set')
            pass
        else:
            return self.rotatonalPeriod
        
            
    
    
        
        