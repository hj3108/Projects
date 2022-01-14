// Game Constants & Variables

let inputDir = {x:0 , y:0};
const foodSound = new Audio('music/food.mp3');
const gameOverSound = new Audio('music/gameover.mp3');
const moveSound = new Audio('music/move.mp3');
const musicSound = new Audio('music/music.mp3');
let speed=5;
let score=0;
let count=1;
let lastPaintTime=0;
let snakeArr = [
    {x: 13, y: 15}
];

// const goingUp = y === -1;
// const goingDown = y === 1;
// const goingRight = x === 1;  
// const goingLeft = x === -1;

food = {x: 6, y: 7}; 

//Game Functions
function main(ctime) //ctime--> current time 
{ 
    window.requestAnimationFrame(main); //will then become loop
    if((ctime - lastPaintTime)/1000 < 1/speed) // 1/speed basicaaly is a number i.e. after how much time you have to render the screen
    {
        return;
    }
    lastPaintTime = ctime;
    gameEngine();
}

function isCollide(sarr) //sarr --> is snake array only i.e. snakeArr
{
    //if you bump into yourself
    for(let i=1 ; i<sarr.length; i++)
    {
        if(sarr[i].x === sarr[0].x && sarr[i].y === sarr[0].y)
        {
            return true;
        }
    }

    //if you collide to wall
    if(sarr[0].x >= 18 || sarr[0].x <=0 || sarr[0].y >= 18 || sarr[0].y <=0){
        return true;
    }
}

function gameEngine()
{
    
    //Part 1 :- Updating the snake array
    if(isCollide(snakeArr))
    {
        gameOverSound.play();
        musicSound.pause();
        inputDir = {x:0 , y:0};
        alert("Game Over. Press any key to play again!");
        snakeArr = [{x: 13, y: 15}]; //Resetting snake Arr
        musicSound.play();
        score = 0;
        speed=5;
        scoreBox.innerHTML= "Score: "+score;
    }

    // If you have eaten the food, increment the score and regenerate the food
    if(count%5!==0)
    {
        if(snakeArr[0].y===food.y && snakeArr[0].x===food.x) //i.e. we snake head i.e 0th element of snake array overlaps food object that means snake have eaten the food
        {
            foodSound.play();
            score+=1;
            speed+=0.5; //increasing speed every time when snake has eaten the food
            if(score>hiscoreval){
                hiscoreval = score;
                localStorage.setItem("hiscore", JSON.stringify(hiscoreval));
                hiscoreBox.innerHTML = "High Score: " + hiscoreval;
            }
            scoreBox.innerHTML= "Score: "+score;
            snakeArr.unshift({x: snakeArr[0].x + inputDir.x, y: snakeArr[0].y + inputDir.y}); //will add one more segment to the snake i.e. snake length will increase
            let a = 1;
            let b = 17;
            food = {x: Math.round(a + (b-a)* Math.random()), y: Math.round(a + (b-a)* Math.random())};
            count++;
        }
    }
    else
    {
        if(snakeArr[0].y===food.y && snakeArr[0].x===food.x) 
        {
            
            foodSound.play();
            score+=2;
            speed+=0.7; //increasing speed every time when snake has eaten the food
            if(score>hiscoreval){
                hiscoreval = score;
                localStorage.setItem("hiscore", JSON.stringify(hiscoreval));
                hiscoreBox.innerHTML = "High Score: " + hiscoreval;
            }
            scoreBox.innerHTML= "Score: "+score;
            snakeArr.unshift({x: snakeArr[0].x + inputDir.x, y: snakeArr[0].y + inputDir.y}); //will add one more segment to the snake i.e. snake length will increase
            let a = 1;
            let b = 17;
            food = {x: Math.round(a + (b-a)* Math.random()), y: Math.round(a + (b-a)* Math.random())};
            count++;
            
        }
    }
    

    //Moving the snake (i.e. to update x and y co-ordinates)
    for (let i = snakeArr.length - 2; i>=0; i--) { 
        snakeArr[i+1] = {...snakeArr[i]}; //Adding a new object basically at last 
    }

    snakeArr[0].x += inputDir.x;
    snakeArr[0].y += inputDir.y;

    //Part 2 :- 
    // Display the snake 
    board.innerHTML = "";
    snakeArr.forEach(function(e,index)
    {
        snakeElement=document.createElement('div');
        snakeElement.style.gridRowStart=e.y;
        snakeElement.style.gridColumnStart=e.x;
        if(index===0)
        {
            snakeElement.classList.add('head');
        }
        else
        {
            snakeElement.classList.add('snake');
        }
        board.appendChild(snakeElement);
    });

    // Display the food
    if(count%5!=0)
    {
        foodElement=document.createElement('div');
        foodElement.style.gridRowStart=food.y;
        foodElement.style.gridColumnStart=food.x;
        foodElement.classList.add('food');
        board.appendChild(foodElement);

    }
    else
    {
        foodElement=document.createElement('div');
        foodElement.style.gridRowStart=food.y;
        foodElement.style.gridColumnStart=food.x;
        foodElement.classList.add('superfood');
        board.appendChild(foodElement);
    }
}



//Main Logic starts here
musicSound.play();
let hiscore = localStorage.getItem("hiscore");
if(hiscore === null){
    hiscoreval = 0;
    localStorage.setItem("hiscore", JSON.stringify(hiscoreval))
}
else{
    hiscoreval = JSON.parse(hiscore);
    hiscoreBox.innerHTML = "High Score: " + hiscore;
}

window.requestAnimationFrame(main); // This will used to initiate
window.addEventListener('keydown',function(e)
{
    inputDir = {x:0 , y:1} //start the game //this is basically snake velocity
    moveSound.play();
    switch(e.key)
    {
        case "ArrowUp" :
            inputDir.x= 0;
            inputDir.y= -1;
            break;

        case "ArrowDown" :
            inputDir.x= 0;
            inputDir.y= 1;
            break;

        case "ArrowLeft" :
            inputDir.x= -1;
            inputDir.y= 0;
            break;

        case "ArrowRight" :
            inputDir.x= 1;
            inputDir.y= 0;
            break;

        default:
            break;
    }
});