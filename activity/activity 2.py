Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======================================================== RESTART: C:/Users/divya/AppData/Local/Programs/Python/Python313/123.py ========================================================
Traceback (most recent call last):
  File "C:/Users/divya/AppData/Local/Programs/Python/Python313/123.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'

======================================================== RESTART: C:/Users/divya/AppData/Local/Programs/Python/Python313/123.py ========================================================
Traceback (most recent call last):
  File "C:/Users/divya/AppData/Local/Programs/Python/Python313/123.py", line 4, in <module>
    data = pd.read_csv("sales_data.csv")
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'sales_data.csv'

======================================================== RESTART: C:/Users/divya/AppData/Local/Programs/Python/Python313/123.py ========================================================
Traceback (most recent call last):
  File "C:/Users/divya/AppData/Local/Programs/Python/Python313/123.py", line 4, in <module>
    data = pd.read_csv("sales_data.csv")
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'sales_data.csv'

======================================================== RESTART: C:/Users/divya/AppData/Local/Programs/Python/Python313/1234.py =======================================================
Traceback (most recent call last):
  File "C:/Users/divya/AppData/Local/Programs/Python/Python313/1234.py", line 4, in <module>
    data = pd.read_csv("sales_data.csv")
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\divya\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'sales_data.csv'
>>> 
======================================================== RESTART: C:/Users/divya/AppData/Local/Programs/Python/Python313/1234.py =======================================================
First 5 rows of dataset:
   Order ID  Order Date     Category Region  Sales   Cost
0      1001  2025-01-05  Electronics  North  25000  18000
1      1002  2025-01-07     Clothing  South  12000   8000
2      1003  2025-01-10  Electronics   East  30000  21000
3      1004  2025-01-12  Accessories   West   8000   5000
4      1005  2025-01-15     Clothing  North  15000   9000

Missing values before cleaning:
Order ID      0
Order Date    0
Category      0
Region        0
Sales         0
Cost          0
dtype: int64

Total Sales by Category:
Category
Accessories     30000
Clothing        70000
Electronics    174000
Name: Sales, dtype: int64

Total Sales by Region:
Region
East     83000
North    81000
South    59000
West     51000
Name: Sales, dtype: int64

Monthly Sales Trend:
Month
1    176000
2     98000
Name: Sales, dtype: int64

Pivot Table (Sales by Region and Category):
Category  Accessories  Clothing  Electronics
Region                                      
East             6000     16000        61000
North            9000     15000        57000
South            7000     25000        27000
West             8000     14000        29000

Analysis Completed. Cleaned file saved as 'cleaned_sales_data.csv'
