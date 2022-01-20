const weatherApi = {
    key: "0b9c939f3bbc4e0e53e13a3d6410e717",
    baseUrl: "https://api.openweathermap.org/data/2.5/weather",
};



// api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

const searchInputBox = document.getElementById('input-box');
searchInputBox.addEventListener('keypress',function(event)
{
    if(event.keyCode == 13) {
        // console.log(searchInputBox.value);
        getWeatherReport(searchInputBox.value);
        document.querySelector('.weather-body').style.display = "block";
    }
});

//Get weather Report
function getWeatherReport(city)
{
    fetch(`${weatherApi.baseUrl}?q=${city}&appid=${weatherApi.key}&units=metric`)
    .then(function(weather)
    {
        return weather.json();
    }).then(showWeatherReport);
}

function showWeatherReport(weather)
{
    // console.log(weather);

    let city=document.getElementById('city');
    city.innerText= `${weather.name}, ${weather.sys.country}`;

    let temperature = document.getElementById('temp');
    temperature.innerHTML = `${Math.round(weather.main.temp)}&deg;C`;

    let minMaxTemp = document.getElementById('min-max');
    minMaxTemp.innerHTML = `${Math.floor(weather.main.temp_min)}&deg;C (min)/ ${Math.ceil(weather.main.temp_max)}&deg;C (max) `;

    let weatherType = document.getElementById('weather');
    weatherType.innerText = `${weather.weather[0].main}`;

    let date = document.getElementById('date');
    let todayDate = new Date();
    date.innerText = dateManage(todayDate);

    
    if(weatherType.textContent == 'Clear') {
        document.body.style.backgroundImage = "url('images/clear.jpg')";
        document.querySelector("#img1").src = "small_images/clear.svg";
        
    } else if(weatherType.textContent == 'Clouds') {

        document.body.style.backgroundImage = "url('images/cloud.jpg')";
        document.querySelector("#img1").src = "small_images/cloud.svg";
        
        
    } else if(weatherType.textContent == 'Haze') {

        document.body.style.backgroundImage = "url('images/cloud.jpg')";
        document.querySelector("#img1").src = "small_images/haze.svg";
        
    }     else if(weatherType.textContent == 'Rain') {
        
        document.body.style.backgroundImage = "url('images/rain.jpg')";
        document.querySelector("#img1").src = "small_images/rain.svg";
        
    } else if(weatherType.textContent == 'Snow') {
        
        document.body.style.backgroundImage = "url('images/snow.jpg')";
        document.querySelector("#img1").src = "small_images/snow.svg";
    
    } else if(weatherType.textContent == 'Thunderstorm') {
    
        document.body.style.backgroundImage = "url('images/thunderstorm.jpg')";
        document.querySelector("#img1").src = "small_images/storm.svg";
        
    } else if(weatherType.textContent == 'Fog') {
    
        document.body.style.backgroundImage = "url('images/fog.jpg')";
        document.querySelector("#img1").src = "small_images/fog.png";
        
    }
}

// Date manage
function dateManage(dateArg) {

    let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    let year = dateArg.getFullYear();
    let month = months[dateArg.getMonth()];
    let date = dateArg.getDate();
    let day = days[dateArg.getDay()];

    return `${date} ${month} (${day}), ${year}`;
}
