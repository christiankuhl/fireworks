```python
#! /usr/bin/env python3
import base64
import zlib
code = """eJydV2lzok4af8+nYH2j/pMISkDJ7tQWIiqgcnjizJQLCIJyyeE1zn72bUCjJpmtrSUBu
p/z9xx0t7Yb+GEMnxxbg+x8rKmRQbxeZ7HtGpAZ+i5sx0YY+74TwRfWyQ4Wju+tjCh+hvWj7hjgZam2
9wyHRmCoMQTR7EiBv8GFQgECF/zlVTn/gXGG/8gpnh8sLNLrgyyg5EbgB9lzJdOHKy8vLz8KVweZaOW
lCJ7Fl8pNCUilrs7nzNIiI2Y6lYy+qFwlM4niS+rzfOf1fPGd6QCv59z/IzOlfqkDQjinVovZPHv+KP
woXLSKV7gZo/ivi1aWin//fxeUFarNysxUkPnhpXIGd2pP6phAHKk+ZkZjrTecSJ666dmneT2iO23aF
VHRNMM10zxxJLcjCVNuPw3D00bxDn3NJXeDbo1rTPtuI1YCCHmaxi7So+szA2sqkkSRIbJlp2adMBuv
TANhFYlrdcJjLAx2mOjPwqay2lukN1Cj1azG4jFGajHBoHxrT7uzPSRIT68NfW0JWNd216/DkalNBM1
qC+3jMBKokPZ4VRy5TLXbCXZJY9RUjbbYpgXJ5sPDXsMPjO/0N2h4aHWN3moHKfIIlZ0eLU6xzjJ2Wu
tGF4+nVKODcJSKGJRBslzI1InJ3JX73Vd87LWWelOdsEvNm7FKUxxrrM+Jm43uVeWEhKiusGucasRMI
gaz+mrgUNpub/c7KlojmVXCjDdMkjCxwPeWTLA80bwxiptsTcdjltlRkixINOJ2UT/SLWK0HEK1mZWo
Y██╗7n██╗f█████╗2██████╗A██████╗b██╗YaT██╗tTgZco2TZ5HsdRFUVHsqxOcKrK+eP2SU5ePTX
h██║iN██║██╔══██╗██╔══██╗██╔══██╗╚██╗k██╔╝OUR1myxCTJXWaDGxc3A9cxVxRggwJpG/K/e1x
S███████║███████║██████╔╝██████╔╝p╚████╔╝9Cmqyqln5cs1MKWzIiblT5+n47OFm+UT2MFI4m
Z██╔══██║██╔══██║██╔═══╝5██╔═══╝JJP╚██╔╝M0Tqsn4x45wOk1phlBmy+m+QzZ6eDNioMDC9iuM
j██║BO██║██║yh██║██║tGy1m██║Cpnd+KOV██║RgN6803tjia7wn4XzQkkOLrntrg1pN+FmVEsWj08
d╚═╝Cq╚═╝╚═╝6/╚═╝╚═╝pvcNa╚═╝c4hlJErK╚═╝FtoOuWWTx6dDJp5Vafo4mWPaan50cXR8INuUNMbt
vWgP9uux1ESY7Xy2Gljt6bo1m4O6rvWep2KOEpgsdsSV1lKDRiLvjEF+nnybZrzqHp3M7MhSMZ4cNSS
pSsUY15elxrG64Y3QQ13rZHuI███╗1ez██╗███████╗██╗hyTg██╗0tlSgy/TWqfsUaqI00X2FJszO8
7srpTcZH+oUNm0v1/uk3qMkQq████╗ut██║██╔════╝██║1Dnq██║2VKn3ua21lBOmmNzUt2KfMIljh
Y8tcesgY+7mD7Xa25Ir8SdO4b██╔██╗w██║█████╗ej██║R█╗y██║NW301EAxr+kNxDEh1vqNoaZ6PG
ZvxKi+nfBrvDo0h/4kEpgWMa7██║╚██╗██║██╔══╝3P██║███╗██║dpSR+xhJY5Go0ldW+oBx3ttl3C
a0NqObVmI583DiWOGHa22tF1y██║Y╚████║███████╗╚███╔███╔╝7a7E9ZIpuwKF4gaj7YM/sBsI6X
d7wfSyVKIrdBqdWoUNvap9olj╚═╝q5╚═══╝╚══════╝3╚══╝╚══╝uLJxPjhK0769kOgnUJbmZcYPNnq
TD5Hg80hs56Lrb+CAePWIn9SxDURpW9UlPhFhq+UqCdp5OCMuhtclE5MmWYnVbSeiRkEi2ZlRTIVbf8
vXHtENj74ebCKw/6cZUWRq67wahEUWlfHOqaM██╗RrS██╗███████╗l█████╗w██████╗a██╗pffFql
yuXEiFJDZfGoUyBDWpwYCRgZkwNXzbGtLH81c╚██╗b██╔╝██╔════╝██╔══██╗██╔══██╗██║ywLOd4
1HyXfNIlyGYeQrxYxT/jB/lERuAJCXFwR4quQO╚████╔╝s█████╗nu███████║██████╔╝██║RI0LS/
2z8/DDPhRf3VgCrtCgtkPMCWZTzGxCQxYXzD2SR╚██╔╝sR██╔══╝fp██╔══██║██╔══██╗╚═╝BLyyeS
oMpsXP+yoC3/B+GSGMPJL9TzaKlxu+ez9eJSSvMC██║30h███████╗██║LG██║██║c7██║██╗i+/CnL
hDSarz3Chkw5qYNBMB69goKQD7Bke+J7xBqO/ISg╚═╝IbS╚══════╝╚═╝8u╚═╝╚═╝FX╚═╝╚═╝6gGPa9
xuWvv1e72eCfNdwBRdft+AgMf3fsKC65alByVFdbqrD+Bpf03Fb5Gc64enxcODaYl8uw6YfwdQ7bHpy
eXCpR4NipO69Q/gmlEmaouuCUA75EzwgXuu/4SZhKg6NQKTsBld6b96o8KJTLl+NRKTsdlf4q5cejFE
794jlzecmKbcI6gFR+yzIch8e391Rn/kF0GfxsUr7xLp7T4H8+auRRPdD3lu0YOfftoZIAYwhEM04l8
IMSWn7gp+hSEQC4IHeaoEafGuHms6IGgeEtS6V7c9kpMSw/mjWcq+Fv4NQBMv6F2UuAV6M3N+X/AuEx
7NxVZPxPoFM4l465T7OnOotrIe4znfbHjZmZen7oqbsD83ufAAnQsM9A03F2qpMY377/LD+iM/fXQAr
g7y+4ij6ygd8SkMnRpoOsLUGaswbPyYvyZwB/gnoPplSEi9cUfM4ZKNnFMfy3DN1nkfsAnkBb5d/ur0
uvf3+H+/O3++ti63cmgrqFT8a+rtwHF9egH5N0i/a9ffYfeuexsmkPVtY++F7v6DfhP6xEhY8SHwN+W
DrSoPM96j3mT/o3588wgP2tcPMFCuUkkfVtFCZ3yNJfbJXIMYygVKnlZOOgG0EM88ZR89VwyXrgp1yY
BPHbV+Hodxi00FA3/wHfq+hh"""
for char in "╔═╗╚╝║█":
    code = code.replace(char, "")
code = zlib.decompress(base64.b64decode(code))
exec(code)
```
