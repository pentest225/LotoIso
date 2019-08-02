$(function(){
    setInterval(function(){
            $.ajax({
					url:"http://127.0.0.1:8000/scrap",
					type:"GET",
					data:{},
					dataType:"json",
					success:function(data)
					{
                        console.log(data)
					}
				})
        }, 60000);


    divTime=document.querySelectorAll('.sectionHeure p .heureDeMathe');
    for (i =0 ;i<divTime.length;i++){
    	chaineTemps=divTime[i].innerText.split(':')
    	myMin=parseInt(chaineTemps[1]);
   myHeure=parseInt(chaineTemps[0]);
   mySec=60;
   myCurrentTime=new Date()
   currentSec=myCurrentTime.getSeconds()
   currentMin=myCurrentTime.getMinutes()
   currentHeure=myCurrentTime.getHours()
   console.log("Heure "+currentHeure+"minute"+currentMin+"segonde"+currentSec)
   tempActuelEnSegonde=currentSec+currentMin*60+3600*currentHeure
   tempsMatheEnSegonde=mySec+myMin*60+3600*myHeure

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
	console.log(this)

   if (isNaN(myMin) || isNaN(myHeure)){
      document.querySelector('.myChrono').innerHTML='<strong style="color: red">temps Nom Specifier </strong>';

   }
   else{
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

	}


})