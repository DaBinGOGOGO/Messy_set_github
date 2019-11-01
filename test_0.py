import torch
# from tqdm import tqdm,trange
# import time
# l=list(range(10))
# for i in tqdm(l):
#     print('###',i,'\n')
#     time.sleep(5)

from sklearn.datasets import load_digits
# from MulticoreTSNE import MulticoreTSNE as TSNE
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

digits = load_digits()
print(digits.data.shape)

embeddings = TSNE(n_components=2).fit_transform(digits.data)
print(embeddings.shape)
vis_x = embeddings[:, 0]
vis_y = embeddings[:, 1]

plt.scatter(vis_x, vis_y, c=digits.target, cmap=plt.cm.get_cmap("jet", 10), marker='.')
plt.colorbar(ticks=range(10))
plt.clim(-0.5, 9.5)
plt.show()
