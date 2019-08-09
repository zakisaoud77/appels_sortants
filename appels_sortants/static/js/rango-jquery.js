
/*$(document).ready(function() {
    $("#btndelete").click(function(){
        //alert("button");
          return confirm("Are you sure you want to delete?");
    }); 
});
*/

function ConfirmEdit() {
  return confirm("Do you want to confirm the changes ? ");
}


function ConfirmDelete() {
  return confirm("Are you sure you want to delete this element?");
}


function ConfirmDelete2() {
  return confirm("Etes-vous sûr(e) de vouloir supprimer tous les historiques?");
  
}



function select_all()  {
     window.alert("okok");
  }

$( "a.navbar-brand" ).hover(function() {
  $( this ).fadeOut( 100 );
  $( this ).fadeIn( 500 );
});


$(document).ready(function(){
  $("#bouton1").click(function(){
    //$("#bouton2").hide();
    $("#bouton2").fadeOut( 100 );
    console.log('Tab count \n');
     //console.log('Tab count \n');
  });
  });

// Pour afficher les 2 boutons (disponible, non disponible) 
// et pour enregistrer la date de l'appel




$(document).ready(function(){
$("#bouton_call").click(function(){


        //$("#bouton_raccroche").fadeIn("slow")

        var catid ;
        catid = $(this).attr("data-catid");

        $.ajax(
        {
         type:"GET",
         url: "/appel_started",
         data:{
                 contact_id: catid,
         },
         success: function( data ) 
         {  
            
            //$("#bouton_dis").fadeIn("slow");
            //$("#bouton_nondis").fadeIn("slow");
            //console.log(data);

         }

        })

        });
      });


 $(document).ready(function(){
 $("#bouton_raccroche").click(function(){

            
            //$(this).fadeOut("slow");
            $("#bouton_dis").fadeIn("slow");
            $("#bouton_nondis").fadeIn("slow");


            //$('#myModal3').modal('hide');
            //$('body').removeClass('modal-open');
            //$('.modal-backdrop').remove();



        });
      });


// si le client est intérésé ou non ? 
//( on doit sauvgarder ca dans lhistorique sans refraichir la page)

$(document).ready(function(){
    $("#btconfirm_interet").click(function(){

        var radioValue = $("input[name='drone']:checked").val();
        var catid = $(this).attr("data-catid");

        /*
        if(radioValue){
                alert("Your are a - " + radioValue);
            } */

        $.ajax(
        {

         type:"GET",
         url: "/appel_answered",
         data:{
                 contact_id: catid,
                 button_type : radioValue
         },

         success: function( data ) 
         {  

           var uri = window.location.toString();
           if (uri.indexOf("?") > 0) {
           var clean_uri = uri.substring(0, uri.indexOf("?"));
           window.history.replaceState({}, document.title, clean_uri); }
            
            window.location = "/";

            //window.location.href("/");
            //$("#bouton_suivant").click();

         }

        })

        });
  });



// Si le client était pas disponible ...
//( on doit sauvgarder ca dans lhistorique sans refraichir la page)


$(document).ready(function(){
$("#bt_next_date").click(function(){

        var catid ;
        catid = $(this).attr("data-catid");

        $.ajax(
        {
         type:"GET",
         url: "/appel_non_answered",
         data:{
                 contact_id: catid,
         },
         success: function( data ) 
         {  


            var uri = window.location.toString();
            if (uri.indexOf("?") > 0) {
            var clean_uri = uri.substring(0, uri.indexOf("?"));
            window.history.replaceState({}, document.title, clean_uri); }
            //alert(" Vous avez reporté l'appel avec le client " + catid);
            window.location = "/";
            //window.location.href("/");

         }

        })

        });
      });



/*
$(document).ready(function(){
$("#bouton_call2").click(function(){

        mobile = $(this).attr("data-catid2");

        var myPhoneNumber = mobile;
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


        });
      });

*/
