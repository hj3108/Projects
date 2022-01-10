let music= new Audio("music.mp3");
let audioTurn= new Audio("ting.mp3");
let gameover= new Audio("gameover.mp3");
let isgameover=false;

let turn ="X";

//Function to change the turn
function changeTurn()
{
    if(turn==="X")
    {
        return "0";
    }
    else
    {
        return "X";
    }
}

//Function to check for a Win
function checkWin()
{
    let boxtext = document.getElementsByClassName('boxtext');
    let wins = [
        [0, 1, 2, -12, 5, 0],
        [3, 4, 5, -12, 15, 0],
        [6, 7, 8, -12, 25, 0],
        [0, 3, 6, -22.5, 15, 90],
        [1, 4, 7, -12.5, 15, 90],
        [2, 5, 8, -2.5, 15, 90],
        [0, 4, 8, -12.5, 15, 45],
        [2, 4, 6, -12.5, 15, 135],
    ]

    wins.forEach(function(e)
    {
        if((boxtext[e[0]].innerText===boxtext[e[1]].innerText) && (boxtext[e[1]].innerText===boxtext[e[2]].innerText) && boxtext[e[0]].innerText!=="")
        {
            document.querySelector(".info").innerText= boxtext[e[0]].innerText+" Won"
            isgameover=true;
            document.querySelector(".imgbox").getElementsByTagName("img")[0].style.width="200px";
            document.querySelector(".line").style.transform = `translate(${e[3]}vw, ${e[4]}vw) rotate(${e[5]}deg)`;
            document.querySelector(".line").style.width="20vw";
        }
    });
}

//Game Logic
let boxes= document.getElementsByClassName("box");
Array.from(boxes).forEach(element =>{
    let boxtext=element.querySelector(".boxtext");
    element.addEventListener("click", function()
    {
        // console.log(boxtext.innerText);
        if(boxtext.innerText==="")
        {
            boxtext.innerText=turn;
            turn=changeTurn();
            audioTurn.play();
            checkWin();
            if(!isgameover)
            {
                document.getElementsByClassName("info")[0].innerText = "Turn for "+turn;
            }
            
        }
    })
});

//Adding onclick listener to rest button
reset.addEventListener("click",function()
{
    let boxtexts=document.querySelectorAll(".boxtext");
    Array.from(boxtexts).forEach(element => {
        element.innerText = "";
    });
    turn="X";
    isgameover=false;
    document.querySelector(".line").style.width="0vw";
    document.getElementsByClassName("info")[0].innerText = "Turn for "+turn;
    document.querySelector(".imgbox").getElementsByTagName("img")[0].style.width="0px";


});
