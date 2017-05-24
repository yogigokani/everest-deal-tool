$(document).ready(function(){
    var projects = [
        {
            showString: "yogi",
            hiddenString: "SM",
            url: "url"
        },
        {
            showString: "motu",
            hiddenString: "SM1",
            url: "url1"
        },
        {
            showString: "chotu",
            hiddenString: "SM2",
            url: "url2"
        }
    ];

    $("#tags").autocomplete({

        source: function(request, response){

            var matcher = new RegExp( $.ui.autocomplete.escapeRegex( request.term ), "i" );

            response( $.grep( projects, function( value ) {

                // mention the fields to be searched in
                return matcher.test(value.showString) || matcher.test(value.hiddenString) || matcher.test(value.url);

            }));
        }

    });

    // overridden renderItem of Jquery - autocomplete feature
    $.ui.autocomplete.prototype._renderItem = function (ul, item) {

        var createA = document.createElement('a');
        var createAText = document.createTextNode(item.showString);
        createA.setAttribute('href', item.url);
        createA.appendChild(createAText);

        return $( "<li>" )
            .append( createA )
            .appendTo( ul );
    };

});
