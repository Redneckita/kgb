GEARS = [
    ['pistols', 'FGfg', False]
    ,['smg', 'IJh', False]
    ,['autos', 'LMae', False]
    ,['spas', 'H', False]
    ,['negev', 'c', False]
    ,['snipers', 'NZ', False]
    ,['nades', 'OQK', False]
    ,['armor', 'RW', False]
    ,['attachments', 'UV', False]
    ,['extras', 'XTS', True]
]



print "available parameters are: +/- " + ' '.join([x[0] for x in GEARS]) + " or none or all"