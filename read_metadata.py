import pydicom
import glob
import os
import matplotlib.pyplot as plt
from personal_info_deletion import delete_personal_info

##########
# sample dicom files
# https://www.jira-net.or.jp/dicom/dicom_data_01_02.html
##########

HOME_DIR = '/Users/1sey/Desktop/dzip2'

files = glob.glob(os.path.join(HOME_DIR,"output","*","*"))

SAMPLE_DIR = HOME_DIR + '/output/sample_DICOM3/disk_60B6B512/DCMDT'

files = glob.glob(os.path.join(SAMPLE_DIR, '*'))
# print(files)

SAMPLE_DCM_PATH = files[0]
print(SAMPLE_DCM_PATH)

for dcm_path in files:
    delete_personal_info(dcm_path)

print("-----以下check-----")
for dcm_path in files:
    delete_personal_info(dcm_path)