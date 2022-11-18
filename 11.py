import os
from pathlib import Path
import shutil
from tqdm import tqdm
for dir5 in ['img', 'xml']:
    if not os.path.exists(dir5):
        os.makedirs(dir5)
path = Path('LogoDet-3K')
root = os.listdir(path)
for dir1 in tqdm(root):
    dir2 = os.listdir(path/dir1)
    for dir3 in dir2:
        files = os.listdir(path/dir1/dir3)
        if files:
            for file in files:
                new_file = f'{dir1}_{dir3}_{file}'.replace(' ', '')
                if new_file.endswith('.xml'):
                    src_path = Path(os.path.abspath(path)) / dir1 / dir3 / file
                    dst_path = Path(os.path.abspath('xml')) / new_file
                    shutil.copy(src_path, dst_path)
                elif new_file.endswith('.jpg'):
                    src_path = Path(os.path.abspath(path)) / dir1 / dir3 / file
                    dst_path = Path(os.path.abspath('img')) / new_file
                    shutil.copy(src_path, dst_path)
        # break
    # break

print('Done')