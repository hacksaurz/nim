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
    success: function( json ) { updatePage( json.state ) }
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
    contentType: "application/json; charset=utf-8",
    dataType : 'json',
    success: applyMoves
  });
};

function applyMoves( json ) {
  if ( json.playerState ) {
    updatePage( json.playerState )
  }

  if ( json.botState && !$('#delay').is(":checked") ) {
    setTimeout(function() { updatePage( json.botState ) }, 100);
  }

  else if ( json.botState ) {
    setTimeout(function() { updatePage( json.botState ) }, 1000);
  }

  console.log( "JSON Data: " + json );
};

function updatePage( state ) {
    $( "#piles" ).empty();
    for (i = 0; i < state.length; i++) {
        $( "#piles" ).append( '<div style="float: left;"><h1>' + state[i] + '</h1></div>' );
    }
    console.log( "State: " + state );
};
