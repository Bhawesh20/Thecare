$( document ).on( "pagecreate", function() {
    $( ".photopopup" ).on({
        popupbeforeposition: function() {
            var maxHeight = $( window ).height() - 60 + "px";
            $( ".photopopup img" ).css( "max-height", maxHeight );
        }
    });
});
var todayDate = new Date().getDate();
 $(function () {
    $('.datetime-input').datetimepicker({
    	locale: 'en',
		format:'YYYY-MM-DD',
		minDate:new Date(new Date().setDate(todayDate + 1)),
		maxDate:new Date(new Date().setDate(todayDate + 10)),
		viewMode: 'days',
        
    });
});
 $(function () {
    $('.datetime-input2').datetimepicker({
		format:'YYYY-MM-DD',
		minDate:new Date(new Date().setDate(todayDate - 60)),
		maxDate:new Date(new Date().setDate(todayDate)),
		viewMode: 'days',
    });
});
