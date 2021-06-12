async function callClick() {
    let coinsPrase = $("#coins").text().split(' ');
    let coins = parseInt(coinsPrase[2])
    let powerPhrase = $('#clickPower').text().split(" ");
    let power = parseInt(powerPhrase[powerPhrase.length - 1]);
    let coinsCount = coins + power;
    $("#coins").text('You have ' + coinsCount + " coins");
}

function setAutoClick() {
    setInterval(function () {
        let coinsPrase = $("#coins").text().split(' ');
        let coins = parseInt(coinsPrase[2])
        let powerPhrase = $('#autoClickPower').text().split(" ");
        let power = parseInt(powerPhrase[powerPhrase.length - 1]);
        let coinsCount = coins + power;
        $("#coins").text('You have ' + coinsCount + " coins");
    }, 1000)
}

function setSendCoinsInterval() {
    setInterval(function () {
        const csrftoken = getCookie("csrftoken");
        let coinsPrase = $("#coins").text().split(' ');
        const coinsCounter = parseInt(coinsPrase[2])
        fetch('../set_main_cycle/', {
            method: 'POST',
            headers: {
                "X-CSRFToken": csrftoken,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    coinsCount: coinsCounter,
                }
            )
        }).then(response => {
            if (response.ok) {
                return response.json();
            } else {
                return Promise.reject(response);
            }
        }).then(data => {
            console.log("Coins sent to server");
            console.log(data);
            if (data.boosts)
                renderAllBoosts(data.boosts);
            checkBoosts(true);
        })
    }, 2500)
}

async function getUser(id) {
    let response = await fetch("../users/" + id, {method: "GET"});
    let answer = await response.json();
    $("#user").text("Welcome, " + answer.username);
    let getCycle = await fetch("../cycles/" + answer.cycle, {method: "GET"});
    let cycle = await getCycle.json();
    $('#coins').text('You have ' + cycle.coinsCount + " coins");
    $('#clickPower').text('Your click power is ' + cycle.clickPower);
    $('#autoClickPower').text('Your auto-click power is ' + cycle.autoClickPower);
    let getBoost = await fetch("../boosts/" + answer.cycle, {method: "GET"});
    let boosts = await getBoost.json();
    if (boosts)
        renderAllBoosts(boosts);
    checkBoosts(true)
    setAutoClick()
    setSendCoinsInterval()
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
    }).then(data => {
        $('#coins').text('You have ' + data.coins_count + " coins");
        $('#clickPower').text('Your click power is ' + data.click_power);
        $('#autoClickPower').text('Your auto-click power is ' + data.auto_click_power);
        let nextPrice = parseInt(data.power) + parseInt(data.click_power);
        $(`boost-info_${boostLevel} .boost_level`).text("Level:" + boostLevel)
        $(`boost-info_${boostLevel} .boost_power`).text("NEXT CLICK POWER:" + nextPrice);
        $(`boost-info_${boostLevel} .boost_price`).text("PRICE:" + data.price);
        checkBoosts(false)
    });
    checkBoosts(false)
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function renderAllBoosts(boosts) {
    $('#boost-wrapper').empty();
    boosts.forEach(boost => {
        renderBoost(boost);
    })
}

function checkBoosts(allowUnlock) {
    coinsPrase = $("#coins").text().split(' ');
    coins = parseInt(coinsPrase[2])
    $("div.upgrade").toArray().forEach(div => {
        checkBoost(div, coins, allowUnlock)
    });
}

function checkBoost(div, coins, allowUnlock) {
    let pricePhrase = div.querySelector(".boost_price").innerHTML.split(':');
    const price = parseInt(pricePhrase[1]);
    if (price > coins) {
        let btn = div.querySelector('input');
        div.removeAttribute('class');
        div.setAttribute('class', 'upgrade inactive');
        btn.setAttribute('disabled', 'true');
    } else {
        if (allowUnlock) {
            let btn = div.querySelector('input');
            div.removeAttribute('class');
            div.setAttribute('class', 'upgrade');
            btn.removeAttribute('disabled');
        }
    }
}

function renderBoost(boost) {
    let totalPower = $('#clickPower').text().split(" ");
    let boost_img = $('#boost-png').attr('value');
    let auto_boost_img = $('#auto-boost-png').attr('value');
    let nextPower = parseInt(boost['power']) + parseInt(totalPower[totalPower.length - 1]);
    $(`<li>
            <div class="upgrade">
            <input type="image" class="cat upgrade" src="${boost.boostType == 1 ? boost_img : auto_boost_img}" onclick="buyBoost(${boost.level})"/>
            <div id="boost-info_${boost.level}" class="boost-info">
                <p class="boost_level" >${"Level:" + boost.level}</p>
                <br/>
                <p class="boost_power">${"NEXT " + (boost.boostType == 1 ? " " : "AUTO-") + "CLICK POWER:" + nextPower}</p>
                <br/>
                <p class="boost_price">${"PRICE:" + boost.price}</p>
            </div>
            </div>
        </li>`).appendTo($('#boost-wrapper'));
}
