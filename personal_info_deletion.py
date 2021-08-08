import pydicom

def delete_personal_info(dcm_path, save_new=True):
    """
    dcmファイルの個人情報に関わるmetadataを削除する.
    dcm_path: dcmファイルのPATH
    save_new: 上書きするかどうか
    (0008,0020): study date
    (0008,0021): series date
    (0008,0022): aquisition date
    (0008,0050): accession number
    (0010,0010): patient name
    (0010,0020): patient id
    (0010,0030): patient birth date
    (0010,1000): other patient ids
    (0010,1040): patient address
    (0010,2154): patient telephone
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

    privacy_info_indices = [(0x0008,0x0020),(0x0008,0x0021),(0x0008,0x0022),(0x0008,0x0050),(0x0010,0x0010),
                            (0x0010,0x0020),(0x0010,0x0030),(0x0010,0x1000),(0x0010,0x1040),(0x0010,0x2154)]

    for index in privacy_info_indices:
        try:
            private_value = dataset[index].value
            # print(index,private_value)
            dataset[index].value = '###'
        except:
            pass

    # 書き換えたものを上書き保存する
    if (save_new):
        dataset.save_as(dcm_path, write_like_original=False)
    return