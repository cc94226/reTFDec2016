emb_path = "/data/che313/reDec2016data/embedding/SKIP_GRAM_average_v5_200.th"

emb = torch.load(emb_path)
emb_vecs = emb.M
emb_vocab = emb.w2vvocab

print "ok"
