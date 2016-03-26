$(document).ready(function(){

  var onSuccess = function(stuff, status) {
    $("#svgchart").empty();

    console.log(stuff)

    var names = [],
        data = [],
        topic = stuff.topic;


    for (var property in stuff.stuff) {

       if ( ! stuff.stuff.hasOwnProperty(property)) {
          continue;
       }

       names.push(property);
       data.push(stuff.stuff[property]);

    };

    console.log(names);
    console.log(data);

    var margin = {top: 20, right: 0, bottom: 30, left: 40},
        width = 900 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var y = d3.scale.linear()
        .range([height, 0]);

    var x = d3.scale.ordinal()
        .rangeRoundBands([0, width], .1)
        .domain(names.map(function(d) { return d; }));

    var chart = d3.select(".chart")
        .attr("width", width + 45)
        .attr("height", height + 50)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var barWidth = width / data.length;

    var bar = chart.selectAll("g")
        .data(data)
      .enter().append("g")
        .attr("transform", function(d, i) { return "translate(" + i * barWidth + ",0)"; });

    bar.append("rect")
        .attr("y", function(d) { return y(d); })
        .attr("height", function(d) { return height - y(d); })
        .attr("width", barWidth - 1);

    bar.append("text")
        .attr("x", barWidth / 2 + 15)
        .attr("y", function(d) { return y(d) + 3; })
        .attr("dy", ".75em")
        .text(function(d) { return d; });

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    chart.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    chart.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Subjectivity");

    chart.append("text")
        .attr("x", (width / 2) + 95)
        .attr("y", 0 - (margin.top / 2) + 10)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("fill", "#586e75")
        .text("Subjectivity for Topic '"+topic+"'");
  };

  var onError = function(data, status) {
    console.log("status", status);
    console.log("error", data);
  };

  $("#searchTopic").submit(function(event) {
    event.preventDefault();

    var topic = $("#searchTopic").find("[name='topic']").val();

    $.post("topic_results", {
      topic: topic
    })
      .done(onSuccess)
      .error(onError);
  });
});
