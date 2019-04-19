# manual test
# Place your test images in ../../test_images/ 

cd ..
TEST_IMAGES="./test/test_images/"
OUT="./test/out_images/"

if [ ! -d "$OUT" ]; then 
    mkdir -p "$OUT"
fi;

for file in $(ls $TEST_IMAGES); do
    # TODO: add a test for file format *.jpg, *.png, etc.
    echo $file
    python3 -m preprocessing.preprocess --image=$TEST_IMAGES/$file --save=$OUT
done;
