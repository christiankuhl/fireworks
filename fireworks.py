#! /usr/bin/env python3
import base64
import zlib
code = """eJydVtuSosoSfecrOL6oYbciKmqf6AcQUUBFQRR7ZqIPlwJBbnIRcZz97RtQp3Wm58SOz
YNW5W2tzCwqMR3fCyL4ZJsKZF7WihwCrH3bRaYDID3wHNiMQBB5nh3CV9XJ9N9tzzVAGD3BaqraAIIG
9HIDv8K.;;,lUgnK.;;,HvjTp37+g+IM/1FTPj9EeM+fX2wzySUI/GB7rhf+cP35+flr6QZQmNafy9l
v+bn+4Z`RZ;;5VD;;nc'xHpvRAWPvVC/l6/WRYW5ecc83yHer5iFz4Z6vmC/6jMpZ/6ZCmc86jlYl/8
fi19LV29yj;;e6h;;a,L8.;;;.v6t.;;,;;;,XU.;;,;;;,Yq.;;.//.;;.t0DFY2iaH645nhWuHYOM
CdqdUIPW,;;;;;;;;;'Ip`PW3;;oY`o;;CMj;;2`I;;IjL;;a`3;;M9;;L'AZztgVU1scGo2+lzCbSW
cK3FiX9q`z;;SIT;;fj7n.;;.;;hmbl;;pct;;yZy;;UzK;;N36;;Km;;Ah0njcaUsRqhYmtdlTAIY4
7qILRmDZ1v;;tIj;;lPB0;;NB;;4,tj;;0JN;;mY7;;l/w;;igs;;Wd;;NTWn87rQOa6pucojXWXWC8
bRcqjmB.Qj;;0jnz';;'T`;;;';;'G5;;';;'08lA;;';;'1FmZt`;;';BitfxCZmBITyaIWCxJ1p4E
3GynLnS';;'o74JROKRfbbww+HfIrEJ;;OqvAOGaC;;6XB5FW2wAaNL;;arGW8O5HFt5nDdEzd2k0ki
D+ftiAPkiqvhWirwKNNvsdbA2BxO.Rz;;/GOxu.z5;;if75pQzMK.K2;;QJaJoE88f7y3IAolY03pjK
NevO0t4pahTQxJsoYbFvVXKEuIg4';;'AmJJ0Z';;'gPV6z/AKR0';;'u9+XBo+d0dggt9gse7+ATd6
IKZptKWg5qBBkZv0WJooYGrs4Em6+vRANsP267jHi2e1yjKb3m4uDTNGJs1h8rqNE+bja7o2QtXCLyR
sA+7ag1f80ZtMYU6QyU1+g.;;,i,;;;,6ZzxyFioncW932elRxTVE7dvdxf6QGgiHbrsSRWx3Sh8Q+q
Ht0PRIIGmlA+Rk4Sp4l63h`rc;;NWo2;;eQ4U652mikR1GLQzFhIlk41R9ozGh7HLq4dLClaYPYjJkV
K89EVuohb8mQDQTgER2gBo4mM;;lZ3C;;6ZdNV,;;,pG.;;.2zYJ2S.;;,uBnxiMxGKCzaLeApUDris
SHNLgzNHY88yB44Rk27IoIaO4;;XhOy;;uV8Q;;Vo;;y`Y;;KR82Hc;;9'9kylJYE4ximuLOQPZxok1
2glCDZTjEdGWerjYo2zE6+mYw;;LBu0;;znyW;;;;;'U8a;;2u;;5I;;EKcJWPqYown72XynpCbvYjF
iyQHOywsTMzp0D4fUXc2m6A4X;;ocOB;;NQWh;;R8Z.kHG;;Jj;;ir;;HbK7yToC5vRsx4au7ReUdMD
QNpasA+Bpy8H4VNy+43wmH.UQ;;fDW1B';;'cR`;;;'h4Qm`;;'`;;'28M8cpmDI6A9nefaSavFU9yh
d5qPdqjQjTfMGIsH4dJcy1';;'JLNcdK8IZzFBm+tcO1aLIKuUtaK+GUtmRt6LMyFHd2cmdimLyf9LE
2bnECsxsdQ6U5x7yY1Fm6qU63s5OkGRIdp/yAUWRO2CiCGJu2acwsa4Zg5Mo78H3GazIxJI1FcUAjU8
MfHd5kEYgdQ1l6XTyoJdFA3vJ+EAZ9nzu1Bt4.;;.yoPTN.;;.RnVbsbeb9ocTn4574xrZZzL12l6Oe
sskgEZuzXK1Q0flN9vk9XIHDbgJJ/L5DfS9xJ`de;;4H7;;zC'S6N8gWaLYh80c4Wm3zReoJnngteYO
TH4+WVj7G6BlTP8QMQhpXLKKsrWDsXaqDy07harV;;9Fp;;TjS.;;,n3.;;;.ulK.;;.;;;,gT5gelG
ldJXpNX6gjKXv/82x5lKNaM0C//FNsOo4sh+xZYd;;RZN;;h9;;QW;;u'qBc;;y1`S;;e40'KpR+m6b
2b5ahXUvgG972HThfDjWQ982cxS3VP0G5RZ6kN1R;;ubo;;Yo;;;;;'R.;;,;;8Ub5;;azUrX6UoytK
Ehffg69i9vrBbXYVD90ZgASL9jlnL89elzIPMiTrW`;;;';mD;;i/b.l;;Ya;;a,qW;;znITAtN3ff8
ClJ90Jv6xSTjXuJHRNab38b3B2Zd9n3gapXKfbinIkD1M;;Syw`;;;'b4`;;';;'Ff;'s3mUFeqTsNc
Eb0E/YKr/h8Jj2heoEPwj0jmda6Pvy+zK9vutEfeVztv6;;oSxCPT0chbtvp8otmcwiO2dPmadtH2Q7
Bq9fvlUf2enJLZHsnXlQZIiVTHvhmS8824uDrMDFi.'by;;I36u/Q/+J5D2NShku35L/vVpZs67A8H8
yXvAn7bqnXssO1OUd+35957/8pPvth/P9GutHYYI4';;;'pd+Cfd6zXyBuST8W6SPbnwcn+eXUPPY0P
311yzPd+0p9GP/5xni0uHN+gjPY19KHbVZoOw63r8sgvoucf3bXQxsAv1JHL2JwVIEfwSxIFU8ONNrN
vseD2I9ePqOj3nFQAiDv/gbXoHhD"""
exec(zlib.decompress(base64.b64decode(code)))
