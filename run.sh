
for i in train test val
do
  python voc2coco.py \
      --ann_dir dataset/xmls/$i \
      --ann_ids sample/dataset_ids/$i.txt \
      --labels sample/labels.txt \
      --output sample/$i.json \
      --ext xml
done