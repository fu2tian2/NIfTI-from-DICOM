import pydicom
import glob
import os
import matplotlib.pyplot as plt
from personal_info_deletion import delete_personal_info

##########
# sample dicom files
# https://www.jira-net.or.jp/dicom/dicom_data_01_02.html
##########

"""
現時点ではzip fileを解凍した後、SAMPLE_DIRにあるものだけ処理できるような感じ
今後各zip fileを解凍して個人情報削除して再度zipするコードに書き換えることも可能。
"""

HOME_DIR = '/Users/1sey/Desktop/dzip2'
files = glob.glob(os.path.join(HOME_DIR,"output","*","*"))
SAMPLE_DIR = HOME_DIR + '/output/sample_DICOM3/disk_60B6B512/DCMDT'

files = glob.glob(os.path.join(SAMPLE_DIR, '*'))
# print(files)

SAMPLE_DCM_PATH = files[0]
# print(SAMPLE_DCM_PATH)

# metadataの個人情報を"###"に置き換える
for dcm_path in files:
    delete_personal_info(dcm_path)

# print("-----以下check-----")
# for dcm_path in files:
#     delete_personal_info(dcm_path, save_new=False)