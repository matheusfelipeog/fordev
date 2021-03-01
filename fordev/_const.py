# -*- coding: utf-8 -*-
"""All constants using in fordev module."""

from .__about__ import __version__
from .__about__ import __author__
from .__about__ import __email__
from .__about__ import __github__


# -------------- fordev request --------------
LIST_OF_USER_AGENT: list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2)',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 OPR/65.0.3467.78',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.64',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko)',
]

URL_4DEV_API: str = 'https://www.4devs.com.br/ferramentas_online.php'


# -------------- fordev generator --------------
ALL_UF_CODE: list = [
    "AC", "AL", "AP", "AM", "BA", "CE", "ES", "GO", "MA",
    "MT", "MS", "MG","PA", "PB", "PR", "PE", "PI", "RJ",
    "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO", "DF"
]

ALL_VEHICLE_BRANDS: dict = {
    1: {'brand_name': 'Acura', 'code': 1},
    2: {'brand_name': 'Agrale', 'code': 2},
    3: {'brand_name': 'Alfa Romeo', 'code': 3},
    4: {'brand_name': 'AM Gen', 'code': 4},
    5: {'brand_name': 'Asia Motors', 'code': 5},
    6: {'brand_name': 'ASTON MARTIN', 'code': 189},
    7: {'brand_name': 'Audi', 'code': 6},
    8: {'brand_name': 'BMW', 'code': 7},
    9: {'brand_name': 'BRM', 'code': 8},
    10: {'brand_name': 'Buggy', 'code': 9},
    11: {'brand_name': 'Bugre', 'code': 123},
    12: {'brand_name': 'Cadillac', 'code': 10},
    13: {'brand_name': 'CBT Jipe', 'code': 11},
    14: {'brand_name': 'CHANA', 'code': 136},
    15: {'brand_name': 'CHANGAN', 'code': 182},
    16: {'brand_name': 'CHERY', 'code': 161},
    17: {'brand_name': 'Chrysler', 'code': 12},
    18: {'brand_name': 'Citroen', 'code': 13},
    19: {'brand_name': 'Cross Lander', 'code': 14},
    20: {'brand_name': 'Daewoo', 'code': 15},
    21: {'brand_name': 'Daihatsu', 'code': 16},
    22: {'brand_name': 'Dodge', 'code': 17},
    23: {'brand_name': 'EFFA', 'code': 147},
    24: {'brand_name': 'Engesa', 'code': 18},
    25: {'brand_name': 'Envemo', 'code': 19},
    26: {'brand_name': 'Ferrari', 'code': 20},
    27: {'brand_name': 'Fiat', 'code': 21},
    28: {'brand_name': 'Fibravan', 'code': 149},
    29: {'brand_name': 'Ford', 'code': 22},
    30: {'brand_name': 'FOTON', 'code': 190},
    31: {'brand_name': 'Fyber', 'code': 170},
    32: {'brand_name': 'GEELY', 'code': 199},
    33: {'brand_name': 'GM - Chevrolet', 'code': 23},
    34: {'brand_name': 'GREAT WALL', 'code': 153},
    35: {'brand_name': 'Gurgel', 'code': 24},
    36: {'brand_name': 'HAFEI', 'code': 152},
    37: {'brand_name': 'Honda', 'code': 25},
    38: {'brand_name': 'Hyundai', 'code': 26},
    39: {'brand_name': 'Isuzu', 'code': 27},
    40: {'brand_name': 'JAC', 'code': 177},
    41: {'brand_name': 'Jaguar', 'code': 28},
    42: {'brand_name': 'Jeep', 'code': 29},
    43: {'brand_name': 'JINBEI', 'code': 154},
    44: {'brand_name': 'JPX', 'code': 30},
    45: {'brand_name': 'Kia Motors', 'code': 31},
    46: {'brand_name': 'Lada', 'code': 32},
    47: {'brand_name': 'LAMBORGHINI', 'code': 171},
    48: {'brand_name': 'Land Rover', 'code': 33},
    49: {'brand_name': 'Lexus', 'code': 34},
    50: {'brand_name': 'LIFAN', 'code': 168},
    51: {'brand_name': 'LOBINI', 'code': 127},
    52: {'brand_name': 'Lotus', 'code': 35},
    53: {'brand_name': 'Mahindra', 'code': 140},
    54: {'brand_name': 'Maserati', 'code': 36},
    55: {'brand_name': 'Matra', 'code': 37},
    56: {'brand_name': 'Mazda', 'code': 38},
    57: {'brand_name': 'Mercedes-Benz', 'code': 39},
    58: {'brand_name': 'Mercury', 'code': 40},
    59: {'brand_name': 'MG', 'code': 167},
    60: {'brand_name': 'MINI', 'code': 156},
    61: {'brand_name': 'Mitsubishi', 'code': 41},
    62: {'brand_name': 'Miura', 'code': 42},
    63: {'brand_name': 'Nissan', 'code': 43},
    64: {'brand_name': 'Peugeot', 'code': 44},
    65: {'brand_name': 'Plymouth', 'code': 45},
    66: {'brand_name': 'Pontiac', 'code': 46},
    67: {'brand_name': 'Porsche', 'code': 47},
    68: {'brand_name': 'RAM', 'code': 185},
    69: {'brand_name': 'RELY', 'code': 186},
    70: {'brand_name': 'Renault', 'code': 48},
    71: {'brand_name': 'Rolls-Royce', 'code': 195},
    72: {'brand_name': 'Rover', 'code': 49},
    73: {'brand_name': 'Saab', 'code': 50},
    74: {'brand_name': 'Saturn', 'code': 51},
    75: {'brand_name': 'Seat', 'code': 52},
    76: {'brand_name': 'SHINERAY', 'code': 183},
    77: {'brand_name': 'smart', 'code': 157},
    78: {'brand_name': 'SSANGYONG', 'code': 125},
    79: {'brand_name': 'Subaru', 'code': 54},
    80: {'brand_name': 'Suzuki', 'code': 55},
    81: {'brand_name': 'TAC', 'code': 165},
    82: {'brand_name': 'Toyota', 'code': 56},
    83: {'brand_name': 'Troller', 'code': 57},
    84: {'brand_name': 'Volvo', 'code': 58},
    85: {'brand_name': 'VW - VolksWagen', 'code': 59},
    86: {'brand_name': 'Wake', 'code': 163},
    87: {'brand_name': 'Walk', 'code': 120}
}

ALL_BANK_FLAGS: dict = {
    1: 'master',
    2: 'visa16',
    3: 'amex',
    4: 'diners',
    5: 'discover',
    6: 'enroute',
    7: 'jcb',
    8: 'voyager',
    9: 'hiper',
    10: 'aura'
}

ALL_BANK_FLAGS_2: dict = {
    1: 'MasterCard',
    2: 'Visa',
    3: 'Visa Electron',
    4: 'American Express',
    5: 'Diners Club',
    6: 'Discover',
    7: 'Enroute',
    8: 'JCB',
    9: 'Maestro',
    10: 'Solo',
    11: 'Switch',
    12: 'LaserCard'
}
