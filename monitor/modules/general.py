import random
import subprocess
import datetime
import os.path


def bashcmd(string):
    cmd = string.split(" ")

    try:
        ret = subprocess.check_output(cmd)
    except subprocess.CalledProcessError:
        ret = ""
    ret = ret.replace("\n","")
    return ret


class simulation:

   def __init__(self, machine, directory):
      self.machine = machine
      self.directory = directory

   class parse():
      """Subclass this method to parse the
      input/output files in directory"""
      def __init__(self):
         return
      def getName(self):
         self.name = "Simulation " + str(random.rand() * 1000)
      def self.getDescription(self):
         self.description = bashcmd("cat notes")
      def self.getLastModified(self,file):
         d = os.path.getmtime("example")
         d = datetime.datetime.fromtimestamp(d)
         self.lastmodified = d











