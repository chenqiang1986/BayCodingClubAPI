
CLICK_BUTTON = document.getElementById('clickButton')
CLICK_BUTTON.addEventListener('click', clickButtonHandler);

CONTENT_DIV = document.getElementById('my_content')

CLICK_TIMES = 0

function clickButtonHandler() {
    console.log("Button was clicked.")
    CLICK_TIMES +=1

    new_elmt = document.createElement("div")
    new_elmt.id=`click_counting_${CLICK_TIMES}`
    new_elmt.innerHTML=`You clicked the Button ${CLICK_TIMES} times`

    CONTENT_DIV.appendChild(new_elmt)

    if (CLICK_TIMES > 3) {
        to_remove_id = `click_counting_${CLICK_TIMES - 3}`
        to_remove_elmt = document.getElementById(to_remove_id)
        to_remove_elmt.remove()
    }
}


BACKEND_BUTTON = document.getElementById('backendCall')
BACKEND_BUTTON.addEventListener('click', backendButtonHandler);

async function backendButtonHandler() {
    try{
        NUM1_TEXTBOX = document.getElementById('num1_input')
        NUM2_TEXTBOX = document.getElementById('num2_input')

        response = await fetch("/my_backend", {
            method: "POST",
            body: JSON.stringify({
                "num1": parseInt(NUM1_TEXTBOX.value),
                "num2": parseInt(NUM2_TEXTBOX.value)
            })
        })
        
        response_text = await response.text()

        response_obj = JSON.parse(response_text)

        new_elmt = document.createElement("div")
        new_elmt.innerHTML = response_obj["sum"]

        CONTENT_DIV.appendChild(new_elmt)
    }
    catch(e) {
        alert(e)
    }
}


