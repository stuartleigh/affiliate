window.Components = (function(Components){
	function request(B,A){this.bindFunction=function(E,D){return function(){return E.apply(D,[D])}};this.stateChange=function(D){if(this.request.readyState==4){this.callbackFunction(this.request)}};this.getRequest=function(){if(window.ActiveXObject){return new ActiveXObject("Microsoft.XMLHTTP")}else{if(window.XMLHttpRequest){return new XMLHttpRequest()}}return false};this.postBody=(arguments[2]||"");this.callbackFunction=A;this.url=B;this.request=this.getRequest();if(this.request){var C=this.request;C.onreadystatechange=this.bindFunction(this.stateChange,this);if(this.postBody!==""){C.open("POST",B,true);C.setRequestHeader("X-Requested-With","XMLHttpRequest");C.setRequestHeader("Content-type","application/x-www-form-urlencoded");}else{C.open("GET",B,true)}C.send(this.postBody)}};

	Components.infiniteScroll = function(url, success) {
		function checkForScroll() {
			if (loading) {return;}
			var body = document.body, html = document.documentElement;
			var height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
			var scrollHeight = window.scrollY + window.innerHeight;
			if (height * 0.9 <= scrollHeight) {
				loading = true;
				document.getElementById('scrollLoader').className = 'spinner'
				request(url + '?page=' + page, handleResponse);
				++page;
			}
		}

		function handleResponse(res) {
			document.getElementById('scrollLoader').className = ''
			if(res.status === 200) {
				success(res)
				loading = false;
			} else {
				clearInterval(scrollChecker);
			}
		}

		var loading = false, page = 2, scrollChecker = setInterval(checkForScroll, 500);
	}

	return Components

})(window.Components || {});

!function(){function g(g){g=g||window.event;for(var i,j,k,h=g.target||g.srcElement;h&&"a"!==h.nodeName.toLowerCase();)h=h.parentNode;h&&"a"===h.nodeName.toLowerCase()&&h.href&&(i=h.href.match(a),i&&(j=Math.round(f/2-c/2),k=0,e>d&&(k=Math.round(e/2-d/2)),window.open(h.href,"intent",b+",width="+c+",height="+d+",left="+j+",top="+k),g.returnValue=!1,g.preventDefault&&g.preventDefault()))}if(!window.__twitterIntentHandler){var a=/twitter\.com(\:\d{2,4})?\/intent\/(\w+)/,b="scrollbars=yes,resizable=yes,toolbar=no,location=yes",c=550,d=420,e=screen.height,f=screen.width;document.addEventListener?document.addEventListener("click",g,!1):document.attachEvent&&document.attachEvent("onclick",g),window.__twitterIntentHandler=!0}}();