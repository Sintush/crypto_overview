from unittest import TestCase
import pandas as pd

from utils import get_coin_gecko


class Test(TestCase):
    def test_modify_gecko_output_bitcoin(self):
        output = {'prices': [[1617660264773, 49674.85095040552], [1617678076379, 49778.07780010743], [1617681629319, 49792.74339302505]],
                  'market_caps': [[1617660264773, 926710114195.2921], [1617663905558, 930836263082.8783], [1617667493830, 929741397057.1488]],
                  'total_volumes': [[1617660264773, 45463084914.035355], [1617663905558, 46089370002.64161], [1617667493830, 46593832173.03431]]}

        actual = get_coin_gecko.modify_gecko_output(output, 1.2, 'bitcoin')

        excpected = pd.DataFrame({
            'Date': ['2021-04-05 22:04:24.773', '2021-04-06 03:01:16.379', '2021-04-06 04:00:29.319'],
            'Price': [59609.821140, 59733.693360, 59751.292072],
            'Crypto': ['bitcoin', 'bitcoin', 'bitcoin']
        })
        excpected['Date'] = pd.to_datetime(excpected['Date'])

        self.assertEqual(str(actual), str(excpected))


class Test(TestCase):
    def test_modify_gecko_output_aave(self):
        output = {'prices': [[1617823152789, 292.1640975342869], [1617823475524, 291.3576766754107], [1617823738208, 293.7514223780491]],
                  'market_caps': [[1617823152789, 3659351660.198075], [1617823475524, 3638026584.116122], [1617823738208, 3638026584.116122]],
                  'total_volumes': [[1617823152789, 565676183.153785], [1617823475524, 565629218.7042856], [1617823738208, 572507511.4749027]]}

        actual = get_coin_gecko.modify_gecko_output(output, 0.00002, 'aave')

        excpected = pd.DataFrame({
            'Date': ['2021-04-07 19:19:12.789', '2021-04-07 19:24:35.524', '2021-04-07 19:28:58.208'],
            'Price': [0.005843, 0.005827, 0.005875],
            'Crypto': ['aave', 'aave', 'aave']
        })
        excpected['Date'] = pd.to_datetime(excpected['Date'])

        self.assertEqual(str(actual), str(excpected))
