# coding: utf-8
# -----------------------------------------------------------------------------
# Copyright 2015 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

# ==================================================
# ImportWMOStationsTestCase.py
# --------------------------------------------------
# requirements:
# * ArcGIS Desktop 10.X+
# * Python 2.7
#
# author: ArcGIS Solutions
# company: Esri
#
# ==================================================
# history:
# 2/10/2016 - JH - initial creation
# ==================================================

import unittest
import arcpy
import os
import UnitTestUtilities
import Configuration
import DataDownload

class ImportWMOStationsTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Import WMO Station Data tool
    in the Military Aspects of Weather toolbox'''
    
    def setUp(self):
        if Configuration.DEBUG == True: print("     ImportWMOStationsTestCase.setUp")
        UnitTestUtilities.checkArcPy()
        Configuration.suitabilityDataPath = os.path.join(Configuration.suitabilityPaths, "data")
        if (Configuration.suitabilityScratchGDB == None) or (not arcpy.Exists(Configuration.suitabilityScratchGDB)):
            Configuration.suitabilityScratchGDB = UnitTestUtilities.createScratch(Configuration.suitabilityDataPath)
        UnitTestUtilities.checkFilePaths([Configuration.suitabilityDataPath, Configuration.maow_ToolboxPath])
        # scratch GDB needed for output
    
    def tearDown(self):
        if Configuration.DEBUG == True: print("     ImportWMOStationsTestCase.tearDown")
        UnitTestUtilities.deleteScratch(Configuration.suitabilityScratchGDB)
        
    def test_import_wmo_stations(self):
        if Configuration.DEBUG == True: print("     ImportWMOStationsTestCase.test_import_wmo_stations")
        arcpy.AddMessage("Testing Import WMO Stations (Desktop)")
        
        runToolMessage = "Running tool (Import WMO Stations)"
        arcpy.AddMessage(runToolMessage)
        Configuration.Logger.info(runToolMessage)
            