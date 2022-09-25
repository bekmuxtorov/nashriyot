var videPlayer=document.getElementById("videoPlayer");
var myVideo = document.getElementById("myVideo");

function stopVideo(){
    videPlayer.style.display="none";
    
}
function playVideo(file){
    myVideo.src=file;
    videPlayer.style.display="block";
}