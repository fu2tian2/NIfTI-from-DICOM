import pydicom

def delete_personal_info(dcm_path, save_new=True):
    """
    dcmファイルの個人情報に関わるmetadataを削除する.
    dcm_path: dcmファイルのPATH
    save_new: 上書きするかどうか
    [削除項目]
    (0x0008,0x0014): Instance Creator UID
    (0x0008,0x0018): SOP Instance UID
    (0x0008,0x0020): Study Date
    (0x0008,0x0021): Series Date
    (0x0008,0x0022): Aquisition Date
    (0x0008,0x0050): Accession Number
   	(0x0008,0x0080): Institution Name	
    (0x0008,0x0081): Institution Address
    (0x0008,0x0090): Referring Physician's Name
    (0x0008,0x0092): Referring Physician's Address
    (0x0008,0x0094): Referring Physician's Telephone numbers
    (0x0008,0x1010): Station Name
    (0x0008,0x1030): Study Description
    (0x0008,0x103E): Series Description
    (0x0008,0x1040): Institutional Department name
    (0x0008,0x1048): Physician(s) of Record
    (0x0008,0x1050): Performing Physicians' Name
    (0x0008,0x1060): Name of Physician(s) Reading study
    (0x0008,0x1070): Operator's Name
    (0x0008,0x1080): Admitting Diagnoses Description
    (0x0008,0x1155): Referenced SOP Instance UID
    (0x0008,0x2111): Derivation Description
    (0x0010,0x0010): Patient Name
    (0x0010,0x0020): Patient ID
    (0x0010,0x0030): Patient Birth Date
    (0x0010,0x0032): Patient's Birth Time
    (0x0010,0x1000): Other Patient IDs
    (0x0010,0x1001): Other Patient Names
    (0x0010,0x1010): Patient's Age
    (0x0010,0x1040): Patient Address
    (0x0010,0x1090): Medical Record Locator
    (0x0010,0x2154): Patient Telephone
    (0x0010,0x2160): Ethnic Group
    (0x0010,0x2180): Occupation
    (0x0010,0x21B0): Additional Patient's History
    (0x0010,0x4000): Patient Comments
    (0x0020,0x000D): Study Instance UID
    (0x0020,0x000E): Series Instance UID
    (0x0020,0x0010): Study ID
    (0x0020,0x0052): Frame of Reference UID
    (0x0020,0x0200): Synchronization Frame of Reference UID	
    (0x0020,0x4000): Image Comments	
    (0x0040,0x0275): Request Attributes Sequence
    (0x0040,0xA124): UID
    (0x0040,0xA730): Content Sequence
    (0x0088,0x0140): Storage Media File-set UID	
    (0x3006,0x0024): Referenced Frame of Reference UID
    (0x3006,0x00C2): Related Frame of Reference UID	

    参考文献: 
    https://medschool.duke.edu/sites/medschool.duke.edu/files/field/attachments/Guidance%20for%20research%20DICOM%20images.pdf
    http://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_6.html#table_6-1
    """
    dataset = pydicom.filereader.dcmread(dcm_path)
    # print(type(dataset))

    # 画像表示
    # img = dataset.pixel_array
    # fig, ax = plt.subplots()
    # ax.imshow(img, cmap='gray')
    # ax.set_axis_off()
    # plt.show()

    # 個人情報削除 

    privacy_info_indices = [(0x0008,0x0014),(0x0008,0x0018),(0x0008,0x0020),(0x0008,0x0021),
                            (0x0008,0x0022),(0x0008,0x0050),(0x0008,0x0080),(0x0008,0x0081),
                            (0x0008,0x0090),(0x0008,0x0092),(0x0008,0x0094),(0x0008,0x1010),
                            (0x0008,0x1030),(0x0008,0x103E),(0x0008,0x1040),(0x0008,0x1048),
                            (0x0008,0x1050),(0x0008,0x1060),(0x0008,0x1070),(0x0008,0x1080),
                            (0x0008,0x1155),(0x0008,0x2111),(0x0010,0x0010),(0x0010,0x0020),
                            (0x0010,0x0030),(0x0010,0x0032),(0x0010,0x1000),(0x0010,0x1001),
                            (0x0010,0x1010),(0x0010,0x1040),(0x0010,0x1090),(0x0010,0x2154),
                            (0x0010,0x2160),(0x0010,0x2180),(0x0010,0x21B0),(0x0010,0x4000),
                            (0x0020,0x000D),(0x0020,0x000E),(0x0020,0x0010),(0x0020,0x0052),
                            (0x0020,0x0200),(0x0020,0x4000),(0x0040,0x0275),(0x0040,0xA124),
                            (0x0040,0xA730),(0x0088,0x0140),(0x3006,0x0024),(0x3006,0x00C2)]

    for index in privacy_info_indices:
        try:
            private_value = dataset[index].value
            # print(index,private_value)
            if index==(0x0008,0x0050):
                dataset[index].value = '1111111111111111'
            else:
                dataset[index].value = '###'
        except:
            pass

    # 書き換えたものを上書き保存する
    if save_new:
        dataset.save_as(dcm_path, write_like_original=False)
    return
