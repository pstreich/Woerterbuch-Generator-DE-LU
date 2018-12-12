// Steuert die Anzeige der Tabellenfelder, oeffnen und schliessen bei onclick   
   $('.key_ger').on('click', function(){
    if($(this).hasClass('selected')){
    	$(this).removeClass('selected')
    }
    else {
    	$(this).addClass('selected');
    }    
});

   $('.key_lux').on('click', function(){
    if($(this).hasClass('selected')){
    	$(this).removeClass('selected')
    }
    else {
    	$(this).addClass('selected');
    }    
});

   $('th.vorkommen').on('click', function(){
    if($(this).hasClass('selected')){
    	$(this).removeClass('selected')
    }
    else {
    	$(this).addClass('selected');
    }    
});

   $('th.vorschlag').on('click', function(){
    if($(this).hasClass('selected')){
    	$(this).removeClass('selected')
    }
    else {
    	$(this).addClass('selected');
    }    
});

   $('th.vorkommen_lux').on('click', function(){
    if($(this).hasClass('selected')){
    	$(this).removeClass('selected')
    }
    else {
    	$(this).addClass('selected');
    }    
});

   $('th.vorschlag_lux').on('click', function(){
    if($(this).hasClass('selected')){
    	$(this).removeClass('selected')
    }
    else {
    	$(this).addClass('selected');
    }    
});

// Erstellt grüne Highlight Animation
function jump(event){
	var elm=$( event.target );
	
	$(".key_lux").each(function(i, current){
    	var str=$(current).text();

    	if(elm.text()==str){
        	var lux_hit=$(current);
        	elm.effect("highlight",{color:"#669966"},2000);
        	lux_hit.effect("highlight",{color:"#669966"},2000);
    		$([document.documentElement, document.body]).animate({scrollTop: lux_hit.offset().top}, 2000);
    		jumpTo(lux_hit);
    	}
	});
}

// Markiert geklicktes Element(Wort) und dessen Kindelemente(Woerter in den Saetzen)
function mark(event) {
	var elm=$( event.target );
    var wortform;

    if(elm.hasClass("key_ger")){
        if(elm.hasClass("key_ger_lemma")){wortform=elm.next("p.key_ger_token").text();}
        else{wortform=elm.children("p.key_ger_token").text();}
        elm.parent().next().children().mark(elm.next("p.key_ger_token").text(),{"accuracy":{"value":"exactly","limiters":[",",".",":"]}});
        elm.next().children().mark(wortform,{"accuracy":{"value":"exactly","limiters":[",",".",":"]}});
    }else if(elm.hasClass("key_lux")){
        elm.parent().next().children().mark(elm.text(),{"accuracy":{"value":"exactly","limiters":[",",".",":"]}});
        elm.next().children().mark(elm.children("p").text(),{"accuracy":{"value":"exactly","limiters":[",",".",":","’"]}});
    }

	

    if(elm.hasClass("key_ger")){    
	    $(".key_lux").each(function(i, current){
	        var str=$(current).text();

	        if(elm.text()==str){
	            var lux_hit=$(current);
	            elm.effect("highlight",{color:"#669966"},2000);
	            lux_hit.effect("highlight",{color:"#669966"},2000);
	        	$([document.documentElement, document.body]).animate({scrollTop: lux_hit.offset().top}, 2000);
	        	jumpTo(lux_hit);
	        }      
	    });
    }else if(elm.hasClass("key_lux")){
    	$(".key_ger").each(function(i, current){
	        var str=$(current).text();

	        if(elm.text()==str && $(current).hasClass("key_ger_lemma")){
	            var ger_hit=$(current);
	            elm.effect("highlight",{color:"#669966"});
	            ger_hit.effect("highlight",{color:"#669966"});
	        	$([document.documentElement, document.body]).animate({scrollTop: ger_hit.offset().top}, 2000);
	        	jumpTo(ger_hit);
	        }
	    });
    }
}

// Erstellt deutsche Tabelle
var tf = new TableFilter(
    document.querySelector('.table_ger',),
    {
        base_path: 'tablefilter/',
        start_with_operator: '←',
        paging: {
          length: 10
        },
        rows_counter: {
            text: 'Wörter: '
        },
        col_types: [
          'string'
        ],
        col_widths: [
            '100px','275px','290px'
        ],

        on_filters_loaded: function(tf) {
            tf.dom().rows[tf.getFiltersRowIndex()].style.display = 'none';
        },

        extensions: [{
            name: 'sort'
        }]
    }
);

// Erstellt luxemburgische Tabelle
var tf2 = new TableFilter(
    document.querySelector('.table_lux',),
    {
        base_path: 'tablefilter/',
        start_with_operator: '←',
        paging: {
          length: 10
        },
        rows_counter: {
            text: 'Wörter: '
        },
        col_types: [
          'string'
        ],
        col_widths: [
            '100px','275px','290px'
        ],

        on_filters_loaded: function(tf2) {
            tf2.dom().rows[tf2.getFiltersRowIndex()].style.display = 'none';
        },

        extensions: [{
            name: 'sort'
        }]
    }
);

// deutsche Tabellenfilterung anhand der alphabetischen Leiste 
function filter(evt){
    var elm = evt.target;
    var query = elm.value.length > 0 ? tf.stOperator + elm.value : '';
    tf.setFilterValue(0, query);
    tf.filter();
    }

// luxemburgischen Tabellenfilterung anhand der alphabetischen Leiste
function filter2(evt){
    var elm = evt.target;
    var query = elm.value.length > 0 ? tf.stOperator + elm.value : '';
    tf2.setFilterValue(0, query);
    tf2.filter();
}

// Iniitiert Tabellen
tf.init();
tf2.init();

// Filtert deutsche oder luxemburgische Tabelle bei einem passenden Wort
function jumpTo(target){
    var elm = target;
    var query = elm.text();

    if(elm.hasClass("key_lux")){
    	tf2.setFilterValue(0, query);
    	tf2.filter();
    	tf2.selectedLetter = elm;
	} else if(elm.hasClass("key_ger")){
		tf.setFilterValue(0, query);
    	tf.filter();
	}

}

