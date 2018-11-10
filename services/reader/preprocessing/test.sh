# manual test
# Place your test images in ../../test_images/ 

TEST_IMAGES="../test_images/"
OUT="../out_images/"

if [ ! -d "$OUT" ]; then 
    mkdir -p "$OUT"
fi;

for file in $(ls $TEST_IMAGES); do
    if [[ $file =~ \.jpg$ ]]; then
        echo $file
        python preprocess.py --show --image=$TEST_IMAGES/$file --save=$OUT
    fi;
done;
