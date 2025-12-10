# Council Location & ID Update Implementation

## Overview
Added location fields directly to the Council model and implemented automatic council ID updates when council names are changed.

## Changes Made

### 1. Database Model Updates

**File: `models.py`**

Added 5 location fields to the `Council` model:
```python
class Council(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    location_street = models.CharField(max_length=255, null=True, blank=True)
    location_barangay = models.CharField(max_length=100, null=True, blank=True)
    location_city = models.CharField(max_length=100, null=True, blank=True)
    location_province = models.CharField(max_length=100, null=True, blank=True)
    location_zip_code = models.CharField(max_length=10, null=True, blank=True)
```

### 2. Backend Views Updates

**File: `more_views/council.py`**

#### `add_council()` - Updated
- Now accepts location fields from form
- Saves location information when creating new council
- Extracts council ID from name (first number found)
- Falls back to auto-increment if no number in name

#### `edit_council()` - Updated
- Now accepts and saves location fields
- **NEW**: Automatically updates council ID when name changes
  - Extracts first number from new council name
  - Validates new ID doesn't already exist
  - Updates council.id before saving
- Example: "Council 1234" → "Council 11701" changes ID from 1234 to 11701

### 3. Frontend Template Updates

**File: `templates/manage_councils.html`**

#### Add Council Modal
- Added 5 location input fields (street, barangay, city, province, zip code)
- All location fields are optional
- Fields: location_street, location_barangay, location_city, location_province, location_zip_code

#### Edit Council Modal
- Added same 5 location input fields
- Updated `openEditCouncilModal()` JavaScript function to accept and populate location parameters
- Location fields pre-populate with existing council location data

#### Edit Button
- Updated to pass location data to modal: `openEditCouncilModal(councilId, name, district, street, barangay, city, province, zipCode)`

## How to Use

### Adding a Council with Location
1. Go to "Manage Councils"
2. Click "Add New Council"
3. Fill in:
   - Council Name (required, e.g., "Council 1234")
   - District (required)
   - Location Street (optional)
   - Location Barangay (optional)
   - Location City (optional)
   - Location Province (optional)
   - Location ZIP Code (optional)
4. Click "Add Council"

### Editing Council Location
1. Go to "Manage Councils"
2. Click "Edit" on a council
3. Update location fields as needed
4. Click "Update Council"

### Updating Council ID via Name Change
1. Go to "Manage Councils"
2. Click "Edit" on a council
3. Change council name from "Council 1234" to "Council 11701"
4. Click "Update Council"
5. Council ID automatically updates to 11701

## Database Migration

Run these commands to apply changes:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will add the 5 new location fields to the Council table.

## Key Features

✅ **Location fields directly on Council model** - No separate Location model needed
✅ **Automatic Council ID updates** - ID syncs with council name number
✅ **Optional location data** - All location fields are nullable
✅ **Admin-only operations** - Only admins can add/edit councils
✅ **Validation** - Prevents duplicate council IDs
✅ **Backward compatible** - Existing councils work without location data

## Technical Details

### Council ID Update Logic
1. Extract all numbers from new council name using regex: `\d+`
2. Use first number as new council ID
3. Validate new ID doesn't already exist
4. If valid, update council.id before saving
5. If invalid, show error and prevent update

### Location Fields
- All optional (null=True, blank=True)
- Stored directly on Council model
- No foreign key relationships
- Simple string fields for flexibility

## Files Modified

- `models.py` - Added location fields to Council
- `more_views/council.py` - Updated add_council() and edit_council()
- `templates/manage_councils.html` - Added location UI to modals

## Testing Checklist

- [ ] Run migrations successfully
- [ ] Add council with location data
- [ ] Edit council location
- [ ] Update council name to change ID (e.g., 1234 → 11701)
- [ ] Verify ID changed correctly
- [ ] Create council without location data (optional fields)
- [ ] Verify existing councils still work
- [ ] Test with different user roles (only admin should work)

## Notes

- Council ID is the primary key, so changing it requires careful handling
- Location data is stored as separate fields for simplicity
- No cascade delete or foreign key constraints on location fields
- Location data is independent of events - events still have their own address fields
