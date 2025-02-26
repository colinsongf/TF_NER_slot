from data_utils import get_trimmed_glove_vectors, load_vocab, \
    get_processing_word, Dataset, clear_data_path
from model import NERModel
from config import Config

# create instance of config
config = Config()

# load vocabs
vocab_words = load_vocab(config.words_filename)
vocab_tags = load_vocab(config.tags_filename)
vocab_chars = load_vocab(config.chars_filename)

# get processing functions
processing_word = get_processing_word(
    vocab_words, vocab_chars, lowercase=True, chars=config.chars)
processing_tag = get_processing_word(vocab_tags, lowercase=False)

# get pre trained embeddings
embeddings = get_trimmed_glove_vectors(config.trimmed_filename)

# create dataset
dev = Dataset(
    clear_data_path(config.dev_filename), processing_word, processing_tag,
    config.max_iter)
test = Dataset(
    clear_data_path(config.test_filename), processing_word, processing_tag,
    config.max_iter)
train = Dataset(
    clear_data_path(config.train_filename), processing_word, processing_tag,
    config.max_iter)

# build model
model = NERModel(
    config, embeddings, ntags=len(vocab_tags), nchars=len(vocab_chars))
# build graph
model.build()

# train, evaluate and interact
model.train(train, dev, vocab_tags)
model.evaluate(test, vocab_tags)
model.interactive_shell(vocab_tags, processing_word)
