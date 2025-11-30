"""
Hotel Booking Stream Producer - Azure Event Hub Compatible
"""

import pandas as pd
import json
import time
from datetime import datetime
import os
from azure.eventhub import EventHubProducerClient, EventData

# Konfigürasyon
CSV_FILE = os.getenv('CSV_FILE', 'hotel_raw_stream.csv')
EVENT_HUB_CONNECTION_STRING = os.getenv('EVENT_HUB_CONNECTION_STRING', '')
EVENT_HUB_NAME = os.getenv('EVENT_HUB_NAME', 'hotel-events')
DELAY_SECONDS = float(os.getenv('DELAY_SECONDS', '0.5'))
BATCH_SIZE = int(os.getenv('BATCH_SIZE', '10'))

def send_to_eventstream(producer, events):
    """Event Hub'a event gönder"""
    try:
        event_data_batch = producer.create_batch()
        
        for event in events:
            event_data = EventData(json.dumps(event))
            event_data_batch.add(event_data)
        
        producer.send_batch(event_data_batch)
        return True
        
    except Exception as e:
        print(f"❌ Gönderim hatası: {str(e)}")
        return False

def main():
    print("="*80)
    print("🚀 HOTEL BOOKING STREAM PRODUCER")
    print("="*80)
    print(f"📂 CSV: {CSV_FILE}")
    print(f"🌐 Event Hub: {EVENT_HUB_NAME}")
    print(f"⏱️  Delay: {DELAY_SECONDS}s")
    print(f"📦 Batch: {BATCH_SIZE}")
    print("="*80)
    
    # CSV oku
    try:
        df = pd.read_csv(CSV_FILE)
        print(f"✅ CSV okundu: {len(df):,} satır")
    except FileNotFoundError:
        print(f"❌ HATA: {CSV_FILE} bulunamadı!")
        return
    
    # Event Hub client oluştur
    try:
        producer = EventHubProducerClient.from_connection_string(
            conn_str=EVENT_HUB_CONNECTION_STRING,
            eventhub_name=EVENT_HUB_NAME
        )
        print("✅ Event Hub bağlantısı kuruldu")
    except Exception as e:
        print(f"❌ Bağlantı hatası: {str(e)}")
        return
    
    # Stream simülasyonu
    total_rows = len(df)
    sent_count = 0
    failed_count = 0
    batch = []
    
    print(f"\n🔄 Stream başlıyor... (Ctrl+C ile durdurun)\n")
    
    try:
        for index, row in df.iterrows():
            event = {
                'event_id': f"EVT_{index:09d}",
                'event_timestamp': datetime.utcnow().isoformat() + 'Z',
                'event_type': 'booking_created',
                'data': {k: (str(v) if pd.notna(v) else None) for k, v in row.to_dict().items()}
            }
            
            batch.append(event)
            
            if len(batch) >= BATCH_SIZE:
                if send_to_eventstream(producer, batch):
                    sent_count += len(batch)
                    progress = (sent_count / total_rows) * 100
                    if sent_count % 100 == 0:  # Her 100'de bir log
                        print(f"✅ Gönderildi: {sent_count:,}/{total_rows:,} (%{progress:.1f})")
                else:
                    failed_count += len(batch)
                
                batch = []
                time.sleep(DELAY_SECONDS)
        
        # Son batch
        if batch:
            if send_to_eventstream(producer, batch):
                sent_count += len(batch)
            else:
                failed_count += len(batch)
        
        print("\n" + "="*80)
        print("✅ STREAM TAMAMLANDI!")
        print(f"📊 Gönderilen: {sent_count:,}")
        print(f"❌ Başarısız: {failed_count:,}")
        print("="*80)
        
    except KeyboardInterrupt:
        print("\n⚠️  Stream durduruldu")
        print(f"📊 Gönderilen: {sent_count:,}/{total_rows:,}")
    finally:
        producer.close()

if __name__ == "__main__":
    main()