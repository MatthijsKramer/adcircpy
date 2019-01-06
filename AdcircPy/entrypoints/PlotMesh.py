#! /usr/bin/env python
import os
import argparse
import matplotlib.pyplot as plt
from AdcircPy import AdcircPy

class PlotMesh(object):
  def __init__(self):
    self.parse_args()
    self.read_mesh()
    self.plot_mesh()

  def parse_args(self):
    self.args = argparse.ArgumentParser(description="Program to see a quick plot of an ADCIRC mesh.")
    self.args.add_argument("mesh_path",help="ADCIRC mesh file path.")
    self.args = self.args.parse_args()
    
  def read_mesh(self):
    self.fort14 = AdcircPy.read_mesh(self.args.mesh_path)
    
  def plot_mesh(self):
    self.fort14.make_plot()
    plt.show()

def main():
  PlotMesh()

if __name__ == "__main__":
  main()
