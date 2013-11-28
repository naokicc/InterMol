import sys
sys.path.append('../..')
from System import System
import os.path

System._sys = System("Redone Sample")
print "System initialized\n"
print "ENTER FILENAME?\n"
filename = raw_input("")
while not (os.path.isfile(filename+".cms")):
 print "File doesn't exist, try again\n"
 filename = raw_input("")
filename_out = filename + "_OUT"
print "\nReading in Desmond structure %s"%(filename)
import ctools.DesmondExt.DesmondParser as DesmondParser
DesmondParser = DesmondParser()
DesmondParser.readFile(filename+".cms")
print "\nWriting out Gromacs topology %s.top "%(filename_out)
import  ctools.GromacsExt.GromacsTopologyParser as GromacsTopologyParser
GromacsTopologyParser = GromacsTopologyParser()
GromacsTopologyParser.writeTopology(filename_out+".top")
print "\nWriting in Gromacs Stucture as %s"%(filename_out+".gro")
import ctools.GromacsExt.GromacsStructureParser as GromacsStructureParser
GromacsStructureParser.writeStructure(filename_out+".gro")

