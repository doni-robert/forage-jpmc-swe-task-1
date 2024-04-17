import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_result_ABC = ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2)
    expected_result_DEF = ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    
    self.assertEqual(getDataPoint(quotes[0]), expected_result_ABC)
    self.assertEqual(getDataPoint(quotes[1]), expected_result_DEF)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    expected_result_ABC = ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2)
    expected_result_DEF = ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    
    self.assertEqual(getDataPoint(quotes[0]), expected_result_ABC)
    self.assertEqual(getDataPoint(quotes[1]), expected_result_DEF)


if __name__ == '__main__':
    unittest.main()
