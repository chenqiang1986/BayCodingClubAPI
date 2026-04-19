var CLICK_COUNT = 0

document.getElementById('clickButton').addEventListener(
    'click', 
    function() {
        CLICK_COUNT += 1
        new_elmt = document.createElement('div')
        new_elmt.id = `CLICK_COUNTING_${CLICK_COUNT}`
        new_elmt.innerHTML=`You clicked me for ${CLICK_COUNT} times`
        
        document.getElementById('display_area').appendChild(new_elmt)

        if (CLICK_COUNT > 3) {
            count_to_remove = CLICK_COUNT - 3
            id_to_remove =`CLICK_COUNTING_${count_to_remove}`
            elmt_to_remove = document.getElementById(id_to_remove)

            elmt_to_remove.remove()
        }
    }
);

document.getElementById('backendButton').addEventListener(
    'click', 
    async function() {

        num1_textbox = document.getElementById("num1_textbox")
        num2_textbox = document.getElementById("num2_textbox")

        response = await fetch("/my_backend", {
            method: "POST",
            body: JSON.stringify({
                "num1": parseInt(num1_textbox.value),
                "num2": parseInt(num2_textbox.value)
            })
        })

       response_text = await response.text()
       response_obj = JSON.parse(response_text)

       if (response_obj["sum"] != null) { 
            document.getElementById("display_area_for_backend").innerHTML = response_obj["sum"]
       } 
       else {
            alert("Error: " + response_obj["error"])
       }
    }
);