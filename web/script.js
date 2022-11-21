function gettime() {
    let datetime = new Date().toLocaleTimeString();

    document.getElementById("time").textContent = datetime;
    }

    setInterval(gettime, 1000);