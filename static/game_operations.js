var maxPiles = 5;

$("document").ready(newGame);

function newGame() {
  $.getJSON( "/new", updatePage);
};

function updateGameState() {
  $.getJSON( "/update", updatePage);
};

function updatePage( json ) {
    for (i = 0; i <= maxPiles; i++) {
        $( "#pile" + i ).html( json.state[i] );
    }
    console.log( "JSON Data: " + json.state );
};
