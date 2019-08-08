

window.myCPP = window.myCPP || {};

    document.onkeyup = function(e) {
            if ( e.which   == 57) {
                //la touche 9
    goAvailable();
  } else if ( e.which  == 48) {
      //la touche 0
    goOffline();
  } else if (  e.which == 80){
    //la touche °
	Pause();
    }
    else if (  e.which == 79){
    //la touche +
	AfterCall();
}   else if (e.which == 81) {
      //la touche Q
    acceptContact();
  } else if ( e.which == 83) {
      //la touche S
    disconnectContact();
  } else if ( e.which == 67){
      //la touche C
	muteMic();	

} else if ( e.which == 86){
    //la touche V
        unmuteMic();
} else if ( e.which == 222){
    //la touche ²
	QuickConnect();
}else if ( e.which == 49){
    //la touche 1
	Transfert(0);
}
else if ( e.which == 50){
    //la touche 2
	Transfert(1);
}
else if ( e.which == 51){
    //la touche 3
	Transfert(2);
}
else if ( e.which == 52){
    //la touche 4
	Transfert(3);
}else if ( e.which == 65){
    //la touche 4
	CallEXT();
}



};


    //replace with the CCP URL for your Amazon Connect instance
//var ccpUrl = "https://gaetan-connect-allemagne.awsapps.com/connect/ccp#gaetan-allemagne/";
    var ccpUrl = "https://appelssortants.awsapps.com/connect/ccp#/";
    //var ccpUrl = "https://call-center-experteam.awsapps.com/connect/ccp#/"
    
    /*connect.core.initCCP(containerDiv, {
        ccpUrl: ccpUrl,        
        loginPopup: true,         
        softphone: {
            allowFramedSoftphone: true
        }
    });*/

    connect.contact(subscribeToContactEvents);
    connect.agent(subscribeToAgentEvents);


	function displayCaller(phoneNumber) {
		var listCaller = {
			"+19292240694": "Gaëtan",
			"+33642915377": "Didier",
			"+33668431756" : "Oussama"
		};
		if (phoneNumber in listCaller)
			var caller = listCaller[phoneNumber];
		else
			var caller = "Unknow";
		
        document.getElementById("infoCaller").innerHTML = "Appel entrant du " + phoneNumber + " " + caller;
        $(".elem-demo").notify(caller , "success" ) ;
		setTimeout(function (){
        document.getElementById("infoCaller").innerHTML = "";
        
		}, 8000);
	}

    function callPhone() {
        var myPhoneNumber = document.getElementById("myPhoneNumber").value;
        myPhoneNumber = myPhoneNumber;
        document.getElementById("infoPersonCalled").innerHTML = "Appel en cours vers " + myPhoneNumber;
		setTimeout(function (){
		document.getElementById("infoPersonCalled").innerHTML = "";
		}, 8000);
        var myEndPoint = connect.Endpoint.byPhoneNumber(myPhoneNumber);
        window.myCPP.agent.connect(myEndPoint, {
            success: function() {
                //alert('success');
            },
            failure: function() {
                //alert('error');
            }
        });
    }

    function callPhone2() {
        var e = document.getElementById("selectPhone");
		var selectedName = e.options[e.selectedIndex].text;
		var myPhoneNumber = e.options[e.selectedIndex].value;
	//	myPhoneNumber = "+33" + myPhoneNumber;
        document.getElementById("infoPersonCalled").innerHTML = "Appel en cours vers " + selectedName + "("+ myPhoneNumber + ")";
		setTimeout(function (){
		document.getElementById("infoPersonCalled").innerHTML = "";
		}, 8000);
        var myEndPoint = connect.Endpoint.byPhoneNumber(myPhoneNumber);
        window.myCPP.agent.connect(myEndPoint, {
            success: function() {
                //alert('success');
            },
            failure: function() {
                //alert('error');
            }
        });
    }


    function CallEXT() {
    var txt;
    var myPhoneNumber = prompt("Entrez le numéro de téléphone avec +33 :", "+33668431756");
        //txt = "0033668431756";
        //document.getElementById("demo").innerHTML = txt;
        document.getElementById("infoPersonCalled").innerHTML = "Appel en cours vers " + myPhoneNumber;
		setTimeout(function (){
		document.getElementById("infoPersonCalled").innerHTML = "";
		}, 8000);
    var myEndPoint = connect.Endpoint.byPhoneNumber(myPhoneNumber);
                window.myCPP.agent.connect(myEndPoint, {
                success: function() {
                       // alert('success');
                                    },
                    failure: function() {
                //alert('error');
            }
        });
    
        
  //console.log(txt + "message " + phone);
}


    function subscribeToContactEvents(contact) {
        window.myCPP.contact = contact;
        //logInfoMsg("Enregistrement des événements du contact");
        if (contact.getActiveInitialConnection()
            && contact.getActiveInitialConnection().getEndpoint()) {
            logInfoMsg("Un appel de : " + contact.getActiveInitialConnection().getEndpoint().phoneNumber);
            displayCaller(contact.getActiveInitialConnection().getEndpoint().phoneNumber);
            var Callers = contact.getActiveInitialConnection().getEndpoint().phoneNumber;
            //var phn = new displayCaller(contact.getActiveInitialConnection().getEndpoint().phoneNumber);
            //$.notify("Alert!", {align:"center", verticalAlign:"top"});
            //$(".elem-demo").notify("Hello Box");
        } else {
            logInfoMsg("This is an existing contact for this agent");
        }
        logInfoMsg("La file d'attente est " + contact.getQueue().name);
        //logInfoMsg("Contact attributes are " + JSON.stringify(contact.getAttributes()));
        contact.onIncoming(handleContactIncoming);
        contact.onAccepted(handleContactAccepted);
        contact.onConnected(handleContactConnected);
        contact.onEnded(handleContactEnded);
        $.notify(Callers, "success");
        $(".elem-demo").notify("Caller " + Callers , "success" ) ;
    }

    function handleContactIncoming(contact) {
        if (contact) {
            logInfoEvent("[contact.onIncoming] un appel entrant. status " + contact.getStatus().type);
        } else {
            logInfoEvent("[contact.onIncoming] un appel entrant de status Null");
        }
    }

    function handleContactAccepted(contact) {
        if (contact) {
            logInfoEvent("[contact.onAccepted] Le contact est accepté par l'agent. status " + contact.getStatus().type);
        } else {
            logInfoEvent("[contact.onAccepted] Le contact est accepté par l'agent. status null");
        }
    }

    function handleContactConnected(contact) {
        if (contact) {
            logInfoEvent("[contact.onConnected] Le contact est connecté à l'agent. status " + contact.getStatus().type);
        } else {
            logInfoEvent("[contact.onConnected] Le contact est connecté à l'agent. status null");
        }
    }

    function handleContactEnded(contact) {
        if (contact) {
            logInfoEvent("[contact.onEnded] Le contact est déconnecté à l'agent. status " + contact.getStatus().type);
        } else {
            logInfoEvent("[contact.onEnded] Le contact est déconnecté à l'agent. status null");
        }
    }

    function subscribeToAgentEvents(agent) {
        window.myCPP.agent = agent;
        agentGreetingDiv.innerHTML = '<h3>Bonjour  ' + agent.getName() + '!</h3>';
        //logInfoMsg("Enregistrement des événements de  " + agent.getName());
        //logInfoMsg("Le statut de " +  agent.getName() + agent.getStatus().name);
        displayAgentStatus(agent.getStatus().name);
        agent.onRefresh(handleAgentRefresh);
        agent.onRoutable(handleAgentRoutable);
        agent.onNotRoutable(handleAgentNotRoutable);
        agent.onOffline(handleAgentOffline);
    }

    function handleAgentRefresh(agent) {
        logInfoEvent("[agent.onRefresh] Agent data refreshed. Agent status is " + agent.getStatus().name);
        displayAgentStatus(agent.getStatus().name);
    }

    function handleAgentRoutable(agent) {
        logInfoEvent("[agent.onRoutable] Agent is routable. Agent status is " + agent.getStatus().name);
        displayAgentStatus(agent.getStatus().name);
    }

    function handleAgentNotRoutable(agent) {
        logInfoEvent("[agent.onNotRoutable] Agent is online, but not routable. Agent status is " + agent.getStatus().name);
        displayAgentStatus(agent.getStatus().name);
    }

    function handleAgentOffline(agent) {
        logInfoEvent("[agent.onOffline] Agent is offline. Agent status is " + agent.getStatus().name);
        displayAgentStatus(agent.getStatus().name);
    }

    function logMsgToScreen(msg) {
        logMsgs.innerHTML = '<div>' + new Date().toLocaleTimeString().fontcolor("green") + ' ' + msg.fontcolor("red") + '</div>' + logMsgs.innerHTML;
    }

    function logEventToScreen(msg) {
        eventMsgs.innerHTML = '<div>' + new Date().toLocaleTimeString().fontcolor("black") + ' ' + msg.fontcolor("blue") + '</div>' + eventMsgs.innerHTML;
    }

    function logInfoMsg(msg) {
        connect.getLog().info(msg);
        logMsgToScreen(msg);
    }

    function logInfoEvent(eventMsg) {
        connect.getLog().info(eventMsg);
        logEventToScreen(eventMsg);
    }

    function displayAgentStatus(status) {
        agentStatusDiv.innerHTML = 'Status: <span style="font-weight: bold">' + status + '</span>';
    }

    function goAvailable() {
        var routableState = window.myCPP.agent.getAgentStates().filter(function (state) {
            return state.type === connect.AgentStateType.ROUTABLE;
        })[0];
        window.myCPP.agent.setState(routableState, {
            success: function () {
                logInfoMsg("Set agent status to Available (routable) via Streams")
            },
            failure: function () {
                logInfoMsg("Failed to set agent status to Available (routable) via Streams")
            }
        });
    }
    function Pause() {
        
        var routableState = window.myCPP.agent.getAgentStates().filter(function (state) {
            return state.type === connect.AgentStateType.NOT_ROUTABLE;
        })[1];
        window.myCPP.agent.setState(routableState, {
            success: function () {
                logInfoMsg("L'agent est en Pause")
            },
            failure: function () {
                logInfoMsg("Erreur : Impossible de mettre le statut")
            }
        });
    }
    function AfterCall() {
        
        var routableState = window.myCPP.agent.getAgentStates().filter(function (state) {
            return state.type === connect.AgentStateType.NOT_ROUTABLE;
        })[0];
        window.myCPP.agent.setState(routableState, {
            success: function () {
                logInfoMsg("L'agent est en AfterCall")
            },
            failure: function () {
                logInfoMsg("Erreur : Impossible de mettre le statut ")
            }
        });
    }
    function goOffline() {
        var offlineState = window.myCPP.agent.getAgentStates().filter(function (state) {
            return state.type === connect.AgentStateType.OFFLINE;
        })[0];
        window.myCPP.agent.setState(offlineState, {
            success: function () {
                logInfoMsg("Set agent status to Offline via Streams")
            },
            failure: function () {
                logInfoMsg("Failed to set agent status to Offline via Streams")
            }
        });
    }

    function acceptContact() {
        window.myCPP.contact.accept({
            success: function () {
                logInfoMsg("Accepted contact via Streams");
            },
            failure: function () {
                logInfoMsg("Failed to accept contact via Streams");
            }
        });
    }

    function disconnectContact() {
        //cannot do contact.destroy(), can only destroy (hang-up) agent connection
        window.myCPP.contact.getAgentConnection().destroy({
            success: function () {
                logInfoMsg("Disconnected contact via Streams");
            },
            failure: function () {
                logInfoMsg("Failed to disconnect contact via Streams");
            }
        });
    }
