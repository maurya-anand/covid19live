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
country_code2={"Afghanistan":"AF", "Aland Islands":"AX", "Albania":"AL", "Algeria":"DZ", "American Samoa":"AS", "Andorra":"AD", "Angola":"AO", "Anguilla":"AI", "Antarctica":"AQ", "Antigua and Barbuda":"AG", "Argentina":"AR", "Armenia":"AM", "Aruba":"AW", "Australia":"AU", "Austria":"AT", "Azerbaijan":"AZ", "Bahamas":"BS", "Bahrain":"BH", "Bangladesh":"BD", "Barbados":"BB", "Belarus":"BY", "Belgium":"BE", "Belize":"BZ", "Benin":"BJ", "Bermuda":"BM", "Bhutan":"BT", "Bolivia":"BO", "Bonaire, Saint Eustatius and Saba":"BQ", "Bosnia and Herzegovina":"BA", "Botswana":"BW", "Bouvet Island":"BV", "Brazil":"BR", "British Indian Ocean Territory":"IO", "British Virgin Islands":"VG", "Brunei":"BN", "Bulgaria":"BG", "Burkina Faso":"BF", "Burundi":"BI", "Cambodia":"KH", "Cameroon":"CM", "Canada":"CA", "Cape Verde":"CV", "Cayman Islands":"KY", "Central African Republic":"CF", "Chad":"TD", "Chile":"CL", "China":"CN", "Christmas Island":"CX", "Cocos Islands":"CC", "Colombia":"CO", "Comoros":"KM", "Cook Islands":"CK", "Costa Rica":"CR", "Croatia":"HR", "Cuba":"CU", "Curacao":"CW", "Cyprus":"CY", "Czechia":"CZ", "Congo (Kinshasa)":"CD", "Denmark":"DK", "Djibouti":"DJ", "Dominica":"DM", "Dominican Republic":"DO", "Timor-Leste":"TL", "Ecuador":"EC", "Egypt":"EG", "El Salvador":"SV", "Equatorial Guinea":"GQ", "Eritrea":"ER", "Estonia":"EE", "Ethiopia":"ET", "Falkland Islands":"FK", "Faroe Islands":"FO", "Fiji":"FJ", "Finland":"FI", "France":"FR", "French Guiana":"GF", "French Polynesia":"PF", "French Southern Territories":"TF", "Gabon":"GA", "Gambia":"GM", "Georgia":"GE", "Germany":"DE", "Ghana":"GH", "Gibraltar":"GI", "Greece":"GR", "Greenland":"GL", "Grenada":"GD", "Guadeloupe":"GP", "Guam":"GU", "Guatemala":"GT", "Guernsey":"GG", "Guinea":"GN", "Guinea-Bissau":"GW", "Guyana":"GY", "Haiti":"HT", "Heard Island and McDonald Islands":"HM", "Honduras":"HN", "Hong Kong":"HK", "Hungary":"HU", "Iceland":"IS", "India":"IN", "Indonesia":"ID", "Iran":"IR", "Iraq":"IQ", "Ireland":"IE", "Isle of Man":"IM", "Israel":"IL", "Italy":"IT", "Cote d'Ivoire":"CI", "Jamaica":"JM", "Japan":"JP", "Jersey":"JE", "Jordan":"JO", "Kazakhstan":"KZ", "Kenya":"KE", "Kiribati":"KI", "Kosovo":"XK", "Kuwait":"KW", "Kyrgyzstan":"KG", "Laos":"LA", "Latvia":"LV", "Lebanon":"LB", "Lesotho":"LS", "Liberia":"LR", "Libya":"LY", "Liechtenstein":"LI", "Lithuania":"LT", "Luxembourg":"LU", "Macao":"MO", "North Macedonia":"MK", "Madagascar":"MG", "Malawi":"MW", "Malaysia":"MY", "Maldives":"MV", "Mali":"ML", "Malta":"MT", "Marshall Islands":"MH", "Martinique":"MQ", "Mauritania":"MR", "Mauritius":"MU", "Mayotte":"YT", "Mexico":"MX", "Micronesia":"FM", "Moldova":"MD", "Monaco":"MC", "Mongolia":"MN", "Montenegro":"ME", "Montserrat":"MS", "Morocco":"MA", "Mozambique":"MZ", "Myanmar":"MM", "Namibia":"NA", "Nauru":"NR", "Nepal":"NP", "Netherlands":"NL", "Netherlands Antilles":"AN", "New Caledonia":"NC", "New Zealand":"NZ", "Nicaragua":"NI", "Niger":"NE", "Nigeria":"NG", "Niue":"NU", "Norfolk Island":"NF", "North Korea":"KP", "Northern Mariana Islands":"MP", "Norway":"NO", "Oman":"OM", "Pakistan":"PK", "Palau":"PW", "Palestinian Territory":"PS", "Panama":"PA", "Papua New Guinea":"PG", "Paraguay":"PY", "Peru":"PE", "Philippines":"PH", "Pitcairn":"PN", "Poland":"PL", "Portugal":"PT", "Puerto Rico":"PR", "Qatar":"QA", "Congo (Brazzaville)":"CG", "Reunion":"RE", "Romania":"RO", "Russia":"RU", "Rwanda":"RW", "Saint Barthelemy":"BL", "Saint Helena":"SH", "Saint Kitts and Nevis":"KN", "Saint Lucia":"LC", "Saint Martin":"MF", "Saint Pierre and Miquelon":"PM", "Saint Vincent and the Grenadines":"VC", "Samoa":"WS", "San Marino":"SM", "Sao Tome and Principe":"ST", "Saudi Arabia":"SA", "Senegal":"SN", "Serbia":"RS", "Serbia and Montenegro":"CS", "Seychelles":"SC", "Sierra Leone":"SL", "Singapore":"SG", "Sint Maarten":"SX", "Slovakia":"SK", "Slovenia":"SI", "Solomon Islands":"SB", "Somalia":"SO", "South Africa":"ZA", "South Georgia and the South Sandwich Islands":"GS", "Korea, South":"KR", "South Sudan":"SS", "Spain":"ES", "Sri Lanka":"LK", "Sudan":"SD", "Suriname":"SR", "Svalbard and Jan Mayen":"SJ", "Swaziland":"SZ", "Sweden":"SE", "Switzerland":"CH", "Syria":"SY", "Taiwan*":"TW", "Tajikistan":"TJ", "Tanzania":"TZ", "Thailand":"TH", "Togo":"TG", "Tokelau":"TK", "Tonga":"TO", "Trinidad and Tobago":"TT", "Tunisia":"TN", "Turkey":"TR", "Turkmenistan":"TM", "Turks and Caicos Islands":"TC", "Tuvalu":"TV", "U.S. Virgin Islands":"VI", "Uganda":"UG", "Ukraine":"UA", "United Arab Emirates":"AE", "United Kingdom":"GB", "US":"US", "United States Minor Outlying Islands":"UM", "Uruguay":"UY", "Uzbekistan":"UZ", "Vanuatu":"VU", "Holy See":"VA", "Venezuela":"VE", "Vietnam":"VN", "Wallis and Futuna":"WF", "Western Sahara":"EH", "Yemen":"YE", "Zambia":"ZM", "Zimbabwe":"ZW"}
def getData(request):
    try:
        res = requests.get('https://api.covid19api.com/summary')
    except requests.exceptions.HTTPError as e:
        print (e.response.text,'Failed: https://api.covid19api.com/summary')

    if res:
        resp_data = res.json()
        # print (resp_data)
        # print (resp_data['Message'])
        # print (resp_data['Global'])
        # print (resp_data['Countries'])
        print (resp_data['Date'])
        
        newconfirmed = 0
        totalconfirmed = 0
        newdeaths = 0
        totaldeaths = 0
        newrecovered = 0
        totalrecovered = 0
        date = 0

        if resp_data['Global']['NewConfirmed']:
            newconfirmed = resp_data['Global']['NewConfirmed']

        if resp_data['Global']['TotalConfirmed']:
            totalconfirmed = resp_data['Global']['TotalConfirmed']

        if resp_data['Global']['NewDeaths']:
            newdeaths = resp_data['Global']['NewDeaths']

        if resp_data['Global']['TotalDeaths']:
            totaldeaths = resp_data['Global']['TotalDeaths']

        if resp_data['Global']['NewRecovered']:
            newrecovered = resp_data['Global']['NewRecovered']

        if resp_data['Global']['TotalRecovered']:
            totalrecovered = resp_data['Global']['TotalRecovered']

        if resp_data['Global']['Date']:
            date = resp_data['Global']['Date']

        out_dict = {
            "NewConfirmed":newconfirmed,
            "TotalConfirmed":totalconfirmed,
            "NewDeaths":newdeaths,
            "TotalDeaths":totaldeaths,
            "NewRecovered":newrecovered,
            "TotalRecovered":totalrecovered,
            "Date":date
        }
        total_recovered = totalconfirmed- newconfirmed
        print (out_dict)

    res_arr2=[]
    res_arr_obj2={}
    res_obj3={}

    dt_data={}
    dt_data['data']=[]
        
    for stats in resp_data['Countries']:
        # print (stats)
        total_recov = stats['TotalConfirmed']- stats['NewConfirmed']
        res_arr2.append({"code3":country_code[stats['CountryCode']],"z":stats['NewConfirmed'],"code":stats['CountryCode'],"value":stats['NewConfirmed'],"recovered":total_recov,"deaths":stats['TotalDeaths'],"active":stats['NewConfirmed'] })
        dt_data['data'].append([stats['Country'],country_code[stats['CountryCode']],stats['NewConfirmed'],total_recov,stats['TotalDeaths'],stats['TotalConfirmed']]) 

    dt_data_response=json.dumps(dt_data['data'])
    res_arr_obj2 = json.dumps(res_arr2)
    # print(res_arr_obj2)
    res_obj3={
        'total_reported':totalconfirmed,
        'total_recovered':total_recovered,
        'total_deaths':totaldeaths,
        'total_active':newconfirmed,
        'plotdata':res_arr2,
        'dt_table':dt_data_response
        }
    
    #print(dt_data_response)
    
    return JsonResponse(res_obj3,safe=False)

# source country wise data: https://www.arcgis.com/home/item.html?id=c0b356e20b30490c8b8b4c7bb9554e7c&view=list#data
# source time series: https://coronavirus-resources.esri.com/datasets/1cb306b5331945548745a5ccd290188e_4
# source time series api: https://opendata.arcgis.com/datasets/1cb306b5331945548745a5ccd290188e_4.geojson

# new source for country-wise data
# https://api.covid19api.com/
# https://documenter.getpostman.com/view/10808728/SzS8rjbc
# https://api.covid19api.com/summary