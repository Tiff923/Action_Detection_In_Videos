import random
import torch

from torchvision.transforms import (
    Compose, ToTensor, ToPILImage, Normalize, Resize, Pad, Lambda, RandomApply,
    RandomChoice, RandomOrder, RandomErasing, RandomRotation, RandomPerspective,  
    LinearTransformation, RandomAffine, RandomHorizontalFlip, RandomVerticalFlip, 
    RandomCrop, RandomResizedCrop, CenterCrop, FiveCrop, TenCrop, ColorJitter,
    Grayscale, RandomGrayscale, 
)

from torchvision.transforms._transforms_video import (
    RandomCropVideo, RandomResizedCropVideo, CenterCropVideo,
    NormalizeVideo, RandomHorizontalFlipVideo,
)

from . import functional as F

class SelectFrame(object):
    def __init__(self, idx):
        self.idx = idx
    
    def __call__(self, clip):
        return clip[self.idx]

class FirstFrame(SelectFrame):
    def __init__(self):
        super().__init__(0)

class LastFrame(SelectFrame):
    def __init__(self):
        super().__init__(-1)

class RandomFrame(object):
    def __call__(self, clip):
        return F.select_random_frame(clip)

class RandomFrames(object):
    def __init__(self, num_frames):
        self.num_frames = num_frames
    
    def __call__(self, clip):
        return F.select_random_frames(clip, self.num_frames)

class RandomTrim(object):
    def __init__(self, num_frames):
        self.num_frames = num_frames
    
    def __call__(self, clip):
        return F.select_random_trim(clip, self.num_frames)

class ToTensorVideo(object):
    def __call__(self, clip):
        return F.to_tensor_video(clip)

class ToOpticalFlow(object):
    def __call__(self, clip):
        return F.to_optical_flow(clip)