versio = 1.0

def CF(tila):
    return round(float(tila)*1.8+32,2)

def CK(tila):
    return round(float(tila)+273.15,2)

def FK(tila):
    return round(CK(FC(tila)),2)

def FC(tila):
    return round((float(tila)-32)/1.8,2)

def KC(tila):
    return round(float(tila)-273.15,2)

def KF(tila):
    return round(CF(KC(tila)),2)