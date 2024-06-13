

#Test Automation

"""
Feature lists:
1.5GC000433
2.5GC000430
3.CB008655
4.CB009226

"""


"""
5GC000433

5GC000433_01_Feature_Actiovation
5GC000433_02_Feature_Deactivation
5GC000433_03_PM_Counter_Update

"""

"""
Case1: 5GC000433_01_Feature_Actiovation
Step1: login to WebUI
Step2: Activate 5GC000433 feature
MRBTS/MNL/MNLENT/FEATCADM.actPowerMeter=true
MRBTS/NRBTS/NRPMRNL.mtBtsEnergyMonitoring=15min
MRBTS/NRBTS/NRPMRNL.mtSBTSSmEnergyMonitoring=15min
MRBTS/NRBTS/NRPMRNL.mtSBTSRfmEnergyMonitoring=15min
Step3: Waiting for 15 minutes, check if PM counter is updated
Step4: Collect Log and analyze

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


testline_ip = "10.101.48.132"


print("Case1: 5GC000433_01_Feature_Actiovation")
print("Step1: login to WebUI")

driver = webdriver.Edge()
driver.get("http://www.python.org")


print("Step2: Activate 5GC000433 feature")

print("Step3: Waiting for 15 minutes, check if PM counter is updated")
print("Step4: Collect Log and analyze")
