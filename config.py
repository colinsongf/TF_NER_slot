import os
from general_utils import get_logger


class Config():
    def __init__(self):
        # directory for training outputs
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        # create instance of logger
        self.logger = get_logger(self.log_path)

    # general config
    output_path = "results/crf/"
    model_output = output_path + "model.weights/"
    log_path = output_path + "log.txt"

    # embeddings
    dim = 300
    dim_char = 100
    glove_filename = "../data/glove.6B/glove.6B.{}d.txt".format(dim)

    # trimmed embeddings (created from glove_filename with build_data.py)
    trimmed_filename = "../data/glove.6B.{}d.trimmed.npz".format(dim)

    # dataset
    dev_filename = "../data/dev.tsv"
    test_filename = "../data/test.tsv"
    train_filename = "../data/train.tsv"
    max_iter = None  # if not None, max number of examples

    # vocab (created from dataset with build_data.py)
    words_filename = "../data/words.txt"
    tags_filename = "../data/tags.txt"
    chars_filename = "../data/chars.txt"

    # training
    train_embeddings = False
    nepochs = 15
    dropout = 0.5
    batch_size = 20
    lr_method = "adam"
    lr = 0.001
    lr_decay = 0.9
    clip = -1  # if negative, no clipping
    nepoch_no_imprv = 3
    reload = False

    # model hyperparameters
    hidden_size = 300
    char_hidden_size = 100

    # NOTE: if both chars and crf, only 1.6x slower on GPU
    crf = True  # if crf, training is 1.7x slower on CPU
    chars = True  # if char embedding, training is 3.5x slower on CPU

    # build dev data
    dev_ratio = 0.4
    build_dev_from_trainset = False
    build_dev_from_testset = True