!function(e){e.fn.countTo=function(t){return t=t||{},e(this).each(function(){var n=e.extend({},e.fn.countTo.defaults,{from:e(this).data("from"),to:e(this).data("to"),speed:e(this).data("speed"),refreshInterval:e(this).data("refresh-interval"),decimals:e(this).data("decimals")},t),o=Math.ceil(n.speed/n.refreshInterval),a=(n.to-n.from)/o,i=this,l=e(this),r=0,c=n.from,s=l.data("countTo")||{};function f(e){var t=n.formatter.call(i,e,n);l.html(t)}l.data("countTo",s),s.interval&&clearInterval(s.interval),s.interval=setInterval(function(){r++,f(c+=a),"function"==typeof n.onUpdate&&n.onUpdate.call(i,c);r>=o&&(l.removeData("countTo"),clearInterval(s.interval),c=n.to,"function"==typeof n.onComplete&&n.onComplete.call(i,c))},n.refreshInterval),f(c)})},e.fn.countTo.defaults={from:0,to:0,speed:1e3,refreshInterval:100,decimals:0,formatter:function(e,t){return e.toFixed(t.decimals)},onUpdate:null,onComplete:null}}(jQuery),jQuery(function(e){e(".count-number").data("countToOptions",{formatter:function(e,t){return e.toFixed(t.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g,",")}}),e(".timer").each(function(t){var n=e(this);t=e.extend({},t||{},n.data("countToOptions")||{}),n.countTo(t)})}),$(document).ready(function(){$(".bell").click(function(){$(this).next().slideToggle(200),icon=$(this).find("i"),icon.toggleClass("far fa-bell far fa-bell-slash")})}),$(document).ready(function(){$(".jobs_progress_info_first").hide(),$(".agle_down").click(function(){$(this).next().slideToggle(200),icon=$(this).find("i"),icon.toggleClass("fa fa-angle-down fa fa-angle-up")})}),$(document).ready(function(){$(".header-user-menu-down").hide(),$(".header-user-menu").click(function(){$(".header-user-menu-down").toggle(200)})}),$("#hamburger").click(function(){$(this).toggleClass("animate"),$(".nav_left").toggleClass("active"),$(".nav_left_profile").toggleClass("active")});function vatCalculation(){var t=document.getElementById("subtotal").value,e=parseFloat(parseFloat(t)*parseFloat(.2)).toFixed(2),a=parseFloat(parseFloat(t)-parseFloat(e)).toFixed(2);document.getElementById("subtotal").value=parseFloat(t).toFixed(2),document.getElementById("vat").value=e,document.getElementById("total").value=a}








    function check(){
        document.getElementById("checkbox").checked = true;
    }

    function uncheck(){
        document.getElementById("checkbox").checked = false;
    }




