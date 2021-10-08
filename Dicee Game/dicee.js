var num1=Math.random();
num1=num1*6;
num1=Math.floor(num1)+1;

var image1="dice"+num1+".png";
var path1="images/"+image1;

document.querySelector(".img1").setAttribute("src",path1)

var num2=Math.random();
num2=num2*6;
num2=Math.floor(num2)+1;

var image2="dice"+num2+".png";
var path2="images/"+image2;

document.querySelector(".img2").setAttribute("src",path2)

if(num1>num2)
{
    document.querySelector("h1").textContent="🚩 Player 1 wins!"
}
else if(num1<num2)
{
    document.querySelector("h1").textContent="Player 2 wins! 🚩"
}
else
{
    document.querySelector("h1").textContent="Draw!"
}