function muteMic() {
        window.myCPP.agent.mute({
            success: function () {
                logInfoMsg("Accepted contact via Streams");
            },
            failure: function () {
                logInfoMsg("Failed to accept contact via Streams");
            }
        });
    }
function unmuteMic() {
        window.myCPP.agent.unmute({
            success: function () {
                logInfoMsg("Accepted contact via Streams");
            },
            failure: function () {
                logInfoMsg("Failed to accept contact via Streams");
            }
        });
    }

function ConfCall() {
	window.myCPP.conn.hold({
   		success: function() { logInfoMsg("Accepted Conference via Streams"); },
   		failure: function() { logInfoMsg("Failed Conference via Streams"); }
});
}



function holdcall() {
    var AgentID = myCPP.agent.getContacts()[0].contactId;
    var client = connect.core.getClient();
    client.call(connect.ClientMethods.HOLD_CONNECTION, {
         contactId:     AgentID,
         connectionId:  AgentID
      });
      $('.elem-demo').notify('En attente' ,'alert');
      alert(AgentID.name);


       
    }
function resumecall() {
    window.myCPP.contact.getAgentConnection().resume();
    $('.elem-demo').notify('Résumé' ,'success');
    alert('resume appelé');
    }


function CallTech(){
windows.myCPP.addConnection(endpoint, {
   success: function() {  },
   failure: function() {  }
});
}

function showAchievement (title, message) {
  $.notify({
    title: title,
    message: message + '.'
  }, {
    type: 'achievement',
    placement: {
      align: "left"
    },
    animate:{
      enter:'animated fadeInLeft',
      exit:'animated fadeOutRight'
    },
    delay: 5000
  });
}
var endpnt;
var Qq;
function QuickConnect(){
    var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "contents";
  } else {
    x.style.display = "none";
  }
var agent = new lily.Agent();
agent.getEndpoints(agent.getAllQueueARNs(), {
	success: function(data){ 
        console.log("valid_queue_phone_agent_endpoints", data.endpoints, "You can transfer the call to any of these endpoints");
        endpnt = data.endpoints;
	},
	failure:function(){
		console.log("failed")
	}
});
}
function Transfert(Qq){
var agent = new lily.Agent();
agent.getContacts(lily.ContactType.VOICE)[0].addConnection(endpnt[parseInt(Qq)], {
    success: function(data) {
       alert("transfer success");
    },
    failure: function(data) {
       alert("transfer failed");
    }
}); 

}


