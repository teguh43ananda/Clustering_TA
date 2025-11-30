import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

from mpl_toolkits.mplot3d import Axes3D  # hanya untuk memastikan 3D aktif

# --- 1. BACA DATA ---
file_path = r"E:\1.Clustering_TA\dataset\Afi\Jalan1.csv"  # ganti sesuai file kamu
df = pd.read_csv(file_path)

# --- 2. PILIH FITUR UNTUK CLUSTERING (XYZ SAJA) ---
X = df[['x', 'y', 'z']].values

# (Opsional) kalau datanya sangat besar, bisa di-sample:
# X = X[::5]  # ambil tiap 5 titik saja

# --- 3. JALANKAN DBSCAN ---
dbscan = DBSCAN(eps=0.25, min_samples=5)  # nilai awal, nanti kita tuning
labels = dbscan.fit_predict(X)

# --- 4. PLOT 3D HASIL CLUSTERING ---
unique_labels = np.unique(labels)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for lab in unique_labels:
    mask = labels == lab
    pts = X[mask]

    if lab == -1:
        # noise / outlier
        ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2],
                   s=5, c='k', alpha=0.3, label='noise' if lab == -1 else None)
    else:
        ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2],
                   s=8, alpha=0.8, label=f'Cluster {lab}')

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.legend(loc='upper right')
plt.title('DBSCAN Clustering Point Cloud')
plt.show()
