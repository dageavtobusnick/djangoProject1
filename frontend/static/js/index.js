async function callClick() {
    let response = await fetch("../click/", {
        method: "GET",
        headers: {"X-Requested-With": "XMLHttpRequest"}
    });
    let answer = await response.json();
    $("#coins").text('You have '+answer.toString()+" coins");
}

async function getUser(id){
    let response=await fetch("../users/"+id,{method:"GET"})
    let answer=await response.json()
    $("#user").text("Welcome, "+answer["username"])
    let getCycle=await fetch("../cycles/"+answer['cycle'],{method:"GET"})
    let cycle=await getCycle.json()
    $('#coins').text('You have '+cycle["coinsCount"]+ " coins")
    $('#clickPower').text('Your click power is '+cycle["clickPower"])
}

async function buyBoost(){
    let response = await fetch("../buyBoost/", {
        method: "GET",
        headers: {"X-Requested-With": "XMLHttpRequest"}
    });
    let answer = await response.json();
    $("#clickPower").text("Your click power is "+answer['clickPower'])
    $('#coins').text('You have '+answer["coinsCount"]+ " coins")
}