# Location Features Guide

## What's New

### 1. Dropdown Menus for Location Selection
- **Province Dropdown**: Select from 5 CALABARZON provinces
- **City Dropdown**: Dynamically populated based on province
- **Barangay Dropdown**: Dynamically populated based on city
- **Street Address**: Free text input (optional)
- **ZIP Code**: Free text input (optional)

### 2. Input Validation
- Province must be selected before city becomes available
- City must be selected before barangay becomes available
- Street and ZIP code are optional
- All dropdowns reset when parent selection changes

### 3. Location Display on Public Page
- Council cards now show location information
- Location displays below council name
- Shows: Street, Barangay, City, Province
- Only displays if location data exists

## User Workflows

### Admin: Add Council with Location

1. Go to **Manage Councils**
2. Click **Add New Council**
3. Fill in:
   - **Council Name** (required): "Council 1234"
   - **District** (required): "CALABARZON"
   - **Province** (optional): Select from dropdown
   - **City** (optional): Becomes available after province selection
   - **Barangay** (optional): Becomes available after city selection
   - **Street Address** (optional): Type street name
   - **ZIP Code** (optional): Type ZIP code
4. Click **Add Council**

### Admin: Edit Council Location

1. Go to **Manage Councils**
2. Click **Edit** on a council
3. Update location fields:
   - Change province → city/barangay dropdowns reset
   - Change city → barangay dropdown resets
   - Update street or ZIP code
4. Click **Update Council**

### Member: View Council Locations

1. Go to **Councils** page
2. View council cards
3. Each card shows:
   - Council name
   - Location information (if available)
4. Click card to view council details

## Dropdown Behavior

### Province Selection
```
Province Dropdown
├── Batangas
├── Cavite
├── Laguna
├── Quezon
└── Rizal
```

### City Selection (Example: Batangas)
```
City Dropdown (Batangas)
├── Batangas City
└── Lipa City
```

### Barangay Selection (Example: Batangas City)
```
Barangay Dropdown (Batangas City)
├── Alangilan
├── Balagtas
├── Balete
├── Banaba Center
├── ... (24 barangays total)
└── Barangay 24
```

## Validation Rules

| Field | Required | Type | Validation |
|-------|----------|------|-----------|
| Province | No | Dropdown | Must select to enable city |
| City | No | Dropdown | Must select to enable barangay |
| Barangay | No | Dropdown | Depends on city selection |
| Street | No | Text | Max 255 characters |
| ZIP Code | No | Text | Max 10 characters |

## Features

✅ **Cascading Dropdowns** - Dropdowns populate based on parent selection
✅ **Input Validation** - Prevents invalid selections
✅ **Location Display** - Shows on public councils page
✅ **Optional Fields** - All location fields are optional
✅ **Data Persistence** - Location data saved with council
✅ **Edit Support** - Can update location anytime
✅ **Responsive Design** - Works on mobile devices
✅ **Dark Mode Support** - Location styling works in dark mode

## Location Data Available

### Batangas
- **Batangas City** (ZIP: 4200)
  - 24 barangays including Alangilan, Balagtas, Balete, etc.
- **Lipa City** (ZIP: 4217)
  - 50+ barangays including Adya, Anilao, Antipolo, etc.

### Cavite
- **Kawit** (ZIP: 4109)
  - 5 barangays
- **Rosario** (ZIP: 4118)
  - 4 barangays

### Laguna
- **Lucena** (ZIP: 4301)
  - 6 barangays
- **Candelaria** (ZIP: 4304)
  - 3 barangays

### Quezon
- **Quezon City** (ZIP: 1100)
  - 4 barangays

### Rizal
- **Antipolo** (ZIP: 1870)
  - 4 barangays

## Technical Details

### Frontend
- **Dropdowns**: HTML `<select>` elements
- **Validation**: JavaScript event handlers
- **Cascading**: `updateCityDropdown()` and `updateBarangayDropdown()` functions
- **Data**: `locationData` JavaScript object

### Backend
- **Model**: Council model with location fields
- **Fields**: location_street, location_barangay, location_city, location_province, location_zip_code
- **Validation**: Django form validation
- **Storage**: Simple string fields (no foreign keys)

## Browser Support

- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- Mobile browsers: ✅ Full support
- IE 11: ⚠️ Limited support (basic functionality)

## Troubleshooting

### City dropdown not showing
- **Cause**: Province not selected
- **Solution**: Select a province first

### Barangay dropdown not showing
- **Cause**: City not selected
- **Solution**: Select a city first

### Location not displaying on public page
- **Cause**: No location data saved for council
- **Solution**: Edit council and add location information

### Dropdown values not saving
- **Cause**: Form submission error
- **Solution**: Check browser console for errors, verify form is valid

## Future Enhancements

- Auto-fill ZIP code based on barangay
- Search functionality in dropdowns
- Add more provinces/regions
- Location map integration
- Location search on public page
- Location availability calendar

## Notes

- Location data is hardcoded for CALABARZON region
- Can be extended to include more regions
- All location fields are optional
- Location data is independent of events
- Dropdowns use JavaScript for dynamic population
- No database queries needed for location data
