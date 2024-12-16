import xarray as xr
import numpy as np
import pandas as pd

class readNC():
    def __init__(self, nc_file):
        self.nc_file = nc_file
        self.data = xr.open_dataset(nc_file) 