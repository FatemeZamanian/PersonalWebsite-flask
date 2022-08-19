let resbtn=document.getElementById("btn")
let btns=document.getElementsByClassName("mg");



resbtn.onmouseenter=function(){
    resbtn.style.backgroundColor="purple";
    resbtn.style.borderColor="rgb(204, 137, 204)"
};
resbtn.onmouseleave=function(){
    resbtn.style.backgroundColor="rgb(204, 137, 204)";
    resbtn.style.borderColor="purple";
};


btns[0].onmouseenter=function(){
    btns[0].src = "static/images/insta2.png";
};

btns[0].onmouseleave=function(){
    btns[0].src = "static/images/insta1.png";
};

btns[1].onmouseenter=function(){
    btns[1].style.background = "url('static/images/youtube.gif')";
};

btns[1].onmouseleave=function(){
    btns[1].style.background = "url('static/images/youtube.png')";
};

btns[2].onmouseenter=function(){
    btns[2].style.background = "url('static/images/insta.gif')";
};

btns[2].onmouseleave=function(){
    btns[2].style.background = "url('static/images/insta.png')";
};

btns[3].onmouseenter=function(){
    btns[3].style.background = "url('static/images/linkedin.gif')";
};

btns[3].onmouseleave=function(){
    btns[3].style.background = "url('static/images/linkedin.png')";
};
