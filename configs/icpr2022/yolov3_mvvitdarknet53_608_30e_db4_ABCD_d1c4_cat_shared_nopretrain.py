_base_ = 'yolov3_mvvitdarknet53_608_30e_db4_ABCD_sv_nopretrain.py'
model = dict(
    backbone=dict(
        combination_block=4,
        num_decoder_layers=1,
        shared_transformer=True,
        multiview_decoder_mode='cat',
    )
)