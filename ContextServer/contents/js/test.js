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
    this.skt = null;
    this.url = url;
    this.openfunc = openfunc;
    this.recvfunc = recvfunc;
    console.log("xxx:", this.recvfunc);
    this.closefunc = closefunc;
    this.errorfunc = errorfunc;
    this.open();
}

FOS.WebSocketCtrl.prototype.open = function(){
    console.log("open:", this.url);
    if(this.skt == null){
	this.skt = new WebSocket(this.url);
	this.skt.onopen = this.onopen.bind(this);
	this.skt.onmessage = this.onmessage.bind(this);
	this.skt.onclose = this.onclose.bind(this);
	this.skt.onerror = this.onerror.bind(this);
    }
}

FOS.WebSocketCtrl.prototype.onopen = function(evt){
    console.log("opened:", this.url);
    if(this.openfunc != null){
	this.openfunc(evt);
    }
}

FOS.WebSocketCtrl.prototype.onmessage = function(evt){
    console.log(evt.data);
    console.log(this.url);
    if(this.recvfunc != null){
	this.recvfunc(evt.data);
    }
}

FOS.WebSocketCtrl.prototype.onclose = function(evt){
    console.log("closed:", this.url);
    if(this.closefunc != null){
	this.closefunc(evt);
    }
    this.skt = null;
    //setTimeout(function(url){open(url);}, 1000, ""+url);
    setTimeout(this.open.bind(this), 1000);
}

FOS.WebSocketCtrl.prototype.onerror = function(evt){
    console.log("error", this.url);
    if(this.errorfunc != null){
	this.errorfunc(evt);
    }
    //setTimeout(function(url){open(url);}, 2000, url);
}

FOS.WebSocketCtrl.prototype.send = function(param) {
    if(this.skt != null){
	this.skt.send(param);
    }
}

FOS.WebSocketCtrl.prototype.start = function(){
    this.open();
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


