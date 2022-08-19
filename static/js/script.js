let resbtn=document.getElementById("btn");
let btns=document.getElementsByClassName("mg");

btns[0].onmouseenter=function(){
    btns[0].src = "static/images/insta2.png";
};

btns[0].onmouseleave=function(){
    btns[0].src = "static/images/insta1.png";
};

btns[1].onmouseenter=function(){
    btns[1].src = "static/images/git2.png";
};

btns[1].onmouseleave=function(){
    btns[1].src = "static/images/git1.png";
};

btns[2].onmouseenter=function(){
    btns[2].src = "static/images/linkedin2.png";
};

btns[2].onmouseleave=function(){
    btns[2].src = "static/images/linkedin1.png";
};

btns[3].onmouseenter=function(){
    btns[3].src = "static/images/yout2.png";
};

btns[3].onmouseleave=function(){
    btns[3].src = "static/images/yout1.png";
};

resbtn.onmouseenter=function(){
    resbtn.style.backgroundColor="purple";
    resbtn.style.borderColor="rgb(204, 137, 204)"
};
resbtn.onmouseleave=function(){
    resbtn.style.backgroundColor="rgb(204, 137, 204)";
    resbtn.style.borderColor="purple";
};
