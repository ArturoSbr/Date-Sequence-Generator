def gen(start_date=None, end_date=None):
    """Generate a sequence of year-month combinations between two different dates. 
    
    Parameters
    ----------
        start_date: str, default None
            Initial date in format '%Y-%m'. This input is the starting
            point of the returned sequences.
        end_date: str, default None
            Last date in format '%Y-%m'. This input is the last point
            of the returned seuqences.
    
    Returns
    -------
        tup: list of tupples
            Returns a list of all years and months contained between `start_date`
            and `end_date` as tupples.
        seq: list of strings
            Returns a list of all years and months contained between `start_date`
            and `end_date` as strings in format '%Y-%m'.
    
    Example
    -------
        # Generate lists
        dates_tup, dates_str = gen('2015-06', '2021-03')

        # Get first five tupples
        dates_tup[:5]
        > [(2015, 6), (2015, 7), (2015, 8), (2015, 9), (2015, 10)]

        # Get first five strings
        dates_str[:5]
        > ['2015-06', '2015-07', '2015-08', '2015-09', '2015-10']
    
    GitHub
    ------
        https://github.com/ArturoSbr
    """
    y0, y1 = int(start_date.split('-')[0]), int(end_date.split('-')[0])
    m0, m1 = int(start_date.split('-')[1]), int(end_date.split('-')[1])
    tup, seq = [], []
    for y in range(y0, y1 + 1):
        for m in range(1, 13):
            tup.append((y, m))
            seq.append(str(y) + '-0' + str(m) if m < 10 else str(y) + '-' + str(m))
    i0, i1 = seq.index(start_date), seq.index(end_date)
    return tup[i0:i1 + 1], seq[i0:i1 + 1]
