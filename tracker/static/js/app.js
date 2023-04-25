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
      $("#last_updated_active").text(new Date().toLocaleString());
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
      height: (3 / 4) * 100 + "%",
      // height: "74%",
      //borderWidth: 0.5,
      marginBottom: 0,
      spacingBottom: 0,
      map: "custom/world",
      zoomType: "xy",
    },
    mapNavigation: {
      enabled: false,
    },
    title: {
      text: "Current status of Coronavirus disease (COVID-19) pandemic",
    },
    subtitle: {
      text: "Hover or click on the country to view details. Select any area on the map to zoom.",
    },
    legend: {
      enabled: false,
    },
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
        enableMouseTracking: false,
      },
      {
        name: "Total cases in",
        joinBy: ["iso-a3", "code3"],
        data: data_series,
        minSize: 4,
        maxSize: "15%",
        tooltip: {
          useHTML: true,
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

$(".btn-primary").click(function () {
  $(".collapse").collapse("toggle");
  $("#nxtFrame").attr(
    "src",
    "https://nextstrain.org/ncov/global?sidebar=closed"
  );
});

function createTable(dataSet) {
  // getting the height of the row that contains the map and the table
  $scrollHeight = $("#main_content").height() - 70;
  console.log($scrollHeight);
  $("#cases_dt").DataTable({
    data: JSON.parse(dataSet),
    columns: [
      { title: "Country" },
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
    scrollY: $scrollHeight + "vh",
    // scrollY: "72vh",
    scrollCollapse: true,
    paging: false,
    language: {
      search: "",
      searchPlaceholder: "Search country",
      zeroRecords: "No data available",
    },
    pageResize: true,
    dom: '<"top"f>rt<"bottom"><"clear">',
  });
}
