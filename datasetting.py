from glob import glob
import yaml


# train, val dataset list로 불러오기
train_img_list = glob('data/ng_orig/train/images/*.jpg')
val_img_list = glob('data/ng_orig/valid/images/*.jpg')

# 이미지 경로 저장
with open('data/ng_orig/train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')

with open('data/ng_orig/val.txt', 'w') as f:
    f.write('\n'.join(val_img_list) + '\n')

# yaml에 경로 넣어주기

with open('data/ng_orig/data.yaml', 'r') as f:
    data = yaml.safe_load(f)

print(data)

data['train'] = 'data/ng_orig/train.txt'
data['val'] = 'data/ng_orig/val.txt'

with open('data/ng_orig/data.yaml', 'w') as f:
    yaml.dump(data, f)

print(data)
