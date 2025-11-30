import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # perlu di-import untuk 3D

# Path file CSV (pakai raw string biar backslash aman)
csv_path = r"E:\1.Clustering_TA\dataset\Afi\Jalan34.csv"

# Baca data
df = pd.read_csv(csv_path)

# Cek dulu nama kolom (kalau perlu)
print(df.columns)

# Misal nama kolomnya: 'x', 'y', 'z', 'doppler', 'snr'
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    df["x"],
    df["y"],
    df["z"],
    c="red",      # warna titik
    s=5,             # ukuran titik
    alpha=0.8        # transparansi
)

ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Point Cloud Radar")

plt.tight_layout()
plt.show()
