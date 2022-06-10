getLiveData();

function getLiveData() {
  $.ajax({
    url: "https://coronavirus-tracker-api.herokuapp.com/all",
    type: "GET",
    success: function (response) {
      //console.log(response);

      var total_cases = response.latest["confirmed"];
      var total_deaths = response.latest["deaths"];
      var total_recovered = response.latest["recovered"];

      var total_confirmed_cases = response.confirmed["latest"];
      var last_updated_confirmed_cases = response.confirmed["last_updated"];

      var total_recovered_cases = response.recovered["latest"];
      var last_updated_recovered_cases = response.recovered["last_updated"];

      var total_death_cases = response.deaths["latest"];
      var last_updated_death_cases = response.deaths["last_updated"];

      // $('#total_confirmed_cases').text(total_confirmed_cases);
      $("#last_updated_confirmed").text(
        new Date(Date.parse(last_updated_confirmed_cases))
      );

      // console.log(new Date().toLocaleString());
      //$('#total_recovered_cases').text(total_recovered_cases);
      $("#last_updated_recovered").text(
        new Date(Date.parse(last_updated_recovered_cases))
      );
      $("#last_updated_active").text(
        new Date(Date.parse(last_updated_recovered_cases))
      );

      //$('#total_death_cases').text(total_death_cases);
      $("#last_updated_death").text(
        new Date(Date.parse(last_updated_death_cases))
      );
    },
    error: function () {
      console.log(
        "no data received from the server. Falling back to default time"
      );
      $("#last_updated_confirmed").text(new Date().toLocaleString());
      $("#last_updated_recovered").text(new Date().toLocaleString());
      $("#last_updated_death").text(new Date().toLocaleString());
    },
  });
}

Highcharts.getJSON("data/", function (data) {
  //data_series= JSON.parse(data);
  var data_series = data["plotdata"];
  if (data_series) {
    data_series = data.plotdata;
    $("#total_confirmed_cases").text(data.total_reported);
    $("#total_recovered_cases").text(data.total_recovered);
    $("#total_death_cases").text(data.total_deaths);
    $("#total_active_cases").text(data.total_active);
    createTable(data.dt_table);
  } else {
    data_series = JSON.parse(data);
  }

  // Prevent logarithmic errors in color calulcation
  data_series.forEach(function (p) {
    p.value = p.value < 1 ? 1 : p.value;
  });
  //console.log(data_series);
  Highcharts.mapChart("hc_container", {
    chart: {
      //height: '40%',
      //borderWidth: 0.5,
      marginBottom: 0,
      spacingBottom: 0,
      map: "custom/world",
      zoomType: "xy",
    },

    mapNavigation: {
      enabled: false,
      //enableDoubleClickZoomTo: false,
      //enableMouseWheelZoom: true,
      // buttonOptions: {
      //     verticalAlign: 'bottom'
      // }
    },

    title: {
      //useHTML: true,
      text: "Current status of Coronavirus disease (COVID-19) pandemic",
    },

    subtitle: {
      text: "Hover or click on the country to view details. Select any area on the map to zoom.",
    },

    legend: {
      enabled: false,
    },

    // colors: ["#ca0020", "#f4a582", "#f7f7f7", "#92c5de", "#0571b0"],

    colorAxis: {
      min: 1,
      max: 10000,
      type: "logarithmic",
      // minColor: '#d4edda',  #ffffff',  #ece2f0
      // maxColor: '#007bff',
      stops: [
        [0, "#2b83ba"],
        [0.5, "#92c5de"],
        [0.9, "#c4463a"],
      ],
    },

    credits: {
      enabled: false,
    },

    plotOptions: {
      map: {
        allAreas: false,
        joinBy: ["iso-a2", "code"],
        dataLabels: {
          enabled: true,
          //color: '#FFFFFF',
          // Only show dataLabels for areas with high label rank
          format: null,
          formatter: function () {
            if (
              this.point.properties &&
              this.point.properties.labelrank.toString() < 5
            ) {
              return this.point.properties["iso-a2"];
            }
          },
        },
        tooltip: {
          headerFormat: "",
          pointFormat: "{point.name}: <b>{series.name}</b>",
        },
      },
    },

    series: [
      {
        name: "Countries",
        //color: '#E0E0E0',
        //nullColor: 'red',
        enableMouseTracking: false,
      },
      {
        //type: 'mapbubble',
        name: "Total cases in",
        joinBy: ["iso-a3", "code3"],
        data: data_series,
        minSize: 4,
        maxSize: "15%",
        tooltip: {
          useHTML: true,
          //pointFormat: '<span style="font-size:12px">{point.name} ({point.properties.hc-a2}):</span><br><span style="font-size:20px">{point.z}</span>'
          //pointFormat: '<span style="font-size:12px">{point.name} ({point.properties.hc-a2}):</span><br>Confirmed:<span style="font-size:20px"> {point.z}</span><br>Recovered:<span style="font-size:20px"> {point.recovered}</span><br>Deaths:<span style="font-size:20px"> {point.deaths}</span>'
          pointFormat:
            '<span style="font-size:20px">{point.name}<br></span><br></br>' +
            '<span style="font-size:12px;">Active: </span><span style="font-size:15px"> {point.z}</span><br><br>' +
            '<span style="font-size:12px; color:green">Recovered: </span><span style="font-size:15px"> {point.recovered}</span><br><br>' +
            '<span style="font-size:12px; color:red">Deaths: </span><span style="font-size:15px"> {point.deaths}</span>',
        },
      },
    ],
  });
});

function createTable(dataSet) {
  console.log(dataSet);
  var table = $("#cases_dt").DataTable({
    dom:
      "<'d-flex justify-content-center mt-2'<'pb-0'f>>" +
      "<'row'<'col-sm-12'tr>>" +
      "<'row align-items-center'<'col justify-content-center'p>>",
    language: {
      searchPlaceholder: "Country ...",
      search: "Filter by:",
      zeroRecords: "No data available",
    },
    data: JSON.parse(dataSet),
    columns: [
      { title: "Country", width: "30%" },
      { title: "Code", visible: false },
      { title: "Active", searchable: false },
      { title: "Recovered", searchable: false },
      { title: "Deaths", searchable: false },

      { title: "Total cases", searchable: false },
    ],
    order: [
      [2, "desc"],
      [0, "asc"],
    ],
    paging: false,
    //scrollY: 300,
    scrollY: "70vh",
    scrollX: true,
    pageLength: 50,
  });
}

$("#loadNextstrain").click(function () {
  $("#nxtFrame").attr(
    "src",
    "https://nextstrain.org/ncov/global?sidebar=closed"
  );
});
