$(function(){
   soldeUser=document.querySelector('#userSolde').innerHTML
   console.log(soldeUser)
   divTime=document.querySelector('.sectionHeure p strong').innerText.split(":");
   valIdMath=document.querySelector('#idMath').value
   myMin=parseInt(divTime[1]);
   myHeure=parseInt(divTime[0]);
   mySec=60;
   myCurrentTime=new Date()
   currentSec=myCurrentTime.getSeconds()
   currentMin=myCurrentTime.getMinutes()
   currentHeure=myCurrentTime.getHours()
   console.log("Heure "+currentHeure+"minute"+currentMin+"segonde"+currentSec)
   tempActuelEnSegonde=currentSec+currentMin*60+3600*currentHeure
   tempsMatheEnSegonde=mySec+myMin*60+3600*myHeure
   matchFini=false
   matchEnCour=false
   matchEntente=false

   tempChrono=tempsMatheEnSegonde-tempActuelEnSegonde
   chronoHeure=parseInt(tempChrono/3600)
   restChronoHeur=tempChrono%3600
   chronoMin=parseInt(restChronoHeur/60)
   chronoSegonde=restChronoHeur%60
   console.log(chronoHeure)
   console.log(chronoMin)
   console.log(chronoSegonde)
   console.log(myCurrentTime)
   document.querySelector('.mySec').innerHTML='<strong>'+chronoSegonde+'</strong>'
   document.querySelector('.myMin').innerHTML='<strong>'+chronoMin+'</strong>'
   document.querySelector('.myHeure').innerHTML='<strong>'+chronoHeure+'</strong>'


   if (isNaN(myMin) || isNaN(myHeure)){
      document.querySelector('.myChrono').innerHTML='<strong style="color: red">temps Nom Specifier </strong>';

   }
   else if(tempChrono>0){
      matchEntente=true
      document.querySelector('.myChrono').style.color='white'
      document.querySelector('.etatMath').innerHTML='<strong style="background: #0b51c5;padding: 10px">biento </strong>'
      setInterval(function () {
         chronoSegonde-=1
         document.querySelector('.mySec').innerHTML='<strong>'+chronoSegonde+'</strong>'
         if(chronoSegonde===1){
            chronoMin-=1
            chronoSegonde=60
            document.querySelector('.myMin').innerHTML='<strong>'+chronoMin+'</strong>'
         }
         if(chronoMin===1){
            chronoHeure-=1
            chronoMin=60
            document.querySelector('.myHeure').innerHTML='<strong>'+chronoHeure+'</strong>'
         }
      },1000)
   }
   else{
      // L'HEURE DU MATH EST ARRIVER
      tempChrono=-1*tempChrono
      matchEnCour=true
      if(tempChrono < 100*60){
      chronoHeure=parseInt(tempChrono/3600)
      restChronoHeur=tempChrono%3600
      chronoMin=parseInt(restChronoHeur/60)
      chronoSegonde=restChronoHeur%60
      document.querySelector('.mySec').innerHTML='<strong>'+chronoSegonde+'</strong>'
      document.querySelector('.myMin').innerHTML='<strong>'+chronoMin+'</strong>'
      document.querySelector('.myHeure').innerHTML='<strong>'+chronoHeure+'</strong>'


      document.querySelector('.myChrono').style.color='#168c80'
      document.querySelector('.etatMath').innerHTML='<strong style="background: #4cc543;padding:10px;">En cours  </strong>'

      setInterval(function (){
          // ON REDEMAR LE COMTEUR

               chronoSegonde+=1
            document.querySelector('.mySec').innerHTML='<strong>'+chronoSegonde+'</strong>'
            if(chronoSegonde===60){
               chronoMin+=1
               chronoSegonde=0
               document.querySelector('.myMin').innerHTML='<strong>'+chronoMin+'</strong>'
            }
            if(chronoMin===60){
               chronoHeure+=1
               chronoMin=0
               document.querySelector('.myHeure').innerHTML='<strong>'+chronoHeure+'</strong>'
            }

      },1000)

      }
      else{
         // #Le Math est terminer
         matchFini=true
      chronoHeure=parseInt(tempChrono/3600)
      restChronoHeur=tempChrono%3600
      chronoMin=parseInt(restChronoHeur/60)
      chronoSegonde=restChronoHeur%60
      document.querySelector('.mySec').innerHTML='<strong>'+chronoSegonde+'</strong>'
      document.querySelector('.myMin').innerHTML='<strong>'+chronoMin+'</strong>'
      document.querySelector('.myHeure').innerHTML='<strong>'+chronoHeure+'</strong>'


       document.querySelector('.myChrono').style.color='red'
       document.querySelector('.etatMath').innerHTML='<strong style="background: red;padding:10px;"> Termine </strong>'

      setInterval(function (){
          // ON REDEMAR LE COMTEUR

               chronoSegonde+=1
            document.querySelector('.mySec').innerHTML='<strong>'+chronoSegonde+'</strong>'
            if(chronoSegonde===60){
               chronoMin+=1
               chronoSegonde=0
               document.querySelector('.myMin').innerHTML='<strong>'+chronoMin+'</strong>'
            }
            if(chronoMin===60){
               chronoHeure+=1
               chronoMin=0
               document.querySelector('.myHeure').innerHTML='<strong>'+chronoHeure+'</strong>'
            }

      },1000)

      }
   }

   //REQUETTE POUR VALIDE UN TIKET SI LE MATH EST TERMINER
      if(matchFini){
         alert('Math termine')
         myParieBtn.addEventListener('click',function (e) {
            e.preventDefault()
            myErrorAlert("Desole le Mathe est termine")

         })

         $.ajax({
					url:"http://127.0.0.1:8000/",
					type:"POST",
					data:{idMatch:valIdMath},
					dataType:"json",
					success:function(data)
					{
                        console.log(data)
                        console.log("requete ok ")
					}
				})
      }
//
   // ENREGISTREMENT PARIE
      cote1=document.querySelector('#cote1').innerText
      cote1=cote1.replace(',','.')
      cote2=document.querySelector('#cote2').innerText
      cote2=cote2.replace(',','.')

      console.log(cote1)
      console.log(cote2)
      myParieBtn=document.querySelector('#submitParie')
      inputidVirtoir=document.querySelector("#idVirtoir")
      inputMise=document.querySelector("#mise")
      inputGainPotentiel=document.querySelector("#gainPotentiel")
      idMath=document.querySelector('#idMath')
      mise=inputMise.value
      gain=inputGainPotentiel.value

      inputMise.addEventListener('input',function (e) {
         idVirtoir=document.querySelector("#idVirtoir").value
         mise=document.querySelector("#mise").value
         gainPotentiel=document.querySelector("#gainPotentiel")
         console.log(mise)
         console.log(soldeUser)
         if(inputidVirtoir.value == 0){
            myErrorAlert("selectionne votre equipe")
            myParieBtn.disable=false

         }
         else if(isNaN(mise)){
            text='Saisir des chifres svp'
            myErrorAlert(text)
         }

         else if(soldeUser < mise){
            text="desole solde insufisant ;("
            myErrorAlert(text)
            myParieBtn.disable=false

         }
         else{
            if(inputidVirtoir.value == 1){
               gain=mise*parseFloat(cote1)

               inputGainPotentiel.value=gain
            }
            else{
               gain=mise*parseFloat(cote2)
               inputGainPotentiel.value=gain
            }
         }
      })
})

   function mySuccessAlert() {
      const Toast = Swal.mixin({
           toast: true,
           position: 'top-end',
           showConfirmButton: false,
           timer: 3000
         });

         Toast.fire({
           type: 'success',
           title: text
         })
   }

      function myErrorAlert(text) {
         const Toast = Swal.mixin({
           toast: true,
           position: 'top-end',
           showConfirmButton: false,
           timer: 3000
         });

         Toast.fire({
           type: 'error',
           title: text
         })

      }
      // myParieBtn.addEventListener('click',function (e) {
      //    e.preventDefault()
      //    idUser=document.querySelector('#idUser').value
      //    idVirtoir=document.querySelector("#idVirtoir").value
      //    mise=document.querySelector("#mise").value
      //    gainPotentiel=document.querySelector("#gainPotentiel").value
      //    idMath=document.querySelector('#idMath').value
      //    alert('idVictoire:  '+idVirtoir+'Mise  '+mise+' gainPotentiel  '+gainPotentiel+' idMath  '+idMath+'.')
      // $.ajax({
		// 			url:"http://127.0.0.1:8000/saveParie",
		// 			type:"Post",
		// 			data:{idVictoir:idVirtoir,mise:mise,gain:gainPotentiel,idMatch:idMath,idUser:idUser},
		// 			dataType:"json",
		// 			success:function(data)
		// 			{
      //
		// 			}
		// 		})
      // })

