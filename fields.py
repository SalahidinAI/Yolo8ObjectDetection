import rasterio
from rasterio import shutil as rio_shutil

# Укажи путь к твоему файлу .jp2
input_file = "/Users/salahidin/Downloads/S2C_MSIL2A_20250829T053701_N0511_R005_T43TGH_20250829T090715.SAFE/GRANULE/L2A_T43TGH_A005123_20250829T054026/IMG_DATA/R10m/T43TGH_20250829T053701_TCI_10m.jp2"

# Укажи путь, куда сохранить .tif
output_file = "/Users/salahidin/Downloads/output.tif"

# Открываем исходный .jp2 и копируем в .tif
with rasterio.open(input_file) as src:
    profile = src.profile
    profile.update(driver='GTiff')  # Меняем драйвер на GeoTIFF

    with rasterio.open(output_file, 'w', **profile) as dst:
        dst.write(src.read())

print("✅ Конвертация завершена: JP2 → TIFF")
