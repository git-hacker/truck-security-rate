# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:36:47 2018

@author: pierr
"""

import rpy2
print(rpy2.__version__)

from rpy2.robjects.packages import importr
# import R's "base" package
base = importr('base')

# import R's "utils" package
utils = importr('utils')

# R package names
packnames = ('mongolite', 'lubridate')

# R vector of strings
from rpy2.robjects.vectors import StrVector

utils.install_packages(StrVector(packnames))

rpy2.robjects.r('''
                # Load libraries
                library(dplyr)
                library(mongolite)
                library(lubridate)

                f <- function(verbose=FALSE) {
                        # setup connection for drivers/drivers profile
                        con <- mongo(collection = "DriversTrucks",
                             db = "HackDB01",
                             url = "mongodb://localhost",
                             verbose = FALSE)

                        driverstrucks <- con$find(query = '{}', field = '{}')

                        #setup connection for goods
                        con <- mongo(collection = "Goods",
                                     db = "HackDB01",
                                     url = "mongodb://localhost",
                                     verbose = FALSE)

                        goods <- con$find(query = '{}', field = '{}')
                
                        # Merge dataset left on goods
                        df <- goods %>%
                            left_join(driverstrucks, by = c("t_id" = "_id"))
                        
                        print(head(df))
                        }
                
                f()
                '''
                )
                