from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from requests.exceptions import HTTPError
import time


def index(request):
    return render(request, "tracker/index.html")


global_stats_source_api = 'https://disease.sh/v3/covid-19/all'
per_country_stats_source_api = 'https://disease.sh/v3/covid-19/countries'


def make_request(url: str, max_attempt: int = 5):
    retries = 0
    success = False
    while not success and retries <= max_attempt:
        try:
            response = requests.get(url)
            response.raise_for_status()
            jsonResponse = response.json()
            return (jsonResponse)
            success = True
        except Exception as err:
            wait = retries * 2
            print(f"{err} >Retrying attempt {retries}<")
            time.sleep(wait)
            retries += 1


def getData(request):
    res_obj3 = {
        'total_reported': None,
        'total_recovered': None,
        'total_deaths': None,
        'total_active': None,
        'plotdata': [],
        'dt_table': []
    }
    global_stats_res = make_request(url=global_stats_source_api)
    if (global_stats_res):
        if 'cases' in global_stats_res:
            res_obj3['total_reported'] = global_stats_res['cases']
        if 'recovered' in global_stats_res:
            res_obj3['total_recovered'] = global_stats_res['recovered']
        if 'deaths' in global_stats_res:
            res_obj3['total_deaths'] = global_stats_res['deaths']
        if 'active' in global_stats_res:
            res_obj3['total_active'] = global_stats_res['active']
    res_arr2 = []
    dt_data = {'data': []}
    per_country_stats_stats_res = make_request(
        url=per_country_stats_source_api)
    if (per_country_stats_stats_res):
        for country in per_country_stats_stats_res:
            if 'active' in country and 'countryInfo' in country and 'iso3' in country['countryInfo'] and country['countryInfo']['iso3'] and country['active']:
                res_arr2.append({
                    "code3": country['countryInfo']['iso3'],
                    "z": country['active'],
                    "code": country['countryInfo']['iso2'],
                    "value": country['active'],
                    "recovered": country['recovered'],
                    "deaths": country['deaths'],
                    "active": country['active']
                })
                dt_data['data'].append([country['country'],
                                        country['countryInfo']['iso3'],
                                        country['active'],
                                        country['recovered'],
                                        country['deaths'],
                                        country['cases']]
                                       )
    res_obj3 = {
        'total_reported': None,
        'total_recovered': None,
        'total_deaths': None,
        'total_active': None,
        'plotdata': json.dumps(res_arr2),
        'dt_table': dt_data['data'],
    }
    print(json.dumps(res_arr2))
    print(json.dumps(dt_data['data']))
    return JsonResponse(res_obj3, safe=False)
