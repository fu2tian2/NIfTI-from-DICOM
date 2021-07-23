python3 unzip.py
for f in ~/Desktop/dzip2/output/*
    do
        mkdir $f/NIfTI
        dcm2niix -z y -f %p_%t_%s -o $f/NIfTI $f/*/DCMDT
    done