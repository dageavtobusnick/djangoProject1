async function callClick() {
    let response = await fetch("../click/", {
        method: "GET",
        headers: {"X-Requested-With": "XMLHttpRequest"}
    });
    let answer = await response.json();
    $("#coins").text('You have ' + answer.toString() + " coins");
}

async function getUser(id) {
    let response = await fetch("../users/" + id, {method: "GET"})
    let answer = await response.json()
    $("#user").text("Welcome, " + answer["username"])
    let getCycle = await fetch("../cycles/" + answer['cycle'], {method: "GET"})
    let cycle = await getCycle.json()
    $('#coins').text('You have ' + cycle["coinsCount"] + " coins")
    $('#clickPower').text('Your click power is ' + cycle["clickPower"])
}

function buyBoost(boostLevel) {
    const csrftoken = getCookie("csrftoken");
    fetch("../buyBoost/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,

        },
        body: JSON.stringify({
            boost_level: boostLevel
        })
        }).then(response => {
            if (response.ok)
                return response.json()
            else {
                Promise.reject(response)
            }
        }).then(data =>{
            $('#coins').text('You have ' + data["coins_count"] + " coins")
            $('#clickPower').text('Your click power is ' + data["click_power"])
            $('#boostLevel').text("LEVEL:"+data['level'])
            $('#boostPrice').text("PRICE:"+data['price'])
    });
    }
function getCookie(name){
    let cookieValue=null;
    if(document.cookie && document.cookie!=''){
        const cookies=document.cookie.split(";");
        for (let i=0;i<cookies.length;i++){
            const cookie=cookies[i].trim();
            if(cookie.substring(0,name.length+1)===(name+'=')){
                cookieValue=decodeURIComponent(cookie.substring(name.length+1));
                break;
            }
        }
    }
    return cookieValue;
}


