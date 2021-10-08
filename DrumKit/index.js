// document.querySelector("button").addEventListener("click",handleClick) //adds event listener to our first button only
//if we put parenthesis then it will not wait for the click to happen it will call automatically.

// function handleClick() //to detect mouse click
// {
    // alert("I got clicked");

    // this.style.color="white"; //changes the colour of clicked button to white. 
    //this keyword here refer to the object i.e. buuton here that we have selected using "querySelectorAll".
    
//     var buttonInnerHtml=this.innerHTML;
//     makeSound(buttonInnerHtml);
// }



//Detecting Button Press
var numberofButtons=document.querySelectorAll(".drum").length;

for(var i=0; i<numberofButtons ;i++)
{
    document.querySelectorAll(".drum")[i].addEventListener("click",function(){

        var buttonInnerHtml=this.innerHTML; //will give us the name of the button

        makeSound(buttonInnerHtml);

        buttonAnimation(buttonInnerHtml);

    });
}


//Detecting Keyboard press
document.addEventListener("keypress",function(event){ //this anonymous function  is called with event passed 
    // that triggered the keypress and that event contains a property called key which tells which keybd key was pressed.
    
    //The anonymous function here is also a Callback Function which is executed when and if "addEventListener" funcn is executed.
    makeSound(event.key);

    buttonAnimation(event.key);

});

//this basically means add the event listener "keypress" to the document and if key is pressed get it to call the
//respective anonymous function


//function that handles sound
function makeSound(key)
{
    switch(key)
    {
        case "w":
           var tom1 = new Audio('/DrumKit/sounds/tom-1.mp3')
           tom1.play(); 
           break;
        
        case "a":
           var tom2 = new Audio('/DrumKit/sounds/tom-2.mp3')
           tom2.play(); 
           break;
        
        case "s":
            var tom3 = new Audio('/DrumKit/sounds/tom-3.mp3')
            tom3.play(); 
            break;
        
        case "d":
            var tom4 = new Audio('/DrumKit/sounds/tom-4.mp3')
            tom4.play(); 
            break;
        
        case "j":
            var snare = new Audio('/DrumKit/sounds/snare.mp3')
            snare.play(); 
            break;

        case "k":
            var crash = new Audio('/DrumKit/sounds/crash.mp3')
            crash.play(); 
            break;

        case "l":
            var kick = new Audio('/DrumKit/sounds/kick-bass.mp3')
            kick.play(); 
            break;

        default:
            console.log(buttonInnerHtml);

    }
}

function buttonAnimation(currentKey){
    var activeButton=document.querySelector("."+currentKey); //we add "." as all currentKey s are classes so start with "."(dot)
    activeButton.classList.add("pressed"); //pressed is the class in css

    setTimeout(function(){
        activeButton.classList.remove("pressed");
    },100);
}
