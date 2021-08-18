import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class ThymusCalculator:
    def calc_volume(self,npath: str, npath_labelled: str):
        """
        npath: 胸腺塗り絵されていないniftiファイルのpath
        npath_labelled: 胸腺塗り絵されているniftiファイルのpath
        これらのnifti画像ファイルを用いて、
        ・axialの軸と胸腺の面積の関係をplot
        ・胸腺の最大断面積
        を算出する.
        """
        ni_org = nib.load(npath)
        ni_lab = nib.load(npath_labelled)
        img_org = ni_org.get_fdata()
        img_lab = ni_lab.get_fdata()
        # print(img_org.shape, img_lab.shape)
        square_array = [0 for _ in range(len(img_org[0][0]))]
        for axind in range(len(img_org[0][0])):
            slice_val = img_org[:,:,axind]
            slice_lab = img_lab[:,:,axind]
            for i in range(len(slice_val)):
                for j in range(len(slice_val[0])):
                    if (slice_lab[i][j]==4):
                        square_array[axind]+=1
        ax_array = [i+1 for i in range(len(img_org[0][0]))]
        # 軸断面ごとの胸腺の面積
        plt.plot(ax_array,square_array)
        plt.title('max area: '+str(max(square_array)))
        plt.savefig('thymus_area.png')
        return

    def calc_ct_value(self,npath:str,npath_labelled:str):
        """ 
        入力は上記関数と同様. 胸腺のCT値の平均値を算出する.
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
        ct_value_array = []
        for axind in range(len(img_org[0][0])):
            slice_val = img_org[:,:,axind]
            slice_lab = img_lab[:,:,axind]
            for i in range(len(slice_val)):
                for j in range(len(slice_val[0])):
                    if (slice_lab[i][j]==4):
                        ct_value_array.append(slice_val[i][j])
        ct_value_mean = stats.trim_mean(np.array(ct_value_array),0.05)
        print(ct_value_mean)
        
    def _validate_index(self, ni_org, x:int, y:int, z:int):
        """
        validなindexかどうか判定
        """
        if (x<0) | (len(ni_org)<=x):
            return False
        if (y<0) | (len(ni_org[0])<=y):
            return False
        if (z<0) | (len(ni_org[0][0])<=z):
            return False
        return True
        


if __name__=="__main__":
    tc = ThymusCalculator()
    tc.calc_volume("sample.nii.gz","sample_labelled.nii.gz")
    tc.calc_ct_value("sample.nii.gz","sample_labelled.nii.gz")