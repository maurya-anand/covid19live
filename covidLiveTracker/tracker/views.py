from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request,'tracker/index.html')
    

country_code={"AF":"AFG", "AL":"ALB", "DZ":"DZA", "AS":"ASM", "AD":"AND", "AO":"AGO", "AI":"AIA", "AQ":"ATA", "AG":"ATG", "AR":"ARG", "AM":"ARM", "AW":"ABW", "AU":"AUS", "AT":"AUT", "AZ":"AZE", "BS":"BHS", "BH":"BHR", "BD":"BGD", "BB":"BRB", "BY":"BLR", "BE":"BEL", "BZ":"BLZ", "BJ":"BEN", "BM":"BMU", "BT":"BTN", "BO":"BOL", "BQ":"BES", "BA":"BIH", "BW":"BWA", "BV":"BVT", "BR":"BRA", "IO":"IOT", "BN":"BRN", "BG":"BGR", "BF":"BFA", "BI":"BDI", "CV":"CPV", "KH":"KHM", "CM":"CMR", "CA":"CAN", "KY":"CYM", "CF":"CAF", "TD":"TCD", "CL":"CHL", "CN":"CHN", "CX":"CXR", "CC":"CCK", "CO":"COL", "KM":"COM", "CD":"COD", "CG":"COG", "CK":"COK", "CR":"CRI", "HR":"HRV", "CU":"CUB", "CW":"CUW", "CY":"CYP", "CZ":"CZE", "CI":"CIV", "DK":"DNK", "DJ":"DJI", "DM":"DMA", "DO":"DOM", "EC":"ECU", "EG":"EGY", "SV":"SLV", "GQ":"GNQ", "ER":"ERI", "EE":"EST", "SZ":"SWZ", "ET":"ETH", "FK":"FLK", "FO":"FRO", "FJ":"FJI", "FI":"FIN", "FR":"FRA", "GF":"GUF", "PF":"PYF", "TF":"ATF", "GA":"GAB", "GM":"GMB", "GE":"GEO", "DE":"DEU", "GH":"GHA", "GI":"GIB", "GR":"GRC", "GL":"GRL", "GD":"GRD", "GP":"GLP", "GU":"GUM", "GT":"GTM", "GG":"GGY", "GN":"GIN", "GW":"GNB", "GY":"GUY", "HT":"HTI", "HM":"HMD", "VA":"VAT", "HN":"HND", "HK":"HKG", "HU":"HUN", "IS":"ISL", "IN":"IND", "ID":"IDN", "IR":"IRN", "IQ":"IRQ", "IE":"IRL", "IM":"IMN", "IL":"ISR", "IT":"ITA", "JM":"JAM", "JP":"JPN", "JE":"JEY", "JO":"JOR", "KZ":"KAZ", "KE":"KEN", "KI":"KIR", "KP":"PRK", "KR":"KOR", "KW":"KWT", "KG":"KGZ", "LA":"LAO", "LV":"LVA", "LB":"LBN", "LS":"LSO", "LR":"LBR", "LY":"LBY", "LI":"LIE", "LT":"LTU", "LU":"LUX", "MO":"MAC", "MG":"MDG", "MW":"MWI", "MY":"MYS", "MV":"MDV", "ML":"MLI", "MT":"MLT", "MH":"MHL", "MQ":"MTQ", "MR":"MRT", "MU":"MUS", "YT":"MYT", "MX":"MEX", "FM":"FSM", "MD":"MDA", "MC":"MCO", "MN":"MNG", "ME":"MNE", "MS":"MSR", "MA":"MAR", "MZ":"MOZ", "MM":"MMR", "NA":"NAM", "NR":"NRU", "NP":"NPL", "NL":"NLD", "NC":"NCL", "NZ":"NZL", "NI":"NIC", "NE":"NER", "NG":"NGA", "NU":"NIU", "NF":"NFK", "MP":"MNP", "NO":"NOR", "OM":"OMN", "PK":"PAK", "PW":"PLW", "PS":"PSE", "PA":"PAN", "PG":"PNG", "PY":"PRY", "PE":"PER", "PH":"PHL", "PN":"PCN", "PL":"POL", "PT":"PRT", "PR":"PRI", "QA":"QAT", "MK":"MKD", "RO":"ROU", "RU":"RUS", "RW":"RWA", "RE":"REU", "BL":"BLM", "SH":"SHN", "KN":"KNA", "LC":"LCA", "MF":"MAF", "PM":"SPM", "VC":"VCT", "WS":"WSM", "SM":"SMR", "ST":"STP", "SA":"SAU", "SN":"SEN", "RS":"SRB", "SC":"SYC", "SL":"SLE", "SG":"SGP", "SX":"SXM", "SK":"SVK", "SI":"SVN", "SB":"SLB", "SO":"SOM", "ZA":"ZAF", "GS":"SGS", "SS":"SSD", "ES":"ESP", "LK":"LKA", "SD":"SDN", "SR":"SUR", "SJ":"SJM", "SE":"SWE", "CH":"CHE", "SY":"SYR", "TW":"TWN", "TJ":"TJK", "TZ":"TZA", "TH":"THA", "TL":"TLS", "TG":"TGO", "TK":"TKL", "TO":"TON", "TT":"TTO", "TN":"TUN", "TR":"TUR", "TM":"TKM", "TC":"TCA", "TV":"TUV", "UG":"UGA", "UA":"UKR", "AE":"ARE", "GB":"GBR", "UM":"UMI", "US":"USA", "UY":"URY", "UZ":"UZB", "VU":"VUT", "VE":"VEN", "VN":"VNM", "VG":"VGB", "VI":"VIR", "WF":"WLF", "EH":"ESH", "YE":"YEM", "ZM":"ZMB", "ZW":"ZWE", "AX":"ALA"};

def getData(request):
    response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
    #print(response)
    geodata = response.json()
    
    #print(len(geodata))
    #print(geodata['confirmed']['locations'])
    res_dict={}
    for i in geodata['confirmed']['locations']:
        #print(i['country_code'],i['latest'])
        if i['country_code'] in res_dict:
            res_dict[i['country_code']]+=i['latest']
        else:
            res_dict[i['country_code']]=i['latest']
    
    #print(res_dict)
    
    res_recov_dict={}
    for i in geodata['recovered']['locations']:
        #print(i['country_code'],i['latest'])
        if i['country_code'] in res_recov_dict:
            res_recov_dict[i['country_code']]+=i['latest']
        else:
            res_recov_dict[i['country_code']]=i['latest']
    
    #print(res_recov_dict)

    res_deaths_dict={}
    for i in geodata['deaths']['locations']:
        #print(i['country_code'],i['latest'])
        if i['country_code'] in res_deaths_dict:
            res_deaths_dict[i['country_code']]+=i['latest']
        else:
            res_deaths_dict[i['country_code']]=i['latest']
    
    #print(res_deaths_dict)

    res_arr=[]
    for k,v in res_dict.items():
        #print(k,v)
        if k in country_code:
            res_arr.append({"code3":country_code[k],"z":v,"code":k,"value":v,"recovered":res_recov_dict[k],"deaths":res_deaths_dict[k] })
    
    res_arr_obj=json.dumps(res_arr)
    #return JsonResponse(geodata,safe=True)

    #print(geodata.keys())
    #dict_keys(['confirmed', 'deaths', 'latest', 'recovered'])
    #print(geodata['confirmed']['last_updated'])
    return JsonResponse(res_arr_obj,safe=False)
