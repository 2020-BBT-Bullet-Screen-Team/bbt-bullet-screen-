var sendText = document.getElementById("sendText");
var sendButton = document.getElementById("sendButton");
var receiveBox = document.getElementById("receive-box");
var bulletButton = document.getElementById("bulletButton");
var wrapper = document.getElementById("wrapper");
var time = setInterval(function () {
    init();
}, 1000);
//button start
sendButton.addEventListener("click", function () {
    ws.send(sendText.value);
})
bulletButton.addEventListener("click", function () {
    if (bulletButton.checked) {
        console.log(true);
        time = setInterval(function () {
            init();
        }, 1000);
        //
    } else {
        console.log(false);
        //
        hideBullet();
        clearInterval(time);

    }
})
//button end
//function start
function addMes(tag, text, father) {
    var node = document.createElement(tag);
    var textnode = document.createTextNode(text);
    node.appendChild(textnode);
    father.appendChild(node);
    return node;
}

function move(dom, classname) {
    setTimeout(function () {
        dom.classList.add(classname);

    }, 1000);
}

function showBullet() {
    var bullet = document.getElementsByClassName("right");
    for (let i = 0; i < bullet.length; i++) {
        bullet[i].style.display = "inline-block";
    }
}

function hideBullet() {
    var bullet = document.getElementsByClassName("right");
    for (let i = 0; i < bullet.length; i++) {
        bullet[i].style.display = "none";
    }
}
//function end


var bulletPool = [];
// Create WebSocket connection.
const ws = new WebSocket(baseurl);

// Connection opened
ws.addEventListener('open', function (event) {
    console.log("Connection open...");
    ws.send('Hello Server!');
});
// Connection error
ws.onerror = function (event) {
    console.log("连接失败");
}

// Listen for messages
ws.addEventListener('message', function (event) {
    console.log('Message from server: ', event.data);
    addMes("p", event.data, receiveBox);
    bulletPool.push(event.data);
    console.log(bulletPool);

});
//关闭
ws.onclose = function (event) {
    console.log("Connection closed");
};

const lineMaxCount = 3;
const bulletMaxCount = 12;

function init() {
    var wrapper = document.getElementById("wrapper");
    for (let i = 0; i < bulletPool.length; i++) {
        var x = addMes("span", bulletPool[i], wrapper);
        x.classList.add("right");
        x.style.top = 20 + Math.floor(Math.random() * 10) * 50 + "px";
        x.style.right = -x.offsetWidth + "px";
        move(x, "left");
        var distance = x.offsetWidth + 540;
        x.style.transform = "translateX(-" + distance + "px)";


    }


}