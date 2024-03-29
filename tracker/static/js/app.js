getLiveData();

function getLiveData() {
  $.ajax({
    url: "https://coronavirus-tracker-api.herokuapp.com/all",
    type: "GET",
    success: function (response) {
      var last_updated_confirmed_cases = response.confirmed["last_updated"];
      var last_updated_recovered_cases = response.recovered["last_updated"];
      var last_updated_death_cases = response.deaths["last_updated"];
      $("#last_updated_confirmed").text(
        new Date(Date.parse(last_updated_confirmed_cases))
      );
      $("#last_updated_recovered").text(
        new Date(Date.parse(last_updated_recovered_cases))
      );
      $("#last_updated_active").text(
        new Date(Date.parse(last_updated_recovered_cases))
      );
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
  data_series = JSON.parse(data["plotdata"]);
  if (data_series) {
    $("#total_confirmed_cases").text(data.total_reported);
    $("#total_recovered_cases").text(data.total_recovered);
    $("#total_death_cases").text(data.total_deaths);
    $("#total_active_cases").text(data.total_active);
    createTable(data.dt_table);
  } else {
    data_series = JSON.parse(data);
  }
  // Prevent logarithmic errors in color calculation
  data_series.forEach(function (p) {
    p.value = p.value < 1 ? 1 : p.value;
  });
  Highcharts.mapChart("hc_container", {
    chart: {
      height: 55 + "%",
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
      type: "logarithmic",
      minColor: "#7928CA",
      maxColor: "#FF0080",
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
  $("#cases_dt").DataTable({
    data: dataSet,
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
    scrollY: 62 + "vh",
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
