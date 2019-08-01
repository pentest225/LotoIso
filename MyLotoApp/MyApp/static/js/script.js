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
})