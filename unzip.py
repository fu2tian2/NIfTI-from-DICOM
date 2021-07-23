import zipfile, os, glob

# zipfile解凍
zip_dir = '/Users/1sey/Desktop/dzip2' # zipfileをまとめて入れるdirectory

script_dir = os.path.dirname(__file__)
out_dir = os.path.join(script_dir, 'output')

files = glob.glob(zip_dir+"/*.zip")
for f in files:
  print("unzip:", f)
  base = os.path.basename(f).replace(".zip", "")
  unzip_path = os.path.join(out_dir, base)
  with zipfile.ZipFile(f, 'r') as f:
     f.extractall(unzip_path)

# metadata操作とか
