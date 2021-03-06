// jquery.columnlist.js
// @weblinc, @jsantell (c) 2012

(function($){$.fn.columnlist=function(options){function returnColumn(inc){return $('<li class="'+options.incrementClass+inc+" "+options["class"]+'"></li>')}return options=$.extend({},$.fn.columnlist.defaults,options),this.each(function(){var $list=$(this),size=options.size||$list.data("columnList")||1,$children=$list.children("li"),perColumn=Math.ceil($children.length/size),$column;for(var i=0;i<size;i++){$column=$("<ul />").appendTo(returnColumn(i));for(var j=0;j<perColumn;j++)$children.length>i*perColumn+j&&$column.append($children[i*perColumn+j]);$list.append($column.parent())}})},$.fn.columnlist.defaults={"class":"column-list",incrementClass:"column-list-"}})(jQuery)
