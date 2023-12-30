const btnCheckWeather=document.querySelector('.btn-check-weather')

const checkWeather=function(){
    window.location.href='/result'
}

btnCheckWeather.addEventListener('click',checkWeather)