
var loading = document.getElementById("loading");

function run() {
    
    var bar = document.getElementById("bar");
    var process = document.getElementById("process");
    var light = document.getElementById("light");
    
    if (bar.style.width == "78%") {
        light.style.display = "inline-block";
    }
    else if (bar.style.width == "100%") {
        clearTimeout(timeout);
        return;
    }
    bar.style.width = parseInt(bar.style.width) + 2 + "%";
    process.innerText = bar.style.width;
    
    var timeout = setTimeout('run()', 25);
}


document.onreadystatechange = goLoading;


function goLoading() {
    loading.style.display = "inline-block";
    run();
    var int=self.setInterval(function(){  
        if (document.readyState == "complete") {
            loading.style.display = "none";
        }  
        },2000) 
    
}
