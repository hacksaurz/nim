var pileLeft = '<div style="float: left;"><h1>';
var pileRight = '</h1></div>';
var contTypeJSON = "application/json; charset=utf-8";


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
    contentType: contTypeJSON,
    dataType : 'json',
    success: updatePage
  });
};

function updateGameState() {
  $.ajax({
    type:"POST",
    url: "/update",
    data: JSON.stringify({
      "pile": parseInt($('#pile').val()) - 1,
      "stones": parseInt($('#stones').val()),
    }),
    contentType: contTypeJSON,
    dataType : 'json',
    success: updatePage
  });
};

function updatePage( json ) {
    $( "#piles" ).empty();
    for (i = 0; i < json.state.length; i++) {
        $( "#piles" ).append( pileLeft + json.state[i] + pileRight );
    }
    console.log( "JSON Data: " + json.state );
};
