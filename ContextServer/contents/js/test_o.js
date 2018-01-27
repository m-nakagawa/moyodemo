var FOS = new Object();

/*
      ws = new WebSocket("ws://localhost:8000/openmasami/link");
      ws.onopen = function() {
         FOS.ws.send("Hello, world");
      };
      ws.onmessage = function (evt) {
         $("div#wb").text(evt.data);
         console.log(evt);
      };
*/

FOS.WebSocketCtrl = function (url,openfunc,recvfunc,closefunc,errorfunc) {
    var skt = null;
    open = function(){
	console.log("open:", url);
	if(skt == null){
	    skt = new WebSocket(url);
	    skt.onopen = onopen;
	    skt.onmessage = onmessage;
	    skt.onclose = onclose;
	    skt.onerror = onerror;
	}
    }

    onopen = function(evt){
	console.log("opened:", url);
	if(openfunc != null){
	    openfunc(evt);
	}
    }

    onmessage = function(evt){
	console.log(evt.data);
	recvfunc(evt.data);
    }

    onclose = function(evt){
	console.log("closed:", url);
	if(closefunc != null){
	    closefunc(evt);
	}
	skt = null;
	setTimeout(open(url), 2000);
    }

    onerror = function(evt){
	console.log("error", url);
	if(errorfunc != null){
	    errorfunc(evt);
	}
	setTimeout(open, 2000);
    }

    send = function(param) {
	if(skt != null){
	    skt.send(param);
	}
    }

    open();
    this.send = send;
}

/*
recvfunc = function (data) {
    $("div#wa").text(data);
    var d = JSON.parse(data);
    console.log("!!!",d["people_in_room_01"])
    $("div#wb").text(JSON.stringify(d));
}

openfunc = function (evt){
    ws.send('{"subscribe":"people_in_room_01"}');    
}

ws = new FOS.WebSocketCtrl("ws://localhost:8000/openmasami/link",
			   openfunc, recvfunc );

*/
//setTimeout(function(){ws.send("TEST");},3000);


