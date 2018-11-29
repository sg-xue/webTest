window.onload=getTime;  //网页加载完就调用getTime()方法
function getTime(){
    var today=new Date();   //获取当前系统时间
    var hours=today.getHours();   //获取小时
    var minutes=today.getMinutes();  //获取分
    var seconds=today.getSeconds();  //获取秒
    if(minutes<10){     //分小于10就在前面补0
        minutes="0"+minutes;
    }
    if(seconds<10){  //秒小于10就在前面补0
        seconds="0"+seconds;
    }
    //把时分秒拼起来得到时间
    var time =hours+":"+minutes+":"+seconds;
	//把时间显示在div上,您自己可以放在网页任何位置,反正时间就是time
    document.getElementById("time").innerHTML="当前时间："+time;
      //每隔一秒更新一次时间
    setTimeout("getTime()",1000);
}