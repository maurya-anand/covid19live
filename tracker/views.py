from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return render(request, "tracker/index.html")

#country_code={"AF":"AFG", "AL":"ALB", "DZ":"DZA", "AS":"ASM", "AD":"AND", "AO":"AGO", "AI":"AIA", "AQ":"ATA", "AG":"ATG", "AR":"ARG", "AM":"ARM", "AW":"ABW", "AU":"AUS", "AT":"AUT", "AZ":"AZE", "BS":"BHS", "BH":"BHR", "BD":"BGD", "BB":"BRB", "BY":"BLR", "BE":"BEL", "BZ":"BLZ", "BJ":"BEN", "BM":"BMU", "BT":"BTN", "BO":"BOL", "BQ":"BES", "BA":"BIH", "BW":"BWA", "BV":"BVT", "BR":"BRA", "IO":"IOT", "BN":"BRN", "BG":"BGR", "BF":"BFA", "BI":"BDI", "CV":"CPV", "KH":"KHM", "CM":"CMR", "CA":"CAN", "KY":"CYM", "CF":"CAF", "TD":"TCD", "CL":"CHL", "CN":"CHN", "CX":"CXR", "CC":"CCK", "CO":"COL", "KM":"COM", "CD":"COD", "CG":"COG", "CK":"COK", "CR":"CRI", "HR":"HRV", "CU":"CUB", "CW":"CUW", "CY":"CYP", "CZ":"CZE", "CI":"CIV", "DK":"DNK", "DJ":"DJI", "DM":"DMA", "DO":"DOM", "EC":"ECU", "EG":"EGY", "SV":"SLV", "GQ":"GNQ", "ER":"ERI", "EE":"EST", "SZ":"SWZ", "ET":"ETH", "FK":"FLK", "FO":"FRO", "FJ":"FJI", "FI":"FIN", "FR":"FRA", "GF":"GUF", "PF":"PYF", "TF":"ATF", "GA":"GAB", "GM":"GMB", "GE":"GEO", "DE":"DEU", "GH":"GHA", "GI":"GIB", "GR":"GRC", "GL":"GRL", "GD":"GRD", "GP":"GLP", "GU":"GUM", "GT":"GTM", "GG":"GGY", "GN":"GIN", "GW":"GNB", "GY":"GUY", "HT":"HTI", "HM":"HMD", "VA":"VAT", "HN":"HND", "HK":"HKG", "HU":"HUN", "IS":"ISL", "IN":"IND", "ID":"IDN", "IR":"IRN", "IQ":"IRQ", "IE":"IRL", "IM":"IMN", "IL":"ISR", "IT":"ITA", "JM":"JAM", "JP":"JPN", "JE":"JEY", "JO":"JOR", "KZ":"KAZ", "KE":"KEN", "KI":"KIR", "KP":"PRK", "KR":"KOR", "KW":"KWT", "KG":"KGZ", "LA":"LAO", "LV":"LVA", "LB":"LBN", "LS":"LSO", "LR":"LBR", "LY":"LBY", "LI":"LIE", "LT":"LTU", "LU":"LUX", "MO":"MAC", "MG":"MDG", "MW":"MWI", "MY":"MYS", "MV":"MDV", "ML":"MLI", "MT":"MLT", "MH":"MHL", "MQ":"MTQ", "MR":"MRT", "MU":"MUS", "YT":"MYT", "MX":"MEX", "FM":"FSM", "MD":"MDA", "MC":"MCO", "MN":"MNG", "ME":"MNE", "MS":"MSR", "MA":"MAR", "MZ":"MOZ", "MM":"MMR", "NA":"NAM", "NR":"NRU", "NP":"NPL", "NL":"NLD", "NC":"NCL", "NZ":"NZL", "NI":"NIC", "NE":"NER", "NG":"NGA", "NU":"NIU", "NF":"NFK", "MP":"MNP", "NO":"NOR", "OM":"OMN", "PK":"PAK", "PW":"PLW", "PS":"PSE", "PA":"PAN", "PG":"PNG", "PY":"PRY", "PE":"PER", "PH":"PHL", "PN":"PCN", "PL":"POL", "PT":"PRT", "PR":"PRI", "QA":"QAT", "MK":"MKD", "RO":"ROU", "RU":"RUS", "RW":"RWA", "RE":"REU", "BL":"BLM", "SH":"SHN", "KN":"KNA", "LC":"LCA", "MF":"MAF", "PM":"SPM", "VC":"VCT", "WS":"WSM", "SM":"SMR", "ST":"STP", "SA":"SAU", "SN":"SEN", "RS":"SRB", "SC":"SYC", "SL":"SLE", "SG":"SGP", "SX":"SXM", "SK":"SVK", "SI":"SVN", "SB":"SLB", "SO":"SOM", "ZA":"ZAF", "GS":"SGS", "SS":"SSD", "ES":"ESP", "LK":"LKA", "SD":"SDN", "SR":"SUR", "SJ":"SJM", "SE":"SWE", "CH":"CHE", "SY":"SYR", "TW":"TWN", "TJ":"TJK", "TZ":"TZA", "TH":"THA", "TL":"TLS", "TG":"TGO", "TK":"TKL", "TO":"TON", "TT":"TTO", "TN":"TUN", "TR":"TUR", "TM":"TKM", "TC":"TCA", "TV":"TUV", "UG":"UGA", "UA":"UKR", "AE":"ARE", "GB":"GBR", "UM":"UMI", "US":"USA", "UY":"URY", "UZ":"UZB", "VU":"VUT", "VE":"VEN", "VN":"VNM", "VG":"VGB", "VI":"VIR", "WF":"WLF", "EH":"ESH", "YE":"YEM", "ZM":"ZMB", "ZW":"ZWE", "AX":"ALA"}
country_code = {"AF":"AFG", "AX":"ALA", "AL":"ALB", "DZ":"DZA", "AS":"ASM", "AD":"AND", "AO":"AGO", "AI":"AIA", "AQ":"ATA", "AG":"ATG", "AR":"ARG", "AM":"ARM", "AW":"ABW", "AU":"AUS", "AT":"AUT", "AZ":"AZE", "BS":"BHS", "BH":"BHR", "BD":"BGD", "BB":"BRB", "BY":"BLR", "BE":"BEL", "BZ":"BLZ", "BJ":"BEN", "BM":"BMU", "BT":"BTN", "BO":"BOL", "BQ":"BES", "BA":"BIH", "BW":"BWA", "BV":"BVT", "BR":"BRA", "IO":"IOT", "VG":"VGB", "BN":"BRN", "BG":"BGR", "BF":"BFA", "BI":"BDI", "KH":"KHM", "CM":"CMR", "CA":"CAN", "CV":"CPV", "KY":"CYM", "CF":"CAF", "TD":"TCD", "CL":"CHL", "CN":"CHN", "CX":"CXR", "CC":"CCK", "CO":"COL", "KM":"COM", "CK":"COK", "CR":"CRI", "HR":"HRV", "CU":"CUB", "CW":"CUW", "CY":"CYP", "CZ":"CZE", "CD":"COD", "DK":"DNK", "DJ":"DJI", "DM":"DMA", "DO":"DOM", "TL":"TLS", "EC":"ECU", "EG":"EGY", "SV":"SLV", "GQ":"GNQ", "ER":"ERI", "EE":"EST", "ET":"ETH", "FK":"FLK", "FO":"FRO", "FJ":"FJI", "FI":"FIN", "FR":"FRA", "GF":"GUF", "PF":"PYF", "TF":"ATF", "GA":"GAB", "GM":"GMB", "GE":"GEO", "DE":"DEU", "GH":"GHA", "GI":"GIB", "GR":"GRC", "GL":"GRL", "GD":"GRD", "GP":"GLP", "GU":"GUM", "GT":"GTM", "GG":"GGY", "GN":"GIN", "GW":"GNB", "GY":"GUY", "HT":"HTI", "HM":"HMD", "HN":"HND", "HK":"HKG", "HU":"HUN", "IS":"ISL", "IN":"IND", "ID":"IDN", "IR":"IRN", "IQ":"IRQ", "IE":"IRL", "IM":"IMN", "IL":"ISR", "IT":"ITA", "CI":"CIV", "JM":"JAM", "JP":"JPN", "JE":"JEY", "JO":"JOR", "KZ":"KAZ", "KE":"KEN", "KI":"KIR", "XK":"XKX", "KW":"KWT", "KG":"KGZ", "LA":"LAO", "LV":"LVA", "LB":"LBN", "LS":"LSO", "LR":"LBR", "LY":"LBY", "LI":"LIE", "LT":"LTU", "LU":"LUX", "MO":"MAC", "MK":"MKD", "MG":"MDG", "MW":"MWI", "MY":"MYS", "MV":"MDV", "ML":"MLI", "MT":"MLT", "MH":"MHL", "MQ":"MTQ", "MR":"MRT", "MU":"MUS", "YT":"MYT", "MX":"MEX", "FM":"FSM", "MD":"MDA", "MC":"MCO", "MN":"MNG", "ME":"MNE", "MS":"MSR", "MA":"MAR", "MZ":"MOZ", "MM":"MMR", "NA":"NAM", "NR":"NRU", "NP":"NPL", "NL":"NLD", "AN":"ANT", "NC":"NCL", "NZ":"NZL", "NI":"NIC", "NE":"NER", "NG":"NGA", "NU":"NIU", "NF":"NFK", "KP":"PRK", "MP":"MNP", "NO":"NOR", "OM":"OMN", "PK":"PAK", "PW":"PLW", "PS":"PSE", "PA":"PAN", "PG":"PNG", "PY":"PRY", "PE":"PER", "PH":"PHL", "PN":"PCN", "PL":"POL", "PT":"PRT", "PR":"PRI", "QA":"QAT", "CG":"COG", "RE":"REU", "RO":"ROU", "RU":"RUS", "RW":"RWA", "BL":"BLM", "SH":"SHN", "KN":"KNA", "LC":"LCA", "MF":"MAF", "PM":"SPM", "VC":"VCT", "WS":"WSM", "SM":"SMR", "ST":"STP", "SA":"SAU", "SN":"SEN", "RS":"SRB", "CS":"SCG", "SC":"SYC", "SL":"SLE", "SG":"SGP", "SX":"SXM", "SK":"SVK", "SI":"SVN", "SB":"SLB", "SO":"SOM", "ZA":"ZAF", "GS":"SGS", "KR":"KOR", "SS":"SSD", "ES":"ESP", "LK":"LKA", "SD":"SDN", "SR":"SUR", "SJ":"SJM", "SZ":"SWZ", "SE":"SWE", "CH":"CHE", "SY":"SYR", "TW":"TWN", "TJ":"TJK", "TZ":"TZA", "TH":"THA", "TG":"TGO", "TK":"TKL", "TO":"TON", "TT":"TTO", "TN":"TUN", "TR":"TUR", "TM":"TKM", "TC":"TCA", "TV":"TUV", "VI":"VIR", "UG":"UGA", "UA":"UKR", "AE":"ARE", "GB":"GBR", "US":"USA", "UM":"UMI", "UY":"URY", "UZ":"UZB", "VU":"VUT", "VA":"VAT", "VE":"VEN", "VN":"VNM", "WF":"WLF", "EH":"ESH", "YE":"YEM", "ZM":"ZMB", "ZW":"ZWE"}
#country_code2={"Finland":"FI", "France":"FR", "North Macedonia":"MK", "Austria":"AT", "Netherlands":"NL", "Cyprus":"CY", "Nepal":"NP", "US":"US", "Georgia":"GE", "Greece":"GR", "Honduras":"HN", "China":"CN", "Bangladesh":"BD", "Cuba":"CU", "Ireland":"IE", "Colombia":"CO", "United Arab Emirates":"AE", "Panama":"PA", "Thailand":"TH", "Vietnam":"VN", "Ukraine":"UA", "Spain":"ES", "Italy":"IT", "United Kingdom":"GB", "Australia":"AU", "Argentina":"AR", "Dominican Republic":"DO", "Bosnia and Herzegovina":"BA", "Slovakia":"SK", "South Africa":"ZA", "Malaysia":"MY", "Cruise Ship":"OTH", "Morocco":"MA", "Paraguay":"PY", "Romania":"RO", "Togo":"TG", "Ecuador":"EC", "Russia":"RU", "Sri Lanka":"LK", "Congo (Kinshasa)":"OTH", "Saudi Arabia":"SA", "Sweden":"SE", "Jordan":"JO", "Israel":"IL", "Bolivia":"BO", "Mainland China":"CN", "Qatar":"QA", "Canada":"CA", "Switzerland":"CH", "Mexico":"MX", "Belgium":"BE", "Afghanistan":"AF", "Andorra":"AD", "Japan":"JP", "Denmark":"DK", "Iceland":"IS", "Brazil":"BR", "Czechia":"CZ", "Slovenia":"SI", "Poland":"PL", "Philippines":"PH", "Chile":"CL", "Bulgaria":"BG", "Azerbaijan":"AZ", "Serbia":"RS", "Pakistan":"PK", "Holy See":"VA", "Moldova":"MD", "Brunei":"BN", "Turkey":"TR", "Malta":"MT", "Reunion":"RE", "Cote d'Ivoire":"CI", "Portugal":"PT", "Albania":"AL", "Costa Rica":"CR", "Liechtenstein":"LI", "Cambodia":"KH", "Peru":"PE", "Egypt":"EG", "Tunisia":"TN", "Burkina Faso":"BF", "Iraq":"IQ", "Croatia":"HR", "Iran":"IR", "Indonesia":"ID", "Algeria":"DZ", "Germany":"DE", "Estonia":"EE", "Nigeria":"NG", "Bhutan":"BT", "Martinique":"MQ", "occupied Palestinian territory":"PS", "Guyana":"GY", "Belarus":"BY", "Lithuania":"LT", "Oman":"OM", "Bahrain":"BH", "Senegal":"SN", "Cameroon":"CM", "Luxembourg":"LU", "Monaco":"MC", "Kuwait":"KW", "Armenia":"AM", "Mongolia":"MN", "Hungary":"HU", "French Guiana":"GF", "Singapore":"SG", "San Marino":"SM", "Jamaica":"JM", "Latvia":"LV", "Korea":"KR", "India":"IN", "Maldives":"MV", "New Zealand":"NZ", "Norway":"NO", "Taiwan*":"TW", "Lebanon":"LB"}
country_code2={"Afghanistan":"AF", "Aland Islands":"AX", "Albania":"AL", "Algeria":"DZ", "American Samoa":"AS", "Andorra":"AD", "Angola":"AO", "Anguilla":"AI", "Antarctica":"AQ", "Antigua and Barbuda":"AG", "Argentina":"AR", "Armenia":"AM", "Aruba":"AW", "Australia":"AU", "Austria":"AT", "Azerbaijan":"AZ", "Bahamas":"BS", "Bahrain":"BH", "Bangladesh":"BD", "Barbados":"BB", "Belarus":"BY", "Belgium":"BE", "Belize":"BZ", "Benin":"BJ", "Bermuda":"BM", "Bhutan":"BT", "Bolivia":"BO", "Bonaire, Saint Eustatius and Saba":"BQ", "Bosnia and Herzegovina":"BA", "Botswana":"BW", "Bouvet Island":"BV", "Brazil":"BR", "British Indian Ocean Territory":"IO", "British Virgin Islands":"VG", "Brunei":"BN", "Bulgaria":"BG", "Burkina Faso":"BF", "Burundi":"BI", "Cambodia":"KH", "Cameroon":"CM", "Canada":"CA", "Cape Verde":"CV", "Cayman Islands":"KY", "Central African Republic":"CF", "Chad":"TD", "Chile":"CL", "China":"CN", "Christmas Island":"CX", "Cocos Islands":"CC", "Colombia":"CO", "Comoros":"KM", "Cook Islands":"CK", "Costa Rica":"CR", "Croatia":"HR", "Cuba":"CU", "Curacao":"CW", "Cyprus":"CY", "Czechia":"CZ", "Congo (Kinshasa)":"CD", "Denmark":"DK", "Djibouti":"DJ", "Dominica":"DM", "Dominican Republic":"DO", "East Timor":"TL", "Ecuador":"EC", "Egypt":"EG", "El Salvador":"SV", "Equatorial Guinea":"GQ", "Eritrea":"ER", "Estonia":"EE", "Ethiopia":"ET", "Falkland Islands":"FK", "Faroe Islands":"FO", "Fiji":"FJ", "Finland":"FI", "France":"FR", "French Guiana":"GF", "French Polynesia":"PF", "French Southern Territories":"TF", "Gabon":"GA", "Gambia":"GM", "Georgia":"GE", "Germany":"DE", "Ghana":"GH", "Gibraltar":"GI", "Greece":"GR", "Greenland":"GL", "Grenada":"GD", "Guadeloupe":"GP", "Guam":"GU", "Guatemala":"GT", "Guernsey":"GG", "Guinea":"GN", "Guinea-Bissau":"GW", "Guyana":"GY", "Haiti":"HT", "Heard Island and McDonald Islands":"HM", "Honduras":"HN", "Hong Kong":"HK", "Hungary":"HU", "Iceland":"IS", "India":"IN", "Indonesia":"ID", "Iran":"IR", "Iraq":"IQ", "Ireland":"IE", "Isle of Man":"IM", "Israel":"IL", "Italy":"IT", "Cote d'Ivoire":"CI", "Jamaica":"JM", "Japan":"JP", "Jersey":"JE", "Jordan":"JO", "Kazakhstan":"KZ", "Kenya":"KE", "Kiribati":"KI", "Kosovo":"XK", "Kuwait":"KW", "Kyrgyzstan":"KG", "Laos":"LA", "Latvia":"LV", "Lebanon":"LB", "Lesotho":"LS", "Liberia":"LR", "Libya":"LY", "Liechtenstein":"LI", "Lithuania":"LT", "Luxembourg":"LU", "Macao":"MO", "North Macedonia":"MK", "Madagascar":"MG", "Malawi":"MW", "Malaysia":"MY", "Maldives":"MV", "Mali":"ML", "Malta":"MT", "Marshall Islands":"MH", "Martinique":"MQ", "Mauritania":"MR", "Mauritius":"MU", "Mayotte":"YT", "Mexico":"MX", "Micronesia":"FM", "Moldova":"MD", "Monaco":"MC", "Mongolia":"MN", "Montenegro":"ME", "Montserrat":"MS", "Morocco":"MA", "Mozambique":"MZ", "Myanmar":"MM", "Namibia":"NA", "Nauru":"NR", "Nepal":"NP", "Netherlands":"NL", "Netherlands Antilles":"AN", "New Caledonia":"NC", "New Zealand":"NZ", "Nicaragua":"NI", "Niger":"NE", "Nigeria":"NG", "Niue":"NU", "Norfolk Island":"NF", "North Korea":"KP", "Northern Mariana Islands":"MP", "Norway":"NO", "Oman":"OM", "Pakistan":"PK", "Palau":"PW", "Palestinian Territory":"PS", "Panama":"PA", "Papua New Guinea":"PG", "Paraguay":"PY", "Peru":"PE", "Philippines":"PH", "Pitcairn":"PN", "Poland":"PL", "Portugal":"PT", "Puerto Rico":"PR", "Qatar":"QA", "Congo (Brazzaville)":"CG", "Reunion":"RE", "Romania":"RO", "Russia":"RU", "Rwanda":"RW", "Saint Barthelemy":"BL", "Saint Helena":"SH", "Saint Kitts and Nevis":"KN", "Saint Lucia":"LC", "Saint Martin":"MF", "Saint Pierre and Miquelon":"PM", "Saint Vincent and the Grenadines":"VC", "Samoa":"WS", "San Marino":"SM", "Sao Tome and Principe":"ST", "Saudi Arabia":"SA", "Senegal":"SN", "Serbia":"RS", "Serbia and Montenegro":"CS", "Seychelles":"SC", "Sierra Leone":"SL", "Singapore":"SG", "Sint Maarten":"SX", "Slovakia":"SK", "Slovenia":"SI", "Solomon Islands":"SB", "Somalia":"SO", "South Africa":"ZA", "South Georgia and the South Sandwich Islands":"GS", "Korea, South":"KR", "South Sudan":"SS", "Spain":"ES", "Sri Lanka":"LK", "Sudan":"SD", "Suriname":"SR", "Svalbard and Jan Mayen":"SJ", "Swaziland":"SZ", "Sweden":"SE", "Switzerland":"CH", "Syria":"SY", "Taiwan*":"TW", "Tajikistan":"TJ", "Tanzania":"TZ", "Thailand":"TH", "Togo":"TG", "Tokelau":"TK", "Tonga":"TO", "Trinidad and Tobago":"TT", "Tunisia":"TN", "Turkey":"TR", "Turkmenistan":"TM", "Turks and Caicos Islands":"TC", "Tuvalu":"TV", "U.S. Virgin Islands":"VI", "Uganda":"UG", "Ukraine":"UA", "United Arab Emirates":"AE", "United Kingdom":"GB", "US":"US", "United States Minor Outlying Islands":"UM", "Uruguay":"UY", "Uzbekistan":"UZ", "Vanuatu":"VU", "Holy See":"VA", "Venezuela":"VE", "Vietnam":"VN", "Wallis and Futuna":"WF", "Western Sahara":"EH", "Yemen":"YE", "Zambia":"ZM", "Zimbabwe":"ZW"}
def getData(request):
    
    try:
        response = requests.get('https://coronavirus-tracker-api.herokuapp.com/all')
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print (e.response.text,'Failed: https://coronavirus-tracker-api.herokuapp.com/all')

    try:
        response2 = requests.get('https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_1.geojson')
        response2.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print (e.response.text,'Failed: https://opendata.arcgis.com/datasets/bbb2e4f589ba40d692fab712ae37b9ac_1.geojson')

    if (response.json()):
        geodata = response.json()
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
                #res_arr.append({"code3":country_code[k],"z":v,"code":k,"value":v,"recovered":res_recov_dict[k],"deaths":res_deaths_dict[k] })
                res_arr.append({"code3":country_code[k],"z":v,"code":k,"value":v,"recovered":res_recov_dict.get(k, 0),"deaths":res_deaths_dict.get(k, 0) })

        res_arr_obj=json.dumps(res_arr)
    
    res_deaths_dict2={}
    confirmed_cases={}
    recovered_cases={}
    deaths_cases={}
    res_arr2=[]
    res_arr_obj2={}
    res_obj3={}

    total_reported=0
    total_recovered=0
    total_deaths=0
    dt_data={}
    dt_data['data']=[]

    if (response2):
        geodata2 = response2.json()

        for info in geodata2['features']:
            outstr= '{},{},{},{}\n'.format(info['properties']['Country_Region'],info['properties']['Confirmed'],info['properties']['Recovered'],info['properties']['Deaths'])
            #print(outstr)
            total_reported=total_reported+info['properties']['Confirmed']
            total_recovered=total_recovered+info['properties']['Recovered']
            total_deaths=total_deaths+info['properties']['Deaths']

            if info['properties']['Country_Region'] in country_code2:
                #print(country_code2[info['properties']['Country_Region']])
                if country_code2[info['properties']['Country_Region']] in confirmed_cases:
                    confirmed_cases[country_code2[info['properties']['Country_Region']]]+=info['properties']['Confirmed']
                else:
                    confirmed_cases[country_code2[info['properties']['Country_Region']]]=info['properties']['Confirmed']
                
                if country_code2[info['properties']['Country_Region']] in recovered_cases:
                    recovered_cases[country_code2[info['properties']['Country_Region']]]+=info['properties']['Recovered']
                else:
                    recovered_cases[country_code2[info['properties']['Country_Region']]]=info['properties']['Recovered']

                if country_code2[info['properties']['Country_Region']] in deaths_cases:
                    deaths_cases[country_code2[info['properties']['Country_Region']]]+=info['properties']['Deaths']
                else:
                    deaths_cases[country_code2[info['properties']['Country_Region']]]=info['properties']['Deaths']
        
        for c3code,c2code in country_code2.items():
            outstr=None
            
            countryNameDt=None
            if c3code == 'Congo (Kinshasa)':
                countryNameDt = 'Democratic Republic of Congo (Kinshasa)'
            elif c3code == 'Congo (Brazzaville)':
                countryNameDt = 'Republic of Congo (Brazzaville)'
            else:
                countryNameDt= c3code
               
            if c2code in confirmed_cases:
                res_arr2.append({"code3":country_code[c2code],"z":confirmed_cases[c2code],"code":c2code,"value":confirmed_cases[c2code],"recovered":recovered_cases.get(c2code, 0),"deaths":deaths_cases.get(c2code, 0) })
                outstr = '{}\t{}\t{}\t{}\t{}\n'.format(c3code,country_code[c2code],confirmed_cases[c2code],recovered_cases.get(c2code, 0),deaths_cases.get(c2code, 0))
                #dt_data['data'].append([c3code,country_code[c2code],confirmed_cases[c2code],recovered_cases.get(c2code, 0),deaths_cases.get(c2code, 0)])
                dt_data['data'].append([countryNameDt,country_code[c2code],confirmed_cases[c2code],recovered_cases.get(c2code, 0),deaths_cases.get(c2code, 0)])
            else:
                res_arr2.append({"code3":country_code[c2code],"z":0,"code":c2code,"value":0,"recovered":0,"deaths":0 })
                outstr = '{}\t{}\t{}\t{}\t{}\n'.format(c3code,country_code[c2code],0,0,0)
                #dt_data['data'].append([c3code,country_code[c2code],0,0,0])
                dt_data['data'].append([countryNameDt,country_code[c2code],0,0,0])            
        
        dt_data_response=json.dumps(dt_data['data'])
        
        res_arr_obj2 = json.dumps(res_arr2)
        res_obj3={
            'total_reported':total_reported,
            'total_recovered':total_recovered,
            'total_deaths':total_deaths,
            'plotdata':res_arr2,
            'dt_table':dt_data_response
            }
    
    #print(dt_data_response)
    
    if len(res_arr_obj2) < 1: # if arcgis fails
        return JsonResponse(res_arr_obj,safe=False)
    else:
        return JsonResponse(res_obj3,safe=False)

# source: https://www.arcgis.com/home/item.html?id=c0b356e20b30490c8b8b4c7bb9554e7c&view=list#data