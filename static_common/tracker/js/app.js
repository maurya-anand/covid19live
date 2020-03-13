
getLiveData ();

function getLiveData (){
    $.ajax({
        url:'https://coronavirus-tracker-api.herokuapp.com/all',
        type: 'GET',
        success: function(response){
            //console.log(response);
            
            var total_cases= response.latest['confirmed'];
            var total_deaths= response.latest['deaths'];
            var total_recovered= response.latest['recovered'];
            
            var total_confirmed_cases= response.confirmed['latest'];
            var last_updated_confirmed_cases= response.confirmed['last_updated'];

            var total_recovered_cases= response.recovered['latest'];
            var last_updated_recovered_cases= response.recovered['last_updated'];

            var total_death_cases= response.deaths['latest'];
            var last_updated_death_cases= response.deaths['last_updated'];
            
            //$('#total_confirmed_cases').text(total_confirmed_cases);
            $('#last_updated_confirmed').text(new Date(Date.parse(last_updated_confirmed_cases)));

            //$('#total_recovered_cases').text(total_recovered_cases);
            $('#last_updated_recovered').text(new Date(Date.parse(last_updated_recovered_cases)));

            //$('#total_death_cases').text(total_death_cases);
            $('#last_updated_death').text(new Date(Date.parse(last_updated_death_cases)));
       
        },
        error: function(){
            console.log("no data received from the server");
        }
    });
}


Highcharts.getJSON('data/', function (data) {
    //data_series= JSON.parse(data);
    var data_series = data["plotdata"];
    if (data_series){
        //console.log(data_series);
        data_series= data.plotdata;
        $('#total_confirmed_cases').text(data.total_reported);
        $('#total_recovered_cases').text(data.total_recovered);
        $('#total_death_cases').text(data.total_deaths);
    }
    else {
        data_series= JSON.parse(data);
    }
    
    // Prevent logarithmic errors in color calulcation
    data_series.forEach(function (p) {
        p.value = (p.value < 1 ? 1 : p.value);
    });
    //console.log(data_series);
    Highcharts.mapChart('hc_container', {
        loading: {
            hideDuration: 8000,
            showDuration: 9000
        },
        chart: {
            //borderWidth: 1,
            map: 'custom/world',
        },

        title: {
            text: 'Global cases of corona virus',
        },

        subtitle: {
            text: 'Hover on the country to view details'
        },

        legend: {
            enabled: false
        },

        mapNavigation: {
            enabled: true,
            // buttonOptions: {
            //     verticalAlign: 'bottom'
            // }
        },

        colorAxis: {
            minColor: '#000fb0',
            min: 1,
            max: 10000,
            type: 'logarithmic'
        },

        credits: {
            enabled: false
        },

        plotOptions: {
            map: {
                allAreas: false,
                joinBy: ['iso-a2', 'code'],
                dataLabels: {
                    enabled: true,
                    //color: '#FFFFFF',
                    // Only show dataLabels for areas with high label rank
                    format: null,
                    formatter: function() {
                        if (this.point.properties && this.point.properties.labelrank.toString() < 5) {
                            return this.point.properties['iso-a2'];
                        }
                    }
                },
                tooltip: {
                    headerFormat: '',
                    pointFormat: '{point.name}: <b>{series.name}</b>'
                }
            },
        
        },

        series: [
            {
                name: 'Countries',
                //color: '#E0E0E0',
                nullColor: 'red',
                enableMouseTracking: false
            },
            {
                //type: 'mapbubble',
                name: 'Total cases in',
                joinBy: ['iso-a3', 'code3'],
                data: data_series,
                minSize: 4,
                maxSize: '15%',
                tooltip: {
                    useHTML: true,
                    //pointFormat: '<span style="font-size:12px">{point.name} ({point.properties.hc-a2}):</span><br><span style="font-size:20px">{point.z}</span>'
                    //pointFormat: '<span style="font-size:12px">{point.name} ({point.properties.hc-a2}):</span><br>Confirmed:<span style="font-size:20px"> {point.z}</span><br>Recovered:<span style="font-size:20px"> {point.recovered}</span><br>Deaths:<span style="font-size:20px"> {point.deaths}</span>'
                    pointFormat: '<span style="font-size:20px">{point.name}<br></span><br></br>' +
                    '<span style="font-size:12px;">Confirmed: </span><span style="font-size:15px"> {point.z}</span><br><br>' +
                    '<span style="font-size:12px; color:green">Recovered: </span><span style="font-size:15px"> {point.recovered}</span><br><br>' +
                    '<span style="font-size:12px; color:red">Deaths: </span><span style="font-size:15px"> {point.deaths}</span>'
                    
                },
            }
        ]
    });

});
