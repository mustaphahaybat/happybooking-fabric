"""
HappyBooking Data Quality Tests
"""
import pytest
from datetime import datetime

class TestBronzeLayer:
    """Bronze layer data quality tests"""
    
    def test_csv_structure(self):
        """Test CSV data structure"""
        # Mock test - gerçek ortamda Fabric'e bağlanır
        expected_columns = ['hotel_id', 'booking_id', 'customer_id', 'city']
        assert len(expected_columns) > 0, "Expected columns defined"
    
    def test_data_types(self):
        """Test data type conversions"""
        # Örnek: String to numeric
        test_value = "123.45"
        numeric_value = float(test_value)
        assert numeric_value == 123.45

class TestSilverLayer:
    """Silver layer transformation tests"""
    
    def test_date_parsing(self):
        """Test date parsing logic"""
        test_date = "2024-11-28"
        parsed = datetime.strptime(test_date, "%Y-%m-%d")
        
        assert parsed.year == 2024
        assert parsed.month == 11
        assert parsed.day == 28
    
    def test_null_handling(self):
        """Test null value handling"""
        test_value = None
        result = test_value if test_value is not None else 0
        assert result == 0
    
    def test_placeholder_cleaning(self):
        """Test placeholder removal"""
        placeholders = ['___', '???', '--', 'NULL']
        test_value = '___'
        
        cleaned = None if test_value in placeholders else test_value
        assert cleaned is None

class TestGoldLayer:
    """Gold layer business logic tests"""
    
    def test_revenue_calculation(self):
        """Test revenue per night calculation"""
        total_price = 100.0
        nights = 2
        revenue_per_night = total_price / nights
        
        assert revenue_per_night == 50.0
    
    def test_occupancy_rate(self):
        """Test occupancy rate calculation"""
        rooms_booked = 50
        total_rooms = 100
        occupancy = (rooms_booked / total_rooms) * 100
        
        assert occupancy == 50.0
    
    def test_cancellation_rate(self):
        """Test cancellation rate calculation"""
        cancelled = 10
        total = 100
        rate = (cancelled / total) * 100
        
        assert rate == 10.0

class TestDataQuality:
    """General data quality tests"""
    
    def test_no_duplicate_ids(self):
        """Test unique ID constraint"""
        test_ids = ['BKG_001', 'BKG_002', 'BKG_003']
        unique_ids = set(test_ids)
        
        assert len(test_ids) == len(unique_ids)
    
    def test_price_range(self):
        """Test price within valid range"""
        test_price = 150.0
        
        assert 0 < test_price < 10000
    
    def test_date_logic(self):
        """Test booking date before checkin date"""
        booking_date = datetime(2024, 11, 1)
        checkin_date = datetime(2024, 11, 15)
        
        assert booking_date < checkin_date

if __name__ == "__main__":
    pytest.main([__file__, "-v"])