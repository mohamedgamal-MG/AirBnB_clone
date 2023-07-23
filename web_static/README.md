# AirBnB Clone - Web Static

## Task 0: Inline Styling

### Description
Write an HTML page that displays a header and a footer with inline styling.

#### Layout:

**Body:**
- No margin
- No padding

**Header:**
- Color: #FF0000 (red)
- Height: 70px
- Width: 100%

**Footer:**
- Color: #00FF00 (green)
- Height: 60px
- Width: 100%
- Text: "Best School" (centered vertically and horizontally)
- Always at the bottom of the page

### Requirements:
- You must use the `header` and `footer` tags.
- You are not allowed to import any files.
- You are not allowed to use the `style` tag in the `head` tag.
- Use inline styling for all your tags.

## Task 1: Head Styling

### Description
Write an HTML page that displays a header and a footer with styling inside the `style` tag in the `head` tag (same as Task 0).

### Requirements:
- You must use the `header` and `footer` tags.
- You are not allowed to import any files.
- No inline styling.
- You must use the `style` tag in the `head` tag.
- The layout must be exactly the same as Task 0.

## Task 2: CSS Files

### Description
Write an HTML page that displays a header and a footer by using CSS files (same as Task 1).

### Requirements:
- You must use the `header` and `footer` tags.
- No inline styling.
- You must have 3 CSS files:
  - `styles/2-common.css`: for global style (i.e. the body style)
  - `styles/2-header.css`: for header style
  - `styles/2-footer.css`: for footer style
- The layout must be exactly the same as Task 1.

## Task 3: Zoning Done!

### Description
Write an HTML page that displays a header and a footer by using CSS files (same as Task 2).

### Layout:

**Common:**
- No margin
- No padding
- Font color: #484848
- Font size: 14px
- Font family: Circular, "Helvetica Neue", Helvetica, Arial, sans-serif
- Icon in the browser tab

**Header:**
- Color: white
- Height: 70px
- Width: 100%
- Border bottom: 1px #CCCCCC
- Logo aligned on the left and centered vertically (20px space at the left)

**Footer:**
- Color: white
- Height: 60px
- Width: 100%
- Border top: 1px #CCCCCC
- Text: "Best School" (centered vertically and horizontally)
- Always at the bottom of the page

### Requirements:
- No inline style
- You are not allowed to use the `img` tag
- You are not allowed to use the `style` tag in the `head` tag
- All images must be stored in the `images` folder
- You must have 3 CSS files:
  - `styles/3-common.css`: for the global style (i.e. body style)
  - `styles/3-header.css`: for the header style
  - `styles/3-footer.css`: for the footer style

## Task 4: Search!

### Description
Write an HTML page that displays a header, footer, and a filters box with a search button.

### Layout: (based on Task 3)

**Container:**
- Between `header` and `footer` tags, add a `div`:
  - Classname: container
  - Max width: 1000px
  - Margin top and bottom: 30px (it should be 30px under the bottom of the header - screenshot)
  - Center horizontally

**Filter section:**
- Tag: `section`
- Classname: filters
- Inside the `.container`
- Color: white
- Height: 70px
- Width: 100% of the container
- Border: 1px #DDDDDD with radius 4px

**Button search:**
- Tag: `button`
- Text: "Search"
- Font size: 18px
- Inside the section `filters`
- Background color: #FF5A5F
- Text color: #FFFFFF
- Height: 48px
- Width: 20% of the section `filters`
- No borders
- Border radius: 4px
- Center vertically and at 30px of the right border
- Change opacity to 90% when the mouse is on the button

### Requirements:
- You must use: `header`, `footer`, `section
