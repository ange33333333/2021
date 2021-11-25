checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type="TextLoggerHook"),
        # dict(type='TensorboardLoggerHook')
    ],
)
# yapf:enable
custom_hooks = [dict(type="NumClassCheckHook")]

dist_params = dict(backend="nccl")
log_level = "INFO"
load_from = "https://download.openmmlab.com/mmdetection/v2.0/cascade_rcnn/cascade_mask_rcnn_r50_fpn_mstrain_3x_coco/cascade_mask_rcnn_r50_fpn_mstrain_3x_coco_20210628_164719-5bdc3824.pth"
resume_from = None
workflow = [("train", 1), ("val", 1)]
