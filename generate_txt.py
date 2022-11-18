import os
from pathlib import Path
import shutil
for item in ['train', 'test', 'val']:
    test_images_path = Path(f'dataset/xmls/{item}')
    files = os.listdir(test_images_path)
    with open(f'{item}.txt', 'w') as f:
        for file in files:
            line = file.rsplit('.', 1)[0] + '\n'
            f.write(line)
    shutil.copy(f'{item}.txt', 'sample/dataset_ids/')
    os.remove(f'{item}.txt')



