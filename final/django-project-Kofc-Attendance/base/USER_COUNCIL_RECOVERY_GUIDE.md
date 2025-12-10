# User Council Recovery Guide

## Problem
When councils were deleted or the migration was applied, users lost their council assignments, causing:
- "Too many redirects" error when logging in
- Officers and members unable to access their dashboards
- Infinite redirect loops in the dashboard views

## Root Cause
The User model has a ForeignKey to Council with `on_delete=models.SET_NULL`. When councils were deleted, users' council field was set to NULL, and the dashboard views were redirecting users without councils back to the dashboard, creating an infinite loop.

## Solution Applied

### 1. Fixed Redirect Loop (views.py)
✅ Updated `officer_dashboard()` to render `no_council.html` instead of redirecting
✅ Updated `member_dashboard()` to render `no_council.html` instead of redirecting
✅ This prevents the infinite redirect loop and shows users a helpful message

### 2. Created Management Command
✅ Created `reassign_users_to_councils.py` management command to reassign users to councils

## How to Recover Users

### Step 1: Ensure Councils Exist
First, make sure you have at least one council created in the system. If not, create one:
1. Log in as admin
2. Go to Manage Councils
3. Add a new council

### Step 2: Run the Recovery Command

#### Option A: Reassign all users without councils to the first available council
```bash
python manage.py reassign_users_to_councils
```

#### Option B: Reassign only members to a specific council
```bash
python manage.py reassign_users_to_councils --role member --council-id 1
```

#### Option C: Reassign only officers to a specific council
```bash
python manage.py reassign_users_to_councils --role officer --council-id 1
```

### Step 3: Verify Users Can Log In
- Try logging in with an affected user account
- You should now be able to access the dashboard without redirect errors

## What the Command Does
1. Finds all users without a council assignment
2. Optionally filters by role (member/officer)
3. Assigns them to the specified council (or first available council)
4. Shows a summary of reassigned users

## Manual Reassignment (Alternative)
If you prefer to reassign users manually:

1. Log in as admin
2. Go to Member List
3. For each user without a council:
   - Click the Edit button
   - Select a council from the dropdown
   - Save changes

## Preventing This in the Future
✅ Never delete councils that have members assigned
✅ Always reassign members to another council before deleting
✅ The system now prevents deletion of councils with active members

## Files Modified
- `capstone_project/more_views/views.py` - Fixed redirect loops
- `capstone_project/management/commands/reassign_users_to_councils.py` - New recovery command

## Testing
After recovery, test with:
1. Admin user - should see admin dashboard
2. Officer user - should see officer dashboard with their council
3. Member user - should see member dashboard with their council
4. User without council - should see no_council.html message
