emb_path = /data/che313/reDec2016data/embedding/SKIP_GRAM_average_v5_200.th

local emb = torch.load(emb_path)
local emb_vecs = emb.M:double()
local emb_vocab = emb.w2vvocab

print "ok"
