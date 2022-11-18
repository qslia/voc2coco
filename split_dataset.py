import os
import shutil
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import time
imgs = os.listdir('img')
xmls = os.listdir('xml')

train_imgs1, test_imgs1, train_xmls1, test_xmls1 = train_test_split(sorted(imgs),
                                                                    sorted(xmls),
                                                                    train_size=0.05,  # take %5 of dataset to train
                                                                    random_state=42)  # for accelerating training

train_imgs, test_imgs2, train_xmls, test_xmls2 = train_test_split(sorted(train_imgs1),
                                                                  sorted(train_xmls1),
                                                                  test_size=0.3,
                                                                  random_state=42)
val_imgs, test_imgs, val_xmls, test_xmls = train_test_split(sorted(test_imgs2),
                                                            sorted(test_xmls2),
                                                            test_size=0.5,
                                                            random_state=42)

for item11 in ['img', 'xml']:

    os.makedirs(f'{item11}s')

    for dir1 in ['train', 'test', 'val']:
        os.makedirs(dir1)

    for item1 in ['train', 'test', 'val']:
        for item in tqdm(eval(f'{item1}_{item11}s')):
            src = os.path.join(os.path.abspath(f'{item11}'), item)
            dst = f'{item1}'
            shutil.copy(src, dst)

    for item1 in ['train', 'test', 'val']:
        shutil.move(f'{item1}', f'{item11}s')

os.mkdir('dataset')
time.sleep(1)
shutil.move('imgs', 'dataset')
time.sleep(1)
shutil.move('xmls', 'dataset')

print('Done!')
