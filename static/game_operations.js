$("document").ready(newGame);

function update() {
  $.getJSON( "/update", function( json ) {
    $( "#pile0" ).html( json.state[0] );
    $( "#pile1" ).html( json.state[1] );
    $( "#pile2" ).html( json.state[2] );
    $( "#pile3" ).html( json.state[3] );
    $( "#pile4" ).html( json.state[4] );
    console.log( "JSON Data: " + json.state );
  });
};

function newGame() {
  $.getJSON( "/new", function( json ) {
    $( "#pile0" ).html( json.state[0] );
    $( "#pile1" ).html( json.state[1] );
    $( "#pile2" ).html( json.state[2] );
    $( "#pile3" ).html( json.state[3] );
    $( "#pile4" ).html( json.state[4] );
    console.log( "JSON Data: " + json.state );
  });
};
