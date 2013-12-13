book description
<ul>
<li>name</li>
<li>{{map['desc']['name']}}</li>

<li>type</li>
<li>{{map['desc']['type']}}</li>

<li>author</li>
<li>{{map['desc']['author']}}</li>

<li>sections</li>
<li>{{map['desc']['sections']}}</li>

<li>desc</li>
<li>{{map['desc']['desc']}}</li>

<li>cover</li>
<li><img src={{map['desc']['cover']}}></li>
</ul>


<!-- <a href="/book/{{map['desc']['id']}}/page/">show sections:</a> -->

<script src="http://libs.baidu.com/jquery/1.9.0/jquery.js"></script>
<br>

<div class="sounds">
</div>
<a id="next" href="#">append sound</a>

<br>
totalCount: {{map['desc']['sections']}}
<script>
var i=1;
var total = {{map['desc']['sections']}};
$("#next").bind("click", function() {
    //alert( "User clicked on 'foo.'" );
    i++;
    if(i*50 < parseInt(total)){
        getpage(i)
    }
});

function getpage(page){
    var lanrenAPI = "/book/{{map['desc']['id']}}/page/"+page;
    $.getJSON( lanrenAPI, {
     }).done(function(data) {
     console.log(data)
     $.each(data.list, function(i, item){
         $(".sounds").append($("<p><a href="+ item.path+">"+item.name+"</p>"))
         });
     });
}

(function() {
 var lanrenAPI = "/book/{{map['desc']['id']}}/page/1";
 $.getJSON( lanrenAPI, {
     // tags: "mount rainier",
     // tagmode: "any",
     // format: "json"
     })
 .done(function(data) {
     console.log(data)
     $.each(data.list, function(i, item){
         $(".sounds").append($("<p><a href="+ item.path+">"+item.name+"</p>"))
         });
     //$.each( data.items, function( i, item ) {
     //   $( "<img>" ).attr( "src", item.media.m ).appendTo( "#images" );
     //   if ( i === 3 ) {
     //    return false;
     //   }
     //  });
     });
 })();

</script>


