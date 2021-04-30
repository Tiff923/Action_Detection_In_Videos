import os
from models.finetuned_resnet import finetuned_resnet
from model_processing import model_processing

N_CLASSES = 174
IMSIZE = (216, 216, 3)


if __name__ == '__main__':
    src_dir = '/home/changan/ActionRecognition_rnn/data/UCF-Preprocessed'
    dest_dir = '/home/changan/ActionRecognition_rnn/data/CNN_Predicted'
    weights_dir = '/home/changan/ActionRecognition_rnn/models'

    finetuned_resnet_weights = os.path.join(weights_dir, 'finetuned_resnet.h5')
    model = finetuned_resnet(N_CLASSES, weights_dir=finetuned_resnet_weights, include_top=False)

    TIMESEQ_LEN = 10
    model_processing(model, src_dir, dest_dir, TIMESEQ_LEN)