import pandas as pd
import os

# Mevcut klasörü kontrol et
print(f"Çalışma klasörü: {os.getcwd()}")
print(f"Klasördeki dosyalar: {os.listdir('.')}")

# CSV'yi oku (aynı klasörde olduğundan direkt isim yeterli)
df = pd.read_csv('hotel_raw.csv')

print(f"\n✅ CSV okundu!")
print(f"Toplam satır sayısı: {len(df)}")
print(f"Toplam sütun sayısı: {len(df.columns)}")
print(f"İlk 5 sütun: {df.columns[:5].tolist()}")

# %70 batch, %30 stream olarak böl
split_point = int(len(df) * 0.7)

batch_df = df.iloc[:split_point]
stream_df = df.iloc[split_point:]

# Kaydet
batch_df.to_csv('hotel_raw_batch.csv', index=False)
stream_df.to_csv('hotel_raw_stream.csv', index=False)

print(f"\n📊 Sonuçlar:")
print(f"Batch veri: {len(batch_df)} satır → hotel_raw_batch.csv")
print(f"Stream veri: {len(stream_df)} satır → hotel_raw_stream.csv")
print("✅ Veri bölme tamamlandı!")