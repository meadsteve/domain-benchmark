# Benchmarking plain objects vs domain

Some very basic benchmarking on the performance difference between "code preferring domain objects over primitives" and 
"plain types and dicts".

## Happy Path
```bash
pytest . -m "happy" --benchmark-save=happy_path --benchmark-disable-gc
USE_DOMAIN_OBJECTS=1 pytest . -m "happy"  --benchmark-compare=0001 --benchmark-save=happy_path --benchmark-disable-gc
```

```

--------------------------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------------------------
Name (time in us)                                                     Min                 Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_valid_users_get_parsed_and_no_data_is_lost (0001_happy_p)     2.4230 (1.0)       76.0650 (1.0)      3.1123 (1.0)      2.2341 (1.25)     2.6630 (1.0)      0.1560 (1.97)    3219;7603      321.3096 (1.0)       69843           1
test_valid_users_get_parsed_and_no_data_is_lost (NOW)              3.9990 (1.65)     135.6200 (1.78)     4.3137 (1.39)     1.7812 (1.0)      4.1300 (1.55)     0.0790 (1.0)      562;3600      231.8215 (0.72)      44825           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean

```

## Sad Path
```bash
pytest . -m "sad" --benchmark-save=sad_path --benchmark-disable-gc
USE_DOMAIN_OBJECTS=1 pytest . -m "sad"  --benchmark-compare=0003 --benchmark-save=sad_path --benchmark-disable-gc
```

```


------------------------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------------------------
Name (time in us)                                                Min                 Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_invalid_user_data_raises_an_exception (0003_sad_pat)     3.3910 (1.0)      109.7340 (2.84)     3.6168 (1.0)      1.4584 (1.0)      3.4890 (1.0)      0.0320 (1.0)      479;4750      276.4867 (1.0)       56632           1
test_invalid_user_data_raises_an_exception (NOW)              5.6200 (1.66)      38.6240 (1.0)      6.0598 (1.68)     1.8484 (1.27)     5.8110 (1.67)     0.0780 (2.44)     524;3403      165.0221 (0.60)      32421           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean


```

## With an API to slow things down
```bash
uvicorn parrot_api:app --reload

pytest . -m "happy_web" --benchmark-save=happy_web_path --benchmark-disable-gc
USE_DOMAIN_OBJECTS=1 pytest . -m "happy_web" --benchmark-compare=0005 --benchmark-save=happy_web_path --benchmark-disable-gc
```


```
-------------------------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------------------------
Name (time in ms)                                                      Min                Max               Mean            StdDev             Median                IQR            Outliers      OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_valid_users_get_parsed_and_no_data_is_lost (0005_happy_w)     10.2608 (1.0)      35.8208 (1.81)     18.8076 (1.24)     7.6562 (4.94)     15.4346 (1.04)     14.2687 (8.69)         23;0  53.1700 (0.81)         70           1
test_valid_users_get_parsed_and_no_data_is_lost (NOW)              12.2650 (1.20)     19.7666 (1.0)      15.1955 (1.0)      1.5512 (1.0)      14.8576 (1.0)       1.6427 (1.0)          16;2  65.8088 (1.0)          52           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

