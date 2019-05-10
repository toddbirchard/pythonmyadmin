// A $( document ).ready() block.
$( document ).ready(function() {
    console.log( "ready!" );

    $('button').on('click', function(e){
      $(this).toggleClass('inactive');
      console.log('etf');
    });

    $('#avi-filter').on('click', function(){
      $('.dash-cell-value:contains(avi)').closest('tr').toggleClass('hidden');
    });

    $('#basic-filter').on('click', function(){
      $('.dash-cell-value:contains(basic)').closest('tr').toggleClass('hidden');
    });

    $('#crypto-filter').on('click', function(){
      $('.dash-cell-value:contains(crypto)').closest('tr').toggleClass('hidden');
    });

    $('#goal-filter').on('click', function(){
      $('.dash-cell-value:contains(goal)').closest('tr').toggleClass('hidden');
    });

    $('#etc-filter').on('click', function(){
      $('.dash-cell-value:contains(random)').closest('tr').toggleClass('hidden');
    });
});
