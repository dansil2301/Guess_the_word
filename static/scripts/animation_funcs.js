function draw (element, time, right) {
    time /= 100;
    let side = 1;
    if (!right) {
        side = -1;
    }
    let position = side*(Math.pow(time, 2) * (time-7) / 0.4);
    if (position <= -1150 || position >= 1150){
        element.remove();
    }
    else {
        element.style.left =  position + 'px';
    }
}

function heading_animation (element, time, right) {
    time /= 100;
    let pos = Math.pow(time, 2) * (time-9) / 6.5;
    let size = 128 + Math.pow(time, 2) * (time-9) / 10;

    if (pos <= 170) {
        element.style.top = pos  + 'px';
    }
    else {
        element.style.top = 170 + 'px';
    }

    if (size <= 175) {
        element.style.fontSize = size + 'px';
    }
    else {
        element.style.fontSize = 128 + 175 + 'px';
    }
}

function timer_animation (element, start, duration, right=true, func) {
    let timePassed = Date.now() - start;

    if (timePassed >= duration) {
        clearInterval(undefined);
        return;
    }

    func(element, timePassed, right);
}

function main_animation (el, button_names, refs, post=false) {
    let current_time = Date.now();
    const duration = 1740;

    for (let i = 0; i < button_names.length; i++) {
        let wait = 65 * i;
        setTimeout(function () {(current_time = Date.now())}, wait);

        let element = document.getElementById(button_names[i]);
        element.setAttribute('disabled', true);

        if (i % 2 === 0){
            setTimeout(function () {
                setInterval(timer_animation, 20, element, current_time, duration, true, draw)}, wait)
            //setInterval(timer_animation, 20, element, current_time, duration, true, draw);
        }
        else {
            setTimeout(function () {
                setInterval(timer_animation, 20, element, current_time, duration, false, draw)}, wait)
            //setInterval(timer_animation, 20, element, current_time, duration, false, draw);
        }
    }

    let element = document.getElementsByTagName("h1");
    element[0].style.animation = "None";
    element[0].style.webkitAnimation = "None";
    setInterval(timer_animation, 20, element[0], current_time, duration, true, heading_animation);

    if (post) {
        $.ajax({
            type: "POST",
            url: "/difficulty",
            data: {'name': el},
            cache: false
        });
    }

    for (let i = 0; i < refs.length; i++){
        if (button_names[i] === el){
            setTimeout(function () {
                window.location.href = refs[i];
            }, duration);
            break;
        }
    }
}
