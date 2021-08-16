import nibabel as nib

def calc_volume(npath: str, npath_labelled: str):
    """
    npath: 胸腺塗り絵されていないniftiファイルのpath
    npath_labelled: 胸腺塗り絵されているniftiファイルのpath
    これらのnifti画像ファイルを用いて、
    ・axialの軸と胸腺の面積の関係をplot
    ・胸腺の最大断面積
    ・胸腺のCT値の平均値
    を算出する.

    * 胸腺のCT値について
    塗り絵された領域は全て胸腺とは限らないため、
    ・周囲数コマずつ削る
    ・両極端な値を排除して平均値を算出する
    などの手段で精度を高める方針.
    """
    ni_org = nib.load(npath)
    ni_lab = nib.load(npath_labelled)
    img_org = ni_org.get_fdata()
    img_lab = ni_lab.get_fdata()
    print(img_org.shape, img_lab.shape)
    print(type(img_org))

if __name__=="__main__":
    calc_volume("sample.nii.gz","sample_labelled.nii.gz")