_base_ = '../bmvc2021/yolov3_mvdarknet53_608_30e_db4_AC_sv.py'

# Modify dataset related settings
data = dict(
    train=dict(
        ann_files=['data/db4/db4_train_A_laptop.json', 'data/db4/db4_train_C_laptop.json']),
    val=dict(
        ann_files=['data/db4/db4_test_A_laptop.json', 'data/db4/db4_test_C_laptop.json']),
    test=dict(
        ann_files=['data/db4/db4_test_A_laptop.json', 'data/db4/db4_test_C_laptop.json']))
