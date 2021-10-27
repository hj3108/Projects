var buttonColours = ["red", "blue", "green", "yellow"];
var gamePattern=[];
var userClickedPattern=[];
var started=false;
var level=0;

$("body").keypress(function()
{
    if(!started)
    {
        $("#level-title").text("Level "+level);
        nextSequence();
        started=true;
    }
});

function checkAnswer(currentLevel)
{
    if(gamePattern[currentLevel]===userClickedPattern[currentLevel])
    {
        if(gamePattern.length===userClickedPattern.length)
        {
            setTimeout(function()
            {
                nextSequence();
            },1000);
        }
    }
    else
    {
        playSound("wrong");
        $("body").addClass("game-over");
        $("#level-title").text("Game Over, Press Any Key to Restart");

        setTimeout(function()
        {
            $("body").removeClass("game-over");
        },200);

        startOver();

    }
}

function playSound(name)
{
    var audio = new Audio("/sounds/" + name + ".mp3");
    audio.muted=false;
    audio.play();
}

function animatePress(currentColour)
{
    $("."+currentColour).click(function()
    {
        $("."+currentColour).addClass("pressed");
    });

    setTimeout(function()
    {
        $("."+currentColour).removeClass("pressed");
    },100);
}

$(".btn").click(function()
{
    if(started)
    {
        var userChosenColour=$(this).attr("id");
        userClickedPattern.push(userChosenColour);
        animatePress(userChosenColour);
        playSound(userChosenColour);
        checkAnswer(userClickedPattern.length-1);
    }
});

function nextSequence()
{
    
    userClickedPattern=[];
    level++;
    $("#level-title").text("Level "+level);

    var num=Math.random()*4;
    var randomnum=Math.floor(num);
    var randomChosenColour=buttonColours[randomnum];
    gamePattern.push(randomChosenColour);

    $("#"+randomChosenColour).fadeIn(100).fadeOut(100).fadeIn(100);

    playSound(randomChosenColour);

}

function startOver()
{
    level=0;
    gamePattern=[];
    started=false;
}

// -------------------------------------------------------------------------------------------------------------------------

// Checking Page Inactivity

let inactivityTime = function() {
    let time;
    window.onload = resetTimer;
    document.onmousemove = resetTimer;
    document.onkeypress = resetTimer;
    document.click=resetTimer;

    function logout() {
        playSound("wrong");
        $("body").addClass("game-over");
        $("#level-title").text("Time Limit Exceeded");
        
        startOver();
        resetTimer();

        setTimeout((function() {  
            window.location.reload();
        }), 3000);
        
    }

    function resetTimer() {
      clearTimeout(time);
      time = setTimeout(logout, 3000);
    }
};

window.onload = function() {
    inactivityTime();
}

// -------------------------------------------------------------------------------------------------------------------------

//Stop Watch Functionality

function timeToString(time) {
    let diffInHrs = time / 3600000;
    let hh = Math.floor(diffInHrs);
  
    let diffInMin = (diffInHrs - hh) * 60;
    let mm = Math.floor(diffInMin);
  
    let diffInSec = (diffInMin - mm) * 60;
    let ss = Math.floor(diffInSec);
  
    let diffInMs = (diffInSec - ss) * 100;
    let ms = Math.floor(diffInMs);
  
    let formattedMM = mm.toString().padStart(2, "0");
    let formattedSS = ss.toString().padStart(2, "0");
    let formattedMS = ms.toString().padStart(2, "0");
  
    return `${formattedMM}:${formattedSS}:${formattedMS}`;
}

let startTime;
let elapsedTime = 0;
let timerInterval;

// Create function to modify innerHTML

function print(txt) {
  document.getElementById("display").innerHTML = txt;
}

// Create "start", "pause" and "reset" functions

function start() {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(function printTime() {
    elapsedTime = Date.now() - startTime;
    print(timeToString(elapsedTime));
  }, 10);
}


function reset() {
  clearInterval(timerInterval);
  print("00:00:00");
  elapsedTime = 0;
}

$("body").keypress(function()
{
    start();
})
