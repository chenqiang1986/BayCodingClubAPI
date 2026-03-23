# Wearing Suggestion Project - Homework Instructions

## Project Overview
Build a web application that provides clothing suggestions based on weather forecasts for a given location. The application takes user input (state, city, or zip code) and number of days, fetches weather data, and uses AI to suggest appropriate clothing.

---

## Step 1: Build Backend Endpoints

Implement three Flask endpoints in `app.py` to handle the following operations:

### Endpoint 1: `/get_zip_code` (GET Request)

**Purpose:** Normalize and validate the user's location input by converting state/city to zip code.

**Input Parameters (Query String):**
- `state` (string, optional): US state name or abbreviation (e.g., "California", "CA")
- `city` (string, optional): City name (e.g., "San Francisco")
- `zip_code` (string, optional): 5-digit zip code (e.g., "94105")

**Input Validation Logic:**
- If `zip_code` is provided, return it directly (highest priority)
- If `zip_code` is not provided, both `state` AND `city` must be provided
- If none are valid, return `None`

**Output Format (JSON):**
```json
{
  "zip_code": "94105"
}
```

**Output Format (Error Case):**
```json
{
  "zip_code": null
}
```

**Implementation Details:**
- Use the external API: `https://api.sipcode.dev/state/{state}/city/{city}/zip_codes`
- Return the first zip code from the results
- Handle the case where no zip codes are found

---

### Endpoint 2: `/get_weather` (GET Request)

**Purpose:** Fetch weather forecast data for a given location and number of days.

**Input Parameters (Query String):**
- `zip_code` (string, required): 5-digit zip code
- `days` (string, required): Number of days to forecast (1-10)

**Output Format (JSON Array):**
```json
[
  {
    "date": "2026-03-23",
    "condition": "Partly cloudy",
    "maxtemp_c": "22°C",
    "mintemp_c": "15°C"
  },
  {
    "date": "2026-03-24",
    "condition": "Rainy",
    "maxtemp_c": "18°C",
    "mintemp_c": "12°C"
  }
]
```

**Output Format (Error Case):**
```json
[]
```

**Implementation Details:**
- Use the external API: `http://api.weatherapi.com/v1/forecast.json`
- Requires `WEATHER_API_KEY` environment variable from `.env` file
- Extract forecast data for the specified number of days
- Return an empty array if the API request fails or status code is not 200

---

### Endpoint 3: `/get_wearing_suggestion` (POST Request)

**Purpose:** Generate AI-powered clothing suggestions based on weather data.

**Input Format (JSON Request Body):**
```json
[
  {
    "date": "2026-03-23",
    "condition": "Partly cloudy",
    "maxtemp_c": "22°C",
    "mintemp_c": "15°C"
  }
]
```

**Output Format (JSON Array):**
```json
[
  {
    "date": "2026-03-23",
    "condition": "Partly cloudy",
    "maxtemp_c": "22°C",
    "mintemp_c": "15°C",
    "suggestion": "Wear a light jacket and jeans. No umbrella needed."
  }
]
```

**Implementation Details:**
- Use Google's Gemini API (`google_genai` library)
- For each weather day, construct a prompt with: date, weather condition, min/max temperatures
- Request clothing suggestion advice from the AI model (model: "gemini-3-flash-preview")
- Add the `suggestion` field to each weather day object
- Suggestions should be concise (one sentence)

---

## Step 2: Build the Frontend HTML/JavaScript

Create an interactive web interface in `templates/index.html` and `static/index_script.js` that allows users to input location and view weather-based clothing suggestions.

### Visual Layout & Components

**Input Form Elements:**
1. **State Input**
   - Label: "State:"
   - Input type: text field
   - Placeholder: Accept state names or abbreviations

2. **City Input**
   - Label: "City:"
   - Input type: text field
   - Note: Required if zip code not provided

3. **Zip Code Input (Optional)**
   - Label: "Zip Code (optional):"
   - Input type: text field
   - Note: If provided, state and city are ignored

4. **Days Input**
   - Label: "Days:"
   - Input type: text field
   - Default value: "1" if empty

5. **Submit Button**
   - Button text: "Submit"
   - Button ID: `submit_button`
   - Behavior: Should be disabled while processing

### Display Areas

**Zip Code Display Area:**
- Element ID: `zip_code_display`
- Shows: "Using Zip Code: [resolved_zip_code]" after successful lookup
- Error state: "No zip code found." if location cannot be resolved

**Weather Display Area:**
- Element ID: `weather_display`
- Shows loading message: "Fetching Weather...." during processing
- Shows loading message: "Processing...." during initial location lookup

### Button Click Behavior & Event Flow

**Step-by-Step Flow When Submit Button is Clicked:**

1. **Disable the button** to prevent duplicate submissions
2. **Validate inputs:**
   - Either `zip_code` OR both `state` AND `city` must be provided
   - If invalid, show alert: "Please provide either a zip code OR both state and city."
3. **Display processing message:** "Processing...." in zip code display area
4. **Fetch zip code:**
   - Call `GET /get_zip_code` with state/city/zip_code parameters
   - Parse JSON response
   - If no zip code found, display error and stop
   - If successful, display: "Using Zip Code: [zip_code]"
5. **Display loading message:** "Fetching Weather...." in weather display area
6. **Fetch weather data:**
   - Call `GET /get_weather` with zip code and days parameters
   - Parse JSON response
   - Clear the weather display and render weather cards (without suggestions yet)
7. **Fetch clothing suggestions:**
   - Call `POST /get_wearing_suggestion` with weather data as JSON body
   - Send in request header: `'Content-Type': 'application/json'`
   - Parse JSON response with suggestions added
8. **Render final results:**
   - Clear the weather display
   - Render weather cards with AI suggestions
9. **Re-enable button** in the `finally` block for future submissions

### Weather Card Rendering

**For each day in the forecast:**
- Create a `div` element with class: `weather_day_result`
- Display the following information (separated by line breaks):
  - `date` (e.g., "2026-03-23")
  - `condition` (e.g., "Partly cloudy")
  - Temperature range: `mintemp_c` ~ `maxtemp_c` (e.g., "15°C ~ 22°C")
  - `suggestion` (if available, show AI suggestion; if still loading, show "Fetching Suggestion...")

### Error Handling

- Wrap the entire button handler in try-catch-finally
- If an error occurs, display: `<p>An error occurred: [error message]</p>` in the result area
- Always re-enable the submit button in the `finally` block
- Log errors to browser console for debugging

---

## Summary of Key Requirements

### Backend:
- ✅ Three endpoints with proper HTTP methods (GET, POST)
- ✅ Correct JSON input/output formats
- ✅ API integration (zipcode API, weather API, Gemini AI)
- ✅ Environment variable usage (WEATHER_API_KEY)
- ✅ Error handling for API failures

### Frontend:
- ✅ Input form with 4 fields (state, city, zip code, days)
- ✅ Form validation before submission
- ✅ Loading states and user feedback messages
- ✅ Dynamic HTML rendering of weather data
- ✅ Proper async/await for API calls
- ✅ Button disable/enable during processing
- ✅ Clean, user-friendly interface
