$(document).ready(function(){

  var onSuccess = function(stuff, status) {
    console.log("Hello");
    $("#fractal").empty();
    $('#fractal').prepend('<img id="fractal" href="static/duck.png" />')
  };

  var onError = function(data, status) {
    console.log("status", status);
    console.log("error", data);
  };

  $("#searchTopic").submit(function(event) {
    event.preventDefault();

    var topic = $("#searchTopic").find("[name='topic']").val();
    var tu = $("#searchTopic").find("[name='tu']").val();
    var source = $("#searchTopic").find("[name='source']").val();

    $.post("topic_results", {
      topic: topic,
      tu: tu,
      source: source
    })
      .done(onSuccess)
      .error(onError);
  });
});
