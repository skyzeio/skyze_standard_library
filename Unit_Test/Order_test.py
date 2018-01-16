"""Created on 30 / 12 / 2017 @author: michaelnew"""


# Standard Libraries

# Skyze libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *

# Skyze libraries - Test Case Specific
from Skyze_Standard_Library.Order import *


class TradingPair_test(UnitTestSkyzeAbstract):
  """Test the Triangular Arbitrage Strategy Class"""

  _package_name = "Skyze_Strategies_Library"

  def _printParameters(self,
                       p_exchanges,
                       p_excluded_markets,
                       p_arb_margin):
    parameters = "\tp_exchanges:\t" + str(p_exchanges) + \
                 "\tp_excluded_markets:\t" + str(p_excluded_markets) + \
                 "\tp_arb_margin:\t" + str(p_arb_margin)
    print(parameters + "\n")

  def test_equility(self):

    class_tested = "Order"
    test_columns = []

    # Test Data
    separator = "_"
    test_data = {'amount': 10.0,
                 'average': 0.0,
                 'datetime': '2018-01-15T21:44:04.698Z',
                 'fee': None,
                 'filled': 0.0,
                 'id': '7216227905',
                 'info': {'avg_execution_price': '0.0',
                          'cid': 78243675637,
                          'cid_date': '2018-01-15',
                          'exchange': 'bitfinex',
                          'executed_amount': '0.0',
                          'gid': None,
                          'id': 7216227905,
                          'is_cancelled': False,
                          'is_hidden': False,
                          'is_live': True,
                          'oco_order': None,
                          'order_id': 7216227905,
                          'original_amount': '10.0',
                          'price': '53.572',
                          'remaining_amount': '10.0',
                          'side': 'buy',
                          'src': 'api',
                          'symbol': 'qtmusd',
                          'timestamp': '1516052643.698736796',
                          'type': 'exchange market',
                          'was_forced': False},
                 'price': 53.572,
                 'remaining': 10.0,
                 'side': 'buy',
                 'status': 'open',
                 'symbol': 'QTUM/USD',
                 'timestamp': 1516052643698,
                 'type': 'market',
                 'mike': 'mike'}

    target_results = test_data

    # Output Headings
    self.printTestHeader(self._package_name, class_tested,
                         "internal", "internal", test_columns)

    # Output test data
    print("\n\n======= Test Data =================================== ")
    print(str(test_data) + "\n\n")

    # Output target_file
    print("\n\n======= Target Reulsts =================================== ")
    print(str(target_results) + "\n\n")

    # ========= Calcualte =============================================
    order = Order(test_data)
    test_calcs = order.__dict__

    # Output target_file
    print("\n\n======= Test Reulsts =================================== ")
    print("Test Calc: " + str(test_calcs))

    # Assert list of pairs the same
    assert(test_calcs == target_results)


if __name__ == '__main__':
  unittest.main()
