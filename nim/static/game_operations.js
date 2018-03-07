var maxPiles = 5;

$("document").ready(newGame);

function newGame() {
  $.ajax({
    type:"POST",
    url: "/new",
    data: JSON.stringify({
      "min": parseInt($('#minPerPile').val()),
      "max": parseInt($('#maxPerPile').val()),
      "piles": parseInt($('#numPiles').val())
    }),
    contentType: "application/json; charset=utf-8",
    dataType : 'json',
    success: updatePage
  });
};

function updateGameState() {
  $.getJSON( "/update", updatePage);
};

function updatePage( json ) {
    $( "#piles" ).empty();
    for (i = 0; i < json.state.length; i++) {
        $( "#piles" ).append( '<div style="float: left;"><h1>' + json.state[i] + '</h1></div>' );
    }
    console.log( "JSON Data: " + json.state );
};
