print("ok")
require('torch')

emb_path = "/media/cheng/Doc/re/embedding/SKIP_GRAM_average_v5_200.th"
emb = torch.load(emb_path)
emb_vecs = emb.M
print(emb_vecs)
