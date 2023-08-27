In [7]: import pyarrow as pa

In [8]: data = list("abc")

In [9]: ser_sd = pd.Series(data, dtype="string[pyarrow]")

In [10]: ser_ad = pd.Series(data, dtype=pd.ArrowDtype(pa.string()))

In [11]: ser_ad.dtype == ser_sd.dtype
Out[11]: False

In [12]: ser_sd.str.contains("a")
Out[12]: 
0     True
1    False
2    False
dtype: boolean

In [13]: ser_ad.str.contains("a")
Out[13]: 
0     True
1    False
2    False
dtype: bool[pyarrow]
