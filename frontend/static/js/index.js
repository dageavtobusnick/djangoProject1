async function callClick() {
    let response = await fetch("../click/", {
        method: "GET",
        headers: {"X-Requested-With": "XMLHttpRequest"}
    });
    let answer = await response.json();
    if (answer.boosts)
        renderAllBoosts(answer.boosts)
    $("#coins").text('You have ' + answer['coinsCount'] + " coins");
}

async function getUser(id) {
    let response = await fetch("../users/" + id, {method: "GET"});
    let answer = await response.json();
    $("#user").text("Welcome, " + answer["username"]);
    let getCycle = await fetch("../cycles/" + answer['cycle'], {method: "GET"});
    let cycle = await getCycle.json();
    $('#coins').text('You have ' + cycle["coinsCount"] + " coins");
    $('#clickPower').text('Your click power is ' + cycle["clickPower"]);
    let getBoost = await fetch("../boosts/" + answer.cycle, {method: "GET"});
    let boosts=await getBoost.json();
    if (boosts)
        renderAllBoosts(boosts);
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
                return response.json();
            else {
                Promise.reject(response);
            }
        }).then(data =>{
            $('#coins').text('You have ' + data["coins_count"] + " coins");
            $('#clickPower').text('Your click power is ' + data["click_power"]);
            let nextPrice = parseInt(data['power']) + parseInt(data["click_power"]);
            $('#boostLevel_'+boostLevel).text("Level:"+boostLevel)
            $('#boostPower_'+boostLevel).text("NEXT CLICK POWER:"+nextPrice);
            $('#boostPrice_'+boostLevel).text("PRICE:"+data['price']);
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
function renderAllBoosts(boosts){
    $('#boost-wrapper').empty();
    boosts.forEach(boost=>{
        renderBoost(boost);
    })
}

function renderBoost(boost){
    totalPower=$('#clickPower').text().split(" ");
    nextPower=parseInt(boost['power'])+parseInt(totalPower[totalPower.length-1]);
    $(`<div class="upgrade">
            <input type="image" class="cat upgrade" src="/static/images/boost.png" onclick="buyBoost(${boost['level']})"/>
            <div class="boost-info">
                <p id="boostLevel_${boost['level']}" >${"Level:"+boost['level']}</p>
                <p id="boostPower_${boost['level']}" >${"NEXT CLICK POWER:"+nextPower}</p>
                <p id="boostPrice_${boost['level']}">${"PRICE:"+boost['price']}</p>
            </div>
        </div>`).appendTo($('#boost-wrapper'));
}
