console.log("js added");

getLiveData();

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