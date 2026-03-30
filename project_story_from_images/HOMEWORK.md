# Story Generation from Images - Project Documentation

## Overview
This project is a web application that allows users to upload images, automatically generates descriptions for each image, and creates a cohesive story that ties all the images together using AI.

---

## Backend

### Technology Stack
- **Framework**: Flask (Python)
- **AI Integration**: Google Generative AI (Gemini)
- **Environment Management**: python-dotenv

### Backend Endpoints

#### 1. **GET `/`**
**Functionality**: Serves the main HTML frontend page.

**Input**: None (HTTP GET request)

**Output**: 
- HTML page (index.html)

**Status Code**: 200 (Success)

---

#### 2. **POST `/summary_image`**
**Functionality**: Analyzes a single image and generates a description of what's in the image.

**Input**:
```json
{
  "url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA... (data URL string)"
}
```

**Output**:
```json
{
  "description": "A person standing on a beach at sunset with waves in the background"
}
```

**Status Code**: 200 (Success)

---

#### 3. **POST `/generate_story`**
**Functionality**: Creates a complete narrative story that connects multiple images based on their descriptions.

**Input**:
```json
[
  {
    "data_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA...",
    "description": "A person standing on a beach at sunset with waves in the background"
  },
  {
    "data_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA...",
    "description": "A campfire with friends gathered around at night"
  },
  {
    "data_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA...",
    "description": "A mountain landscape with snow-capped peaks"
  }
]
```

**Output**:
```json
{
  "story": "Once upon a time, a group of friends decided to embark on an adventure. They started their journey at a beautiful beach, watching the golden sunset reflect on the waves. As darkness fell, they gathered around a warm campfire, sharing stories and laughter under the stars. Their final destination was the breathtaking mountain landscape with snow-capped peaks, reminding them that nature's beauty is boundless. This journey became a memory they would cherish forever."
}
```

**Status Code**: 200 (Success)

---

## Frontend

### Technology Stack
- **HTML5**: Page structure and semantic markup
- **CSS**: Styling (index.css)
- **JavaScript**: Vanilla JavaScript (ES6+) for interactivity
- **APIs**: Fetch API for HTTP communication

### Frontend Components

#### 1. **Image Upload Section**
- Located at the top of the page
- Allows users to select multiple image files at once
- Accepts: JPG, PNG, GIF, and WebP formats
- Uses HTML `<input type="file" multiple accept="image/*">`

#### 2. **Preview Container**
- Dynamically populated with image cards after file selection
- Each image card contains:
  - Preview image thumbnail
  - Loading indicator ("Fetching Description...")
  - Textarea with auto-generated image description (editable)

#### 3. **Story Container**
- Appears after images are uploaded and processed
- Contains:
  - "Generate Story" button
  - Large textarea displaying the generated story

### Frontend JavaScript Workflow

#### File: `file_upload.js`
**Main Function**: `handleFileSelect(event)`
- Triggered when user selects images
- Calls `processImageFile(files)` to process all selected files

**Helper Function**: `readFileAsync(file)`
- Converts file to base64 data URL
- Returns a Promise that resolves with the data URL

**Main Processing Function**: `processImageFile(files)`
1. Converts each selected file to a data URL
2. Creates image cards for each image with preview and loading text
3. For each image, makes a POST request to `/summary_image`
4. Receives description from backend
5. Replaces loading text with editable textarea containing description
6. Displays "Generate Story" button once all descriptions are fetched

#### File: `story_gen.js`
**Main Function**: `handleGenerateStory()`
- Triggered when user clicks "Generate Story" button
- Collects all image URLs and their descriptions from the DOM
- Sends data to `/generate_story` endpoint
- Displays the generated story in the story textarea

### Data Flow Diagram

```
User Upload Images
     ↓
readFileAsync() - Convert to base64 data URLs
     ↓
Create image cards with preview images
     ↓
Send each image to /summary_image endpoint
     ↓
Display description in editable textarea
     ↓
Show "Generate Story" button
     ↓
User clicks "Generate Story"
     ↓
Collect all images + descriptions from DOM
     ↓
Send to /generate_story endpoint
     ↓
Display final story in story textarea
```

### User Journey

1. **Upload**: User clicks "Select Images" and chooses multiple image files
2. **Preview & Description**: 
   - Images are previewed immediately
   - AI generates descriptions for each image (shown in textareas)
   - User can edit descriptions if needed
3. **Story Generation**: User clicks "Generate Story" button
4. **View Story**: AI generates and displays a cohesive narrative combining all images

---

## Key Features

- ✅ Multiple image upload support
- ✅ Automatic image description generation using AI
- ✅ Editable image descriptions for customization
- ✅ AI-powered story generation combining all images
- ✅ Responsive preview interface
- ✅ Real-time processing feedback

---
