function construct_html_from_weather_json(weather_data, target_dom) {
    for (let weather_day_data of weather_data) {
        day_result = document.createElement("div")
        day_result.className = "weather_day_result"
        day_result.innerHTML = `
            ${weather_day_data["date"]} <br> 
            ${weather_day_data["condition"]} <br>
            ${weather_day_data["mintemp_c"]} ~ ${weather_day_data["maxtemp_c"]} <br>
            ${weather_day_data["suggestion"] || "Fetching Suggestion..."}
        `
        target_dom.appendChild(day_result)
    }
}

async function submit_button_handler() {
    try {
        document.getElementById("submit_button").disabled = true
        const stateInput = document.getElementById("state_input").value.trim();
        const cityInput = document.getElementById("city_input").value.trim();
        const zipCodeInput = document.getElementById("zip_code_input").value.trim() || "";
        const daysInput = document.getElementById("days_input").value.trim() || "1";

        // Validate: either zip_code or both state and city must be filled
        if (!zipCodeInput && (!stateInput || !cityInput)) {
            alert("Please provide either a zip code OR both state and city.");
            return;
        }
    
        const zipCodeDisplayDiv = document.getElementById("zip_code_display");
        zipCodeDisplayDiv.innerHTML ="<p>Processing....</p>"

        // Fetch Zip Code
        const params = new URLSearchParams();
        if (stateInput) params.append("state", stateInput);
        if (cityInput) params.append("city", cityInput);
        if (zipCodeInput) params.append("zip_code", zipCodeInput);

        // Call the backend endpoint
        const response = await fetch(`/get_zip_code?${params.toString()}`);

        // In order to use raw text: const data = JSON.parse(await response.text());
        const data = await response.json()

        // Render the response on the page
        if (!data["zip_code"]) {

            zipCodeDisplayDiv.innerHTML = `<p>No zip code found.</p>`;
            return;            
        } 
        zipCodeDisplayDiv.innerHTML = `<p><strong>Using Zip Code:</strong> ${data["zip_code"]}</p>`;

        // Fetch weather
        const weatherDisplayDiv = document.getElementById("weather_display");
        weatherDisplayDiv.innerHTML ="<p>Fetching Weather....</p>"

        const weather_params = new URLSearchParams();
        weather_params.append("zip_code", data["zip_code"]);
        weather_params.append("days", daysInput);
        const weather_response = await fetch(`/get_weather?${weather_params.toString()}`);

        const weather_data = await weather_response.json()
        
        weatherDisplayDiv.innerHTML=""
        construct_html_from_weather_json(weather_data, weatherDisplayDiv)

        // Fetch Suggestion
        const weather_response_with_suggestion = await fetch(
            `/get_wearing_suggestion`, {
                method: "POST",
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(weather_data)
            }
        )

        const weather_data_with_suggestion = await weather_response_with_suggestion.json()

        weatherDisplayDiv.innerHTML=""
        construct_html_from_weather_json(weather_data_with_suggestion, weatherDisplayDiv)

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = `<p>An error occurred: ${error.message}</p>`;
    } finally {
        document.getElementById("submit_button").disabled = false
    }
}

document.getElementById("submit_button").addEventListener("click", submit_button_handler);
