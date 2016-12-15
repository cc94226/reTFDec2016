import util_StanfordData as utilSIE
import util_loadEmbedding as utilEMB

emb_path = '/home/che313/data/embedding/SKIP_GRAM_200_v5_FIGER_Stanford_0d001_50iter.txt'
test_dir = '/data/che313/reTF2016/bipath_stanford/test/'
max_line = 10000

#test_dataset = utilSIE.read_whole_stanfordIE_data(test_dir,1, max_line, 0)
words_num, emb_size = utilEMB.load_embedding(emb_path)
print words_num, emb_size
