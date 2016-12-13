print("ok")
require('torch')

<<<<<<< HEAD
emb_path = "/media/cheng/Doc/re/embedding/SKIP_GRAM_average_v5_200.th"
=======
emb_path = "/data/che313/reDec2016data/embedding/SKIP_GRAM_average_v5_200.th"
>>>>>>> 3e9372a1104f094d8ecf3150fb339097076ae9eb
emb = torch.load(emb_path)
emb_vecs = emb.M
print(emb_vecs)
