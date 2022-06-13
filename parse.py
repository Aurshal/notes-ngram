import json
data = '''State    Postal
Abbr.    FIPS
Code    State    Postal
Abbr.    FIPS
Code
Alabama    AL    01    Nebraska    NE    31
Alaska    AK    02    Nevada    NV    32
Arizona    AZ    04    New Hampshire    NH    33
Arkansas    AR    05    New Jersey    NJ    34
California    CA    06    New Mexico    NM    35
Colorado    CO    08    New York    NY    36
Connecticut    CT    09    North Carolina    NC    37
Delaware    DE    10    North Dakota    ND    38
District of Columbia    DC    11    Ohio    OH    39
Florida    FL    12    Oklahoma    OK    40
Georgia    GA    13    Oregon    OR    41
Hawaii    HI    15    Pennsylvania    PA    42
Idaho    ID    16    Puerto Rico    PR    72
Illinois    IL    17    Rhode Island    RI    44
Indiana    IN    18    South Carolina    SC    45
Iowa    IA    19    South Dakota    SD    46
Kansas    KS    20    Tennessee    TN    47
Kentucky    KY    21    Texas    TX    48
Louisiana    LA    22    Utah    UT    49
Maine    ME    23    Vermont    VT    50
Maryland    MD    24    Virginia    VA    51
Massachusetts    MA    25    Virgin Islands    VI    78
Michigan    MI    26    Washington    WA    53
Minnesota    MN    27    West Virginia    WV    54
Mississippi    MS    28    Wisconsin    WI    55
Missouri    MO    29    Wyoming    WY    56
Montana    MT    30'''
state = ''
abbr = ''
dat ={} 
for d in (data.split())[10:]:
    if d.istitle():
        if state:
            state +=f" {d}"
        else:
            state = d
    if d.isupper():
        abbr = d

    if d.isnumeric():
        code = d
        dat[state] = {'Postal Abbr':abbr,'FIPS code':code}
        state = ''
        abbr = ''
print(dat)
with open('data/state.json','w') as f:
    json.dump(dat,f,indent = 4)
