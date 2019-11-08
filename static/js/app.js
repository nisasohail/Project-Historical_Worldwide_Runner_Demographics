function buildCharts(country) {
  d3.json(`/gender/${country}`).then((data2) => {
    const Country = data2.country;
    const Gender = data2.gender;
    const Count = data2.noOfAthletes;

    var pieData = [
      {
        values: Count,
        labels: Gender,
        hovertext: Country,
        hoverinfo: "hovertext",
        type: "pie",

      }
    ];

    var pieLayout = {
      title: "Gender Proportion By Country",
      margin: { t: -0.5, l: 0 },
      color: "Yellow"
    };

    Plotly.plot("pie", pieData, pieLayout);
  });
}

function init() {
  var selector = d3.select("#selDataset");
  d3.json("/countryList").then((dataNames) => {
    dataNames.forEach((data) => {
      selector
        .append("option")
        .text(data)
        .property("value", data);
      });
    const firstdata = dataNames.country[0];
    buildCharts(firstdata);
  });
}

//////////////////////////////////////////////////////////////////////
function buildCharts1(country) {
  d3.json(`/agegroup/${country}`).then((data2) => {
    const Country1 = data2.country;
    const Agegroup1 = data2.agegroup;
    const Gender1 = data2.gender;
    const Count1 = data2.noOfAthletes;
    
    var trace = {
      x: Agegroup1,
      y: Count1,
      text: Country1,
      name: "Agegroup",
      type: "bar",
      orientation: "v"
    };

    var data = [trace];
    
    var layout = {
      title: "Distribution By Age Group",
      margin: {
        l: 50,
        r: 50,
        t: 50,
        b: 50
      }
    };
    
    Plotly.newPlot("bar", data, layout);
  });
} 

///////////////////////////////////////////////////////////////

function buildCharts2(country) {
  d3.json(`/event_detail/${country}`).then((data2) => {
    const Country2 = data2.country;
    const Gender2 = data2.gender;
    const Count2 = data2.noOfAthletes;
    const Event2 = data2.event;
    
    var trace = {
      x: Event2,
      y: Count2,
      text: Country2,
      name: "Events",
      type: "bar",
      orientation: "v"
    };

    var data = [trace];
    
    var layout = {
      title: "Count of People By Running Event",
      margin: {
        l: 50,
        r: 50,
        t: 50,
        b: 50
      }
    };
    
    Plotly.newPlot("bar1", data, layout);
  });
} 
//////////////////////////////////////////////////////////////////
function buildCharts3(country) {
  d3.json(`/men/${country}`).then((data6) => {
    const Country3 = data6.country;
    const Agegroup3 = data6.agegroup;
    const Count3 = data6.noOfAthletes;

    var trace = {
      x: Agegroup3,
      y: Count3,
      text: Country3,
      name: "Men",
      type: "line",
      orientation: "v"
    };

    var data = [trace];
    

    var layout = {
      title: "Count of Men by Age Group",
      margin: {
        l: 50,
        r: 50,
        t: 50,
        b: 50
      }
    };
    
    Plotly.newPlot("bar2", data, layout);
  });
} 
///////////////////////////////////////////////////////////////

function buildCharts4(country2) {
  d3.json(`/age/${country2}`).then((data7) => {
    const Country4 = data7.country;
    const Agegroup4 = data7.agegroup;
    const Gender4 = data7.gender;
    const MenCount4 = data7.mencount;
    const WomenCount4 = data7.womencount;

    var trace = {
      x: Agegroup4,
      y: MenCount4,
      text: Country4,
      name: "Men",
      type: "line",
      orientation: "v"
    };

    var trace1 = {
      x: Agegroup4,
      y: WomenCount4,
      text: Country4,
      name: "Women",
      type: "line",
      orientation: "v"
    };

    var data = [trace, trace1];
    

    var layout = {
      title: "Count of Men and Women by Age Group",
      margin: {
        l: 50,
        r: 50,
        t: 50,
        b: 50
      }
    };
    
    Plotly.newPlot("bar3", data, layout);
  });
} 

/////////////////////////////////////////////////////////////////

function optionChanged(newdata) {
  buildCharts(newdata);
  buildCharts1(newdata);
  buildCharts2(newdata);
  buildCharts3(newdata);
  buildCharts4(newdata);
}

init();

