let resbtn=document.getElementById("btn")
let btns=document.getElementsByClassName("lbtn");



resbtn.onmouseenter=function(){
    resbtn.style.backgroundColor="purple";
    resbtn.style.borderColor="rgb(204, 137, 204)"
};
resbtn.onmouseleave=function(){
    resbtn.style.backgroundColor="rgb(204, 137, 204)";
    resbtn.style.borderColor="purple";
};


btns[0].onmouseenter=function(){
    btns[0].style.background = "url('static/github.gif')";
};

btns[0].onmouseleave=function(){
    btns[0].style.background = "url('static/github.png')";
};

btns[1].onmouseenter=function(){
    btns[1].style.background = "url('static/youtube.gif')";
};

btns[1].onmouseleave=function(){
    btns[1].style.background = "url('static/youtube.png')";
};

btns[2].onmouseenter=function(){
    btns[2].style.background = "url('static/insta.gif')";
};

btns[2].onmouseleave=function(){
    btns[2].style.background = "url('static/insta.png')";
};

btns[3].onmouseenter=function(){
    btns[3].style.background = "url('static/linkedin.gif')";
};

btns[3].onmouseleave=function(){
    btns[3].style.background = "url('static/linkedin.png')";
};